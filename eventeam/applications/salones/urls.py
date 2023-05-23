from django.urls import path

from . import views


app_name = "salones_app"


urlpatterns = [
    path(
        'salones-de-eventos/',
        views.ListaSalonesView.as_view(),
        name='lista-eventos'),
    path(
        'salon-evento/',
        views.SalonView.as_view(),
        name='salon-evento'),
    path(
        'registrar-salon/',
        views.RegistrarSalon.as_view(),
        name='registrar-salon'),
    path(
        'update-salon/<pk>/',
        views.UpdateSalon.as_view(),
        name='update-salon'),

]