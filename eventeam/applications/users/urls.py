from django.urls import path

from . import views


app_name = "salones_app"


urlpatterns = [
    path(
        'registrar/',
        views.RegistrarUsuario.as_view(),
        name='registrar'),

]