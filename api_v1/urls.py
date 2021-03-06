from django.urls import path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from . import views

schema_view = get_schema_view(
    openapi.Info(title="Feature Flags API", default_version="v1",), public=True,
)

urlpatterns = [
    re_path(
        r"^/swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^/swagger$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^/redoc$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
    # bindings
    path("/bindings", views.binding_list_view, name="binding_list"),
    path("/bindings/<str:pk>", views.binding_detail_view, name="binding_detail"),
    # flags
    path("/flags", views.flag_list_view, name="flag_list"),
    path("/flags/<str:name>", views.flag_detail_view, name="flag_detail"),
    path(
        "/flags/<str:name>/bindings",
        views.flag_binding_list_view,
        name="flag_binding_list",
    ),
    path(
        "/flags/<str:name>/bindings/<str:subject>",
        views.flag_binding_detail_view,
        name="flag_binding_detail",
    ),
]
