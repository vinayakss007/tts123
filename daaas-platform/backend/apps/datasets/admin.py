from django.contrib import admin

from .models import DataColumn, DataSource, Dataset, DatasetVersion


@admin.register(Dataset)
class DatasetAdmin(admin.ModelAdmin):
    list_display = ("name", "organization", "file_type", "row_count", "status", "created_at")
    list_filter = ("status", "file_type", "created_at")
    search_fields = ("name", "description")
    readonly_fields = ("id", "created_at", "updated_at")


@admin.register(DatasetVersion)
class DatasetVersionAdmin(admin.ModelAdmin):
    list_display = ("dataset", "version_number", "created_at")
    list_filter = ("created_at",)


@admin.register(DataColumn)
class DataColumnAdmin(admin.ModelAdmin):
    list_display = ("name", "dataset", "data_type", "nullable", "null_count")
    list_filter = ("data_type", "nullable")


@admin.register(DataSource)
class DataSourceAdmin(admin.ModelAdmin):
    list_display = ("name", "organization", "source_type", "is_active", "last_synced_at")
    list_filter = ("source_type", "is_active")
