"""Report generation service using AI gateway."""
from typing import Any

from .models import Report, ReportSection


class ReportGenerationService:
    """Service for generating AI-powered reports."""

    def generate(self, report: Report, custom_instructions: str = "") -> dict[str, Any]:
        """Generate a full report using the AI gateway.

        Steps:
        1. Gather dataset statistics and analysis results
        2. Build prompt from template or default structure
        3. Call AI gateway for each section
        4. Compile sections into final report
        5. Export in requested format

        Returns:
            Dictionary with file_path and tokens_used.
        """
        context = self._gather_context(report)
        sections = self._determine_sections(report)
        total_tokens = 0

        for idx, section_config in enumerate(sections):
            prompt = self._build_section_prompt(section_config, context, custom_instructions)
            content, tokens = self._generate_section_content(prompt)
            total_tokens += tokens

            ReportSection.objects.create(
                report=report,
                title=section_config["title"],
                content=content,
                section_type=section_config.get("type", "text"),
                order=idx,
                ai_generated=True,
            )

        file_path = self._export_report(report)

        return {
            "file_path": file_path,
            "tokens_used": total_tokens,
        }

    def _gather_context(self, report: Report) -> dict:
        """Gather relevant data context for report generation."""
        context = {
            "dataset_name": report.dataset.name if report.dataset else "",
            "row_count": report.dataset.row_count if report.dataset else 0,
            "column_count": report.dataset.column_count if report.dataset else 0,
        }

        if report.analysis_session:
            context["analysis_results"] = report.analysis_session.results_summary

        return context

    def _determine_sections(self, report: Report) -> list[dict]:
        """Determine report section structure from template or defaults."""
        if report.template and report.template.structure:
            return report.template.structure

        # Default report structure
        return [
            {"title": "Executive Summary", "type": "text"},
            {"title": "Data Overview", "type": "text"},
            {"title": "Key Findings", "type": "text"},
            {"title": "Statistical Analysis", "type": "text"},
            {"title": "Visualizations", "type": "chart"},
            {"title": "Recommendations", "type": "text"},
        ]

    def _build_section_prompt(self, section_config: dict, context: dict, custom_instructions: str) -> str:
        """Build AI prompt for generating a report section."""
        raise NotImplementedError("Section prompt building not yet implemented")

    def _generate_section_content(self, prompt: str) -> tuple[str, int]:
        """Call AI gateway to generate section content."""
        raise NotImplementedError("AI content generation not yet implemented")

    def _export_report(self, report: Report) -> str:
        """Export the report to the requested format and save to storage."""
        raise NotImplementedError("Report export not yet implemented")
