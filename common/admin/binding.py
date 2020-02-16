from django.contrib import admin

from ._base import BaseAdmin
from common.models import Binding


class BindingAdmin(BaseAdmin):
    list_display = BaseAdmin.list_display + ("flag",)
    search_fields = BaseAdmin.search_fields + ("flag", "subject",)


admin.site.register(Binding, BindingAdmin)


class BindingAdminInline(admin.TabularInline):
    model = Binding
