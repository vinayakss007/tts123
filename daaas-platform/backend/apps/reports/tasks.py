"""Celery tasks for report generation."""
from celery import shared_task

from .models import Report


@shared_task(bind=True, max_retries=2, time_limit=600)
def generate_report(self, report_id: str, custom_instructions: str = ""):
    """Generate an AI-powered report for a dataset/analysis session."""
    try:
        report = Report.objects.select_related("dataset", "template", "analysis_session").get(id=report_id)
        report.status = Report.StatusChoices.GENERATING
        report.save(update_fields=["status"])

        from .services import ReportGenerationService

        service = ReportGenerationService()
        result = service.generate(
            report=report,
            custom_instructions=custom_instructions,
        )

        report.status = Report.StatusChoices.COMPLETED
        report.ai_tokens_used = result.get("tokens_used", 0)
        report.file_path = result.get("file_path", "")
        report.save(update_fields=["status", "ai_tokens_used", "file_path"])

    except Exception as exc:
        report = Report.objects.get(id=report_id)
        report.status = Report.StatusChoices.ERROR
        report.error_message = str(exc)
        report.save(update_fields=["status", "error_message"])
        raise self.retry(exc=exc, countdown=60)
