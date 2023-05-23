from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView, UpdateView

from .forms import SalonForm

from django.forms.models import inlineformset_factory

from .models import Salon


class ListaSalonesView(TemplateView):
    template_name = 'salones/lista-salones.html'


class SalonView(TemplateView):
    template_name = 'salones/salon-evento.html'


class RegistrarSalon(CreateView):
    template_name = 'salones/registrar-salon.html'
    model = Salon
    form_class = SalonForm
    success_url = reverse_lazy('salones_app:registrar-salon')


class UpdateSalon(UpdateView):
    template_name = 'salones/actualizar-salon.html'
    model = Salon
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('salones_app:update-salon', kwargs={'pk': self.get_object().id})

