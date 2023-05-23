from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import TemplateView, FormView, CreateView, UpdateView

from .forms import SalonForm, ImageForm

from django.forms.models import inlineformset_factory

from .models import Salon, SalonImages


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

    def get_context_data(self, **kwargs):
        context = super(UpdateSalon, self).get_context_data(**kwargs)
        context['form_image'] = ImageForm
        return context

    def get_success_url(self):
        return reverse_lazy('salones_app:update-salon', kwargs={'pk': self.get_object().id})

class UploadImage(View):

    def post(self, request, *args, **kwargs):
        id_salon = self.kwargs['pk']
        image = request.FILES['image']
        salon = Salon.objects.get(id=id_salon)
        SalonImages.objects.create(
            image=image,
            salon=salon
        )
        return HttpResponseRedirect(
            reverse(
                'salones_app:update-salon', kwargs={'pk': id_salon},
            )
        )

