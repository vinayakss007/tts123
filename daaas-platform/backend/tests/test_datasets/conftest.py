"""Conftest for datasets tests."""
import pytest

from apps.datasets.models import Dataset


@pytest.fixture
def dataset(db, organization, user):
    """Create a test dataset."""
    return Dataset.objects.create(
        name="Test Dataset",
        organization=organization,
        uploaded_by=user,
        file_name="test.csv",
        file_size=1024,
        file_type="csv",
        file_path="/test/path/test.csv",
        status=Dataset.StatusChoices.READY,
        row_count=100,
        column_count=5,
    )
