"""ViewSets for report generation and management."""
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Report, ReportTemplate
from .serializers import (
    GenerateReportSerializer,
    ReportSerializer,
    ReportTemplateSerializer,
)
from .tasks import generate_report


class ReportViewSet(viewsets.ModelViewSet):
    """CRUD operations for reports with generation action."""

    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Report.objects.filter(
            organization=self.request.user.last_active_organization
        ).prefetch_related("sections")

    def perform_create(self, serializer):
        serializer.save(
            organization=self.request.user.last_active_organization,
            created_by=self.request.user,
        )

    @action(detail=False, methods=["post"])
    def generate(self, request):
        """Generate an AI-powered report."""
        serializer = GenerateReportSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        report = Report.objects.create(
            title=serializer.validated_data["title"],
            organization=request.user.last_active_organization,
            created_by=request.user,
            dataset_id=serializer.validated_data["dataset_id"],
            analysis_session_id=serializer.validated_data.get("analysis_session_id"),
            template_id=serializer.validated_data.get("template_id"),
            output_format=serializer.validated_data["output_format"],
            status=Report.StatusChoices.GENERATING,
        )

        generate_report.delay(
            str(report.id),
            custom_instructions=serializer.validated_data.get("custom_instructions", ""),
        )

        return Response(
            ReportSerializer(report).data,
            status=status.HTTP_202_ACCEPTED,
        )


class ReportTemplateViewSet(viewsets.ModelViewSet):
    """Manage report templates."""

    serializer_class = ReportTemplateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ReportTemplate.objects.filter(
            models.Q(is_system=True)
            | models.Q(organization=self.request.user.last_active_organization)
        )
