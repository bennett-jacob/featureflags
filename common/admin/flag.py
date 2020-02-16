from django.contrib import admin

from ._base import BaseAdmin
from .binding import BindingAdminInline
from common.models import Flag


class FlagAdmin(BaseAdmin):
    list_display = BaseAdmin.list_display + ("name",)
    search_fields = BaseAdmin.search_fields + ("name",)
    inlines = (BindingAdminInline,)


admin.site.register(Flag, FlagAdmin)
