from captcha.fields import ReCaptchaField
from django import forms
from django.contrib.auth import authenticate
from .models import User


class UserRegisterForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Contrasena',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contrasena'
            }
        )
    )
    captcha = ReCaptchaField()

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'region',
            'city',
            'phone'
        )


class LoginForm(forms.Form):
    email = forms.EmailField(
        label='email',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'email',
            }
        )
    )
    password = forms.CharField(
        label='Contrasena',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Contrasena'
            }
        )
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = self.cleaned_data['email']
        password = self.cleaned_data['password']
        if not authenticate(username=username, password=password):
            raise forms.ValidationError('Los datos del usuario no son correctos')

        return self.cleaned_data
