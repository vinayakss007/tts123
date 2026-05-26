"""Celery tasks for async dataset processing."""
from celery import shared_task

from .models import Dataset


@shared_task(bind=True, max_retries=3)
def process_dataset(self, dataset_id: str):
    """Parse, profile, and validate a newly uploaded dataset.

    Steps:
    1. Download file from storage
    2. Parse file based on type (CSV, Excel, JSON, Parquet)
    3. Extract column metadata (types, stats)
    4. Validate data quality
    5. Update dataset status to ready
    """
    try:
        dataset = Dataset.objects.get(id=dataset_id)
        dataset.status = Dataset.StatusChoices.PROCESSING
        dataset.save(update_fields=["status"])

        from .services import FileParsingService

        service = FileParsingService()
        result = service.parse_and_profile(dataset)

        dataset.row_count = result["row_count"]
        dataset.column_count = result["column_count"]
        dataset.status = Dataset.StatusChoices.READY
        dataset.save(update_fields=["row_count", "column_count", "status"])

    except Exception as exc:
        dataset = Dataset.objects.get(id=dataset_id)
        dataset.status = Dataset.StatusChoices.ERROR
        dataset.error_message = str(exc)
        dataset.save(update_fields=["status", "error_message"])
        raise self.retry(exc=exc, countdown=60)


@shared_task
def validate_dataset(dataset_id: str):
    """Run data quality validation on a dataset."""
    from .validators import DatasetValidator

    dataset = Dataset.objects.get(id=dataset_id)
    validator = DatasetValidator()
    return validator.validate(dataset)


@shared_task
def generate_dataset_profile(dataset_id: str):
    """Generate comprehensive statistical profile for a dataset."""
    dataset = Dataset.objects.get(id=dataset_id)

    from .services import FileParsingService

    service = FileParsingService()
    return service.generate_profile(dataset)
