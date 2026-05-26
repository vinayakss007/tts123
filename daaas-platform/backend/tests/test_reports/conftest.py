"""Conftest for reports tests."""
import pytest

from apps.reports.models import Report


@pytest.fixture
def report(db, organization, user, dataset):
    """Create a test report."""
    return Report.objects.create(
        title="Test Report",
        organization=organization,
        created_by=user,
        dataset=dataset,
        output_format=Report.FormatChoices.HTML,
    )
