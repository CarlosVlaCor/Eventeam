from django import forms
from .models import Salon, Tags, SalonImages, ReservaSalon


class SalonForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label
    class Meta:
        exclude = ['user']
        model = Salon
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }


class ImageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label

    class Meta:
        model = SalonImages
        fields = ['image']


class ReservarForm(forms.ModelForm):
    fecha = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}))

    class Meta:
        model = ReservaSalon
        fields = ['fecha', 'inv_aprox']
        widgets = {
            'inv_aprox': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            )

        }

