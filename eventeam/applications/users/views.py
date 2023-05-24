from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import TemplateView, FormView
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import UserRegisterForm, LoginForm
from .models import User


# Create your views here.
class RegistrarUsuario(TemplateView):
    template_name = 'users/registrar.html'


class UserRegisterView(FormView):
    template_name = 'users/registrar.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('users_app:user-login')

    def form_valid(self, form):
        #
        User.objects.create_user(
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            region=form.cleaned_data['region'],
            city=form.cleaned_data['city'],
            phone=form.cleaned_data['phone']
        )
        # enviar el codigo al email del user
        return super(UserRegisterView, self).form_valid(form)

class LoginUser(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home_app:inicio')

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data['email'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)


class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse('users_app:user-login')
        )


class PropietarioRegister(FormView):
    template_name = 'users/registrar-propietario.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('users_app:user-login')

    def form_valid(self, form):
        User.objects.create_propietario(
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            region=form.cleaned_data['region'],
            city=form.cleaned_data['city'],
            phone=form.cleaned_data['phone']
        )

        return super(PropietarioRegister, self).form_valid(form)


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/subject/password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."

    success_url = reverse_lazy('home_app:inicio')


