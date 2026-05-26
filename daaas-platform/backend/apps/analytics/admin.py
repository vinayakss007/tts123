from django.contrib import admin

from .models import AnalysisSession, AnalysisStep, CleaningOperation, Visualization


@admin.register(AnalysisSession)
class AnalysisSessionAdmin(admin.ModelAdmin):
    list_display = ("name", "dataset", "created_by", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("name",)


@admin.register(AnalysisStep)
class AnalysisStepAdmin(admin.ModelAdmin):
    list_display = ("session", "step_type", "order", "status", "created_at")
    list_filter = ("step_type", "status")


@admin.register(Visualization)
class VisualizationAdmin(admin.ModelAdmin):
    list_display = ("title", "chart_type", "session", "created_at")
    list_filter = ("chart_type",)


@admin.register(CleaningOperation)
class CleaningOperationAdmin(admin.ModelAdmin):
    list_display = ("operation_type", "dataset", "status", "created_at")
    list_filter = ("operation_type", "status")
