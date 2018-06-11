from django.contrib import admin, messages

from rest_framework_api_key.helpers import generate_key
from rest_framework_api_key.models import APIKey


@admin.register(APIKey)
class ApiKeyAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created", "modified")

    fieldsets = (
        ("Required Information", {"fields": ("name",)}),
        ("Additional Information", {"fields": ("key_message",)}),
    )
    readonly_fields = ("key_message",)

    search_fields = ("id", "name")

    def key_message(self, obj):
        if obj.key:
            return "Hidden"
        return "The API Key will be generated once you click save."

    def save_model(self, request, obj, form, change):
        if not obj.key:
            obj.key = generate_key()
            messages.add_message(
                request,
                messages.WARNING,
                (
                    "The API Key for %s is %s. Please note it since you will not be able to see it again."
                    % (obj.name, obj.key)
                ),
            )
        obj.save()
