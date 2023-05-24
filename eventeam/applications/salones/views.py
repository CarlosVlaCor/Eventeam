from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import TemplateView, FormView, CreateView, UpdateView, ListView, DeleteView, DetailView

from .forms import SalonForm, ImageForm

from django.forms.models import inlineformset_factory

from .models import Salon, SalonImages


class ListaSalonesView(ListView):
    template_name = 'salones/lista-salones.html'
    model = Salon
    paginate_by = 10
    context_object_name = 'lista'


class SalonView(DetailView):
    template_name = 'salones/salon-evento.html'
    model = Salon


class RegistrarSalon(FormView):
    template_name = 'salones/registrar-salon.html'
    model = Salon
    form_class = SalonForm
    success_url = reverse_lazy('salones_app:registrar-salon')

    def form_valid(self, form):
        tags = form.cleaned_data.pop('tags')
        espacios = form.cleaned_data.pop('espacios')
        salon = Salon.objects.create(
            **form.cleaned_data,
            user=self.request.user
        )
        salon.tags.set(tags)
        salon.espacios.set(espacios)
        return super(RegistrarSalon, self).form_valid(form)


class UpdateSalon(UpdateView):
    template_name = 'salones/actualizar-salon.html'
    model = Salon
    form_class = SalonForm
    success_url = reverse_lazy('salones_app:update-salon')

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


class MisSalonesView(ListView):
    template_name = 'salones/mis-salones.html'
    model = Salon
    fields = '__all__'
    context_object_name = 'salones'

    def get_queryset(self):
        queryset = Salon.objects.filter(
            user=self.request.user
        )
        return queryset


class DeleteSalon(DeleteView):
    model = Salon
    success_url = reverse_lazy('salones_app:mis-salones')
