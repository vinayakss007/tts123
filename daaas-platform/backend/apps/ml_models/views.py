"""ViewSets for ML model management, training, and prediction."""
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import MLModel, ModelVersion, Prediction, TrainingRun
from .serializers import (
    MLModelSerializer,
    ModelVersionSerializer,
    PredictionRequestSerializer,
    PredictionSerializer,
    TrainModelSerializer,
    TrainingRunSerializer,
)
from .tasks import train_model


class MLModelViewSet(viewsets.ModelViewSet):
    """CRUD operations for ML models with train and predict actions."""

    serializer_class = MLModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return MLModel.objects.filter(
            organization=self.request.user.last_active_organization
        ).prefetch_related("versions", "training_runs")

    def perform_create(self, serializer):
        serializer.save(
            organization=self.request.user.last_active_organization,
            created_by=self.request.user,
        )

    @action(detail=True, methods=["post"])
    def train(self, request, pk=None):
        """Trigger model training."""
        model = self.get_object()
        serializer = TrainModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        training_run = TrainingRun.objects.create(
            model=model,
            hyperparameters=serializer.validated_data.get("hyperparameters", {}),
        )

        model.status = MLModel.StatusChoices.TRAINING
        model.save(update_fields=["status"])

        train_model.delay(str(training_run.id))

        return Response(
            TrainingRunSerializer(training_run).data,
            status=status.HTTP_202_ACCEPTED,
        )

    @action(detail=True, methods=["post"])
    def predict(self, request, pk=None):
        """Run predictions using the active model version."""
        model = self.get_object()
        serializer = PredictionRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        active_version = model.versions.filter(is_active=True).first()
        if not active_version:
            return Response(
                {"error": "No active model version found. Train the model first."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        predictions = []
        for input_data in serializer.validated_data["input_data"]:
            prediction = Prediction.objects.create(
                model=model,
                model_version=active_version,
                input_data=input_data,
                requested_by=request.user,
            )
            predictions.append(prediction)

        return Response(
            PredictionSerializer(predictions, many=True).data,
            status=status.HTTP_202_ACCEPTED,
        )

    @action(detail=True, methods=["get"])
    def versions(self, request, pk=None):
        """List all versions of a model."""
        model = self.get_object()
        versions = model.versions.all()
        return Response(ModelVersionSerializer(versions, many=True).data)

    @action(detail=True, methods=["get"])
    def training_history(self, request, pk=None):
        """Get training history for a model."""
        model = self.get_object()
        runs = model.training_runs.all()
        return Response(TrainingRunSerializer(runs, many=True).data)
