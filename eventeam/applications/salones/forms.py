from django import forms
from .models import Salon, Tags


class SalonForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tags.objects.all(),
    )

    class Meta:
        fields = '__all__'
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
