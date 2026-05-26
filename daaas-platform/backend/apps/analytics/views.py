"""ViewSets for analytics operations."""
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import AnalysisSession, AnalysisStep, CleaningOperation, Visualization
from .serializers import (
    AnalysisSessionSerializer,
    AnalysisStepSerializer,
    CleaningOperationSerializer,
    VisualizationSerializer,
)
from .tasks import run_analysis_step


class AnalysisSessionViewSet(viewsets.ModelViewSet):
    """CRUD and execution for analysis sessions."""

    serializer_class = AnalysisSessionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return AnalysisSession.objects.filter(
            organization=self.request.user.last_active_organization
        ).prefetch_related("steps", "visualizations")

    def perform_create(self, serializer):
        serializer.save(
            organization=self.request.user.last_active_organization,
            created_by=self.request.user,
        )

    @action(detail=True, methods=["post"])
    def run(self, request, pk=None):
        """Execute all pending steps in the analysis session."""
        session = self.get_object()
        session.status = AnalysisSession.StatusChoices.RUNNING
        session.save(update_fields=["status"])

        for step in session.steps.filter(status=AnalysisStep.StatusChoices.PENDING):
            run_analysis_step.delay(str(step.id))

        return Response({"status": "running", "message": "Analysis execution started"})

    @action(detail=True, methods=["post"])
    def add_step(self, request, pk=None):
        """Add a new analysis step to the session."""
        session = self.get_object()
        serializer = AnalysisStepSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(session=session, order=session.steps.count())
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class VisualizationViewSet(viewsets.ModelViewSet):
    """CRUD for visualizations."""

    serializer_class = VisualizationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Visualization.objects.filter(
            session__organization=self.request.user.last_active_organization
        )


class CleaningOperationViewSet(viewsets.ModelViewSet):
    """Apply and manage data cleaning operations."""

    serializer_class = CleaningOperationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CleaningOperation.objects.filter(
            dataset__organization=self.request.user.last_active_organization
        )

    def perform_create(self, serializer):
        serializer.save(applied_by=self.request.user)

    @action(detail=True, methods=["post"])
    def revert(self, request, pk=None):
        """Revert a cleaning operation."""
        operation = self.get_object()
        operation.status = CleaningOperation.StatusChoices.REVERTED
        operation.save(update_fields=["status"])
        return Response({"status": "reverted"})
