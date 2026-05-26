"""ViewSets for dataset management including upload and metadata."""
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response

from .models import DataSource, Dataset
from .serializers import (
    DatasetSerializer,
    DatasetUploadSerializer,
    DatasetVersionSerializer,
    DataSourceSerializer,
)
from .tasks import process_dataset


class DatasetViewSet(viewsets.ModelViewSet):
    """CRUD operations for datasets with upload capability."""

    serializer_class = DatasetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Dataset.objects.filter(
            organization=self.request.user.last_active_organization
        ).select_related("uploaded_by").prefetch_related("columns")

    @action(detail=False, methods=["post"], parser_classes=[MultiPartParser, FormParser])
    def upload(self, request):
        """Upload a new dataset file."""
        serializer = DatasetUploadSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        file = serializer.validated_data["file"]
        dataset = Dataset.objects.create(
            name=serializer.validated_data.get("name", file.name),
            description=serializer.validated_data.get("description", ""),
            organization=request.user.last_active_organization,
            uploaded_by=request.user,
            file_name=file.name,
            file_size=file.size,
            file_type=file.name.split(".")[-1].lower(),
            file_path="",  # Set by storage service
            status=Dataset.StatusChoices.UPLOADING,
            tags=serializer.validated_data.get("tags", []),
        )

        # Trigger async processing
        process_dataset.delay(str(dataset.id))

        return Response(
            DatasetSerializer(dataset).data,
            status=status.HTTP_201_CREATED,
        )

    @action(detail=True, methods=["get"])
    def versions(self, request, pk=None):
        """List all versions of a dataset."""
        dataset = self.get_object()
        versions = dataset.versions.all()
        serializer = DatasetVersionSerializer(versions, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def preview(self, request, pk=None):
        """Get a preview of the dataset (first N rows)."""
        dataset = self.get_object()
        # Preview logic handled by service layer
        return Response({"dataset_id": str(dataset.id), "preview": [], "message": "Preview not yet implemented"})


class DataSourceViewSet(viewsets.ModelViewSet):
    """Manage external data source connections."""

    serializer_class = DataSourceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return DataSource.objects.filter(
            organization=self.request.user.last_active_organization
        )

    def perform_create(self, serializer):
        serializer.save(organization=self.request.user.last_active_organization)
