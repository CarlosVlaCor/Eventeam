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

]