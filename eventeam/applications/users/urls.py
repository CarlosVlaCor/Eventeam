from django.urls import path

from . import views


app_name = "users_app"


urlpatterns = [
    path(
        'registrar/',
        views.UserRegisterView.as_view(),
        name='user-register'),
    path(
        'login/',
        views.LoginUser.as_view(),
        name='user-login'),
    path(
        'logout/',
        views.LogoutView.as_view(),
        name='user-logout'),
    path(
        'registrar-propietario/',
        views.PropietarioRegister.as_view(),
        name='registrar-propietario'),

]