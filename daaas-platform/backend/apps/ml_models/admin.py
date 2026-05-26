from django.contrib import admin

from .models import MLModel, ModelVersion, Prediction, TrainingRun


@admin.register(MLModel)
class MLModelAdmin(admin.ModelAdmin):
    list_display = ("name", "model_type", "task_type", "organization", "status", "created_at")
    list_filter = ("model_type", "task_type", "status")
    search_fields = ("name",)


@admin.register(TrainingRun)
class TrainingRunAdmin(admin.ModelAdmin):
    list_display = ("model", "status", "duration_seconds", "started_at")
    list_filter = ("status",)


@admin.register(ModelVersion)
class ModelVersionAdmin(admin.ModelAdmin):
    list_display = ("model", "version_number", "accuracy", "is_active", "created_at")
    list_filter = ("is_active",)


@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):
    list_display = ("model", "model_version", "status", "created_at")
    list_filter = ("status",)
