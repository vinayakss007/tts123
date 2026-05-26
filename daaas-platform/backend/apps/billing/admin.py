from django.contrib import admin

from .models import Invoice, Plan, Subscription, UsageRecord


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ("name", "tier", "price_monthly", "is_active")
    list_filter = ("tier", "is_active")


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("organization", "plan", "status", "billing_interval", "current_period_end")
    list_filter = ("status", "plan")


@admin.register(UsageRecord)
class UsageRecordAdmin(admin.ModelAdmin):
    list_display = ("organization", "metric", "quantity", "period_start")
    list_filter = ("metric",)


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ("organization", "amount", "status", "period_start", "period_end")
    list_filter = ("status",)
