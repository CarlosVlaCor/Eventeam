from django import forms
from .models import Salon, Tags, SalonImages


class SalonForm(forms.ModelForm):

    class Meta:
        exclude = ['user']
        model = Salon
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre'
                }
            ),
            'ciudad': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ciudad'
                }
            ),
            'region': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Region'
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Direccion'
                }
            ),
            'alquiler': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Alquiler'
                }
            ),
            'region': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Region'
                }
            ),
            'rango': forms.Select(
                attrs={
                    'class': 'form-select form-select-m mb-3',
                    'placeholder': 'Rango'
                }
            )

        }


class ImageForm(forms.ModelForm):

    class Meta:
        model = SalonImages
        fields = ['image']