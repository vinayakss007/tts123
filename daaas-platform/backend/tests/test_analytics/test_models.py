"""Tests for analytics models."""
import pytest

from apps.analytics.models import AnalysisSession, AnalysisStep


@pytest.mark.django_db
class TestAnalysisSession:
    def test_create_session(self, analysis_session):
        assert analysis_session.status == AnalysisSession.StatusChoices.DRAFT

    def test_add_step(self, analysis_session):
        step = AnalysisStep.objects.create(
            session=analysis_session,
            step_type=AnalysisStep.StepTypeChoices.DESCRIPTIVE_STATS,
            order=0,
        )
        assert step.status == AnalysisStep.StatusChoices.PENDING
