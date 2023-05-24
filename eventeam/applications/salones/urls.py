from django.urls import path

from . import views


app_name = "salones_app"


urlpatterns = [
    path(
        'salones-de-eventos/',
        views.ListaSalonesView.as_view(),
        name='lista-eventos'),
    path(
        'salon-evento/<pk>/',
        views.SalonView.as_view(),
        name='salon-evento'),
    path(
        'reservar-salon/<pk>/',
        views.ReservarSalonView.as_view(),
        name='reservar'),
    path(
        'registrar-salon/',
        views.RegistrarSalon.as_view(),
        name='registrar-salon'),
    path(
        'update-salon/<pk>/',
        views.UpdateSalon.as_view(),
        name='update-salon'),
    path(
        'upload-image/<pk>/',
        views.UploadImage.as_view(),
        name='upload-image'),
    path(
        'update-salon/<pk_alt>/delete-image/<pk>/',
        views.EliminarImagen.as_view(),
        name='delete-image'),
    path(
        'propietarios/mis-salones/',
        views.MisSalonesView.as_view(),
        name='mis-salones'),
    path(
        'propietarios/mis-salones/<pk>',
        views.DeleteSalon.as_view(),
        name='delete-salon'),
    path(
        'propietarios/lista-reservas/',
        views.ReservasPropietarioListView.as_view(),
        name='lista-reservas'),

]