"""Celery tasks for ML model training (long-running)."""
import time

from celery import shared_task
from django.utils import timezone

from .models import MLModel, ModelVersion, TrainingRun


@shared_task(bind=True, max_retries=1, time_limit=7200, soft_time_limit=7000)
def train_model(self, training_run_id: str):
    """Execute model training pipeline.

    This is a long-running task that:
    1. Loads and preprocesses the dataset
    2. Splits into train/test sets
    3. Trains the model
    4. Evaluates performance
    5. Saves model artifact
    6. Creates a ModelVersion
    """
    try:
        run = TrainingRun.objects.select_related("model", "model__dataset").get(id=training_run_id)
        run.status = TrainingRun.StatusChoices.RUNNING
        run.started_at = timezone.now()
        run.save(update_fields=["status", "started_at"])

        from .services.training import TrainingService

        service = TrainingService()
        result = service.train(
            dataset=run.model.dataset,
            model_type=run.model.model_type,
            task_type=run.model.task_type,
            target_column=run.model.target_column,
            feature_columns=run.model.feature_columns,
            hyperparameters=run.hyperparameters,
        )

        run.status = TrainingRun.StatusChoices.COMPLETED
        run.completed_at = timezone.now()
        run.duration_seconds = (run.completed_at - run.started_at).total_seconds()
        run.metrics = result.get("metrics", {})
        run.save(update_fields=["status", "completed_at", "duration_seconds", "metrics"])

        # Create model version
        version_number = run.model.versions.count() + 1
        ModelVersion.objects.create(
            model=run.model,
            training_run=run,
            version_number=version_number,
            artifact_path=result.get("artifact_path", ""),
            accuracy=result["metrics"].get("accuracy"),
            precision=result["metrics"].get("precision"),
            recall=result["metrics"].get("recall"),
            f1_score=result["metrics"].get("f1_score"),
            feature_importance=result.get("feature_importance", {}),
            is_active=True,
        )

        # Deactivate other versions
        run.model.versions.exclude(version_number=version_number).update(is_active=False)

        run.model.status = MLModel.StatusChoices.TRAINED
        run.model.save(update_fields=["status"])

    except Exception as exc:
        run = TrainingRun.objects.get(id=training_run_id)
        run.status = TrainingRun.StatusChoices.FAILED
        run.error_message = str(exc)
        run.completed_at = timezone.now()
        run.save(update_fields=["status", "error_message", "completed_at"])

        run.model.status = MLModel.StatusChoices.ERROR
        run.model.save(update_fields=["status"])

        raise self.retry(exc=exc, countdown=120)
