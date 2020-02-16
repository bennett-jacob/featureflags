from django.urls import path

from api_v1 import views


urlpatterns = [
    path("/flags", views.flag_list_view, name="flag_list"),
    path("/flags/<str:name>", views.flag_detail_view, name="flag_detail"),
    path(
        "/flags/<str:name>/bindings",
        views.flag_binding_list_view,
        name="flag_binding_list",
    ),
]
