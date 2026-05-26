"""Conftest for analytics tests."""
import pytest

from apps.analytics.models import AnalysisSession


@pytest.fixture
def analysis_session(db, organization, user, dataset):
    """Create a test analysis session."""
    return AnalysisSession.objects.create(
        name="Test Analysis",
        dataset=dataset,
        organization=organization,
        created_by=user,
    )
