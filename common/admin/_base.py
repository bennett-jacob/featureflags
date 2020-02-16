from django.contrib import admin


class BaseAdmin(admin.ModelAdmin):
    readonly_fields = (
        "id",
        "created_at",
        "updated_at",
    )
    search_fields = ("id",)
    list_filter = ("created_at",)
