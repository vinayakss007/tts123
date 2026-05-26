"""Tests for report models."""
import pytest

from apps.reports.models import Report


@pytest.mark.django_db
class TestReportModel:
    def test_create_report(self, report):
        assert report.status == Report.StatusChoices.DRAFT
        assert report.output_format == "html"

    def test_report_str(self, report):
        assert str(report) == "Test Report"
