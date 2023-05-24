from django.urls import path

from . import views
from .views import ResetPasswordView
from django.contrib.auth import views as auth_views
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
    path(
        'password-reset/',
         ResetPasswordView.as_view(),
        name='password_reset'),

]