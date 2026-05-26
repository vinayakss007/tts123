"""Celery tasks for analytics processing."""
import time

from celery import shared_task

from .models import AnalysisSession, AnalysisStep


@shared_task(bind=True, max_retries=2)
def run_analysis_step(self, step_id: str):
    """Execute a single analysis step.

    Routes to the appropriate analysis service based on step type.
    """
    try:
        step = AnalysisStep.objects.select_related("session").get(id=step_id)
        step.status = AnalysisStep.StatusChoices.RUNNING
        step.save(update_fields=["status"])

        start_time = time.time()

        from .services.statistics import StatisticsService

        service = StatisticsService()

        if step.step_type == AnalysisStep.StepTypeChoices.DESCRIPTIVE_STATS:
            result = service.descriptive_stats(step.session.dataset, step.parameters)
        elif step.step_type == AnalysisStep.StepTypeChoices.CORRELATION:
            result = service.correlation_analysis(step.session.dataset, step.parameters)
        elif step.step_type == AnalysisStep.StepTypeChoices.DISTRIBUTION:
            result = service.distribution_analysis(step.session.dataset, step.parameters)
        elif step.step_type == AnalysisStep.StepTypeChoices.HYPOTHESIS_TEST:
            result = service.hypothesis_test(step.session.dataset, step.parameters)
        else:
            result = {"message": f"Step type '{step.step_type}' not yet implemented"}

        elapsed = int((time.time() - start_time) * 1000)
        step.result = result
        step.status = AnalysisStep.StatusChoices.COMPLETED
        step.execution_time_ms = elapsed
        step.save(update_fields=["result", "status", "execution_time_ms"])

        # Check if all steps are complete
        session = step.session
        if not session.steps.filter(status=AnalysisStep.StatusChoices.PENDING).exists():
            session.status = AnalysisSession.StatusChoices.COMPLETED
            session.save(update_fields=["status"])

    except Exception as exc:
        step = AnalysisStep.objects.get(id=step_id)
        step.status = AnalysisStep.StatusChoices.ERROR
        step.error_message = str(exc)
        step.save(update_fields=["status", "error_message"])
        raise self.retry(exc=exc, countdown=30)
