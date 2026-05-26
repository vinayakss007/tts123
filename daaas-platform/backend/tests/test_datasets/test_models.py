"""Tests for dataset models."""
import pytest

from apps.datasets.models import DataColumn, Dataset


@pytest.mark.django_db
class TestDatasetModel:
    """Tests for the Dataset model."""

    def test_create_dataset(self, dataset):
        assert dataset.name == "Test Dataset"
        assert dataset.status == Dataset.StatusChoices.READY
        assert dataset.row_count == 100

    def test_dataset_str(self, dataset):
        assert str(dataset) == "Test Dataset (csv)"


@pytest.mark.django_db
class TestDataColumnModel:
    """Tests for the DataColumn model."""

    def test_create_column(self, dataset):
        column = DataColumn.objects.create(
            dataset=dataset,
            name="age",
            data_type=DataColumn.DataTypeChoices.INTEGER,
            position=0,
        )
        assert column.name == "age"
        assert column.data_type == "integer"
