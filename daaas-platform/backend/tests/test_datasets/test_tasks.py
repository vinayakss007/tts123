"""Tests for dataset async tasks."""
import pytest

from apps.datasets.models import Dataset
from apps.datasets.tasks import process_dataset, validate_dataset


@pytest.mark.django_db
class TestProcessDatasetTask:
    """Tests for the process_dataset Celery task."""

    def test_task_updates_status_on_error(self, dataset):
        # Force an error by using invalid file path
        dataset.file_path = "/nonexistent/path.csv"
        dataset.save()

        with pytest.raises(Exception):
            process_dataset(str(dataset.id))

        dataset.refresh_from_db()
        assert dataset.status == Dataset.StatusChoices.ERROR
