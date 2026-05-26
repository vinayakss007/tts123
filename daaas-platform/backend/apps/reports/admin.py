from django.contrib import admin

from .models import Report, ReportSection, ReportTemplate


@admin.register(ReportTemplate)
class ReportTemplateAdmin(admin.ModelAdmin):
    list_display = ("name", "is_system", "organization", "created_at")
    list_filter = ("is_system",)


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ("title", "organization", "status", "output_format", "created_at")
    list_filter = ("status", "output_format")
    search_fields = ("title",)


@admin.register(ReportSection)
class ReportSectionAdmin(admin.ModelAdmin):
    list_display = ("title", "report", "section_type", "order", "ai_generated")
