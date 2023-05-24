from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import TemplateView, FormView, CreateView, UpdateView, ListView, DeleteView, DetailView
from .forms import SalonForm, ImageForm, ReservarForm
from django.template.loader import get_template
from django.forms.models import inlineformset_factory
from django.conf import settings
from .models import Salon, SalonImages, ReservaSalon
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMessage

class ListaSalonesView(ListView):
    template_name = 'salones/lista-salones.html'
    ordering = 'id'
    model = Salon
    paginate_by = 5
    context_object_name = 'lista'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        print(palabra_clave)
        if palabra_clave == '':
            queryset = Salon.objects.all()
        else:
            queryset = Salon.objects.filter(
                nombre=palabra_clave
            )
        ordering = self.get_ordering()
        if ordering:
            if isinstance(ordering, str):
                ordering = (ordering,)
            queryset = queryset.order_by(*ordering)
        return queryset


class SalonView(DetailView):
    template_name = 'salones/salon-evento.html'
    model = Salon

    def get_context_data(self, **kwargs):
        contexto = super(SalonView, self).get_context_data(**kwargs)
        contexto['reserva'] = ReservarForm
        return contexto


class ReservarSalonView(View):

    def post(self, request, *args, **kwargs):
        form = ReservarForm(request.POST)
        id_salon = self.kwargs['pk']
        salon = Salon.objects.get(id=id_salon)
        if form.is_valid():
            fecha = form.cleaned_data['fecha']
            inv_aprox = form.cleaned_data['inv_aprox']
            ReservaSalon.objects.create(
                fecha=fecha,
                inv_aprox=inv_aprox,
                user=request.user,
                salon=salon

            )
            ctx = {
                'nombre': request.user.first_name + ' ' + request.user.last_name,
                'telefono': request.user.phone,
                'email': request.user.email,
                'fecha': fecha,
                'inv_aprox': inv_aprox
            }
            message = get_template('salones/notificacion-reserva.html').render(ctx)
            msg = EmailMessage(
                'Nueva reserva',
                message,
                settings.EMAIL_HOST_USER,
                [salon.user.email],
            )
            msg.content_subtype = "html"  # Main content is now text/html
            msg.send()

        return HttpResponseRedirect(
            reverse(
                'salones_app:lista-eventos',
            )
        )


class RegistrarSalon(FormView):
    template_name = 'salones/registrar-salon.html'
    model = Salon
    form_class = SalonForm
    success_url = reverse_lazy('salones_app:mis-salones')

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
        return reverse_lazy('salones_app:salon-evento', kwargs={'pk': self.get_object().id})


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


class EliminarImagen(DeleteView):
    model = SalonImages

    def get_success_url(self, **kwargs):
        id_salon = self.kwargs['pk_alt']
        return reverse('salones_app:update-salon', kwargs={'pk': id_salon})


class MisSalonesView(ListView):
    template_name = 'salones/mis-salones.html'
    model = Salon
    paginate_by = 5
    fields = '__all__'
    context_object_name = 'lista'
    ordering = 'id'

    def get_queryset(self):
        queryset = Salon.objects.filter(
            user=self.request.user
        )
        ordering = self.get_ordering()
        if ordering:
            if isinstance(ordering, str):
                ordering = (ordering,)
            queryset = queryset.order_by(*ordering)
        return queryset


class DeleteSalon(DeleteView):
    model = Salon
    success_url = reverse_lazy('salones_app:mis-salones')


class ReservasPropietarioListView(ListView):
    model = ReservaSalon
    ordering = 'created_at'
    template_name = 'salones/lista-reservas.html'
    paginate_by = 10
    context_object_name = 'lista'

    def get_queryset(self):
        primer_queryset = Salon.objects.filter(user=self.request.user)
        queryset = ReservaSalon.objects.filter(salon__in=primer_queryset)
        ordering = self.get_ordering()
        if ordering:
            if isinstance(ordering, str):
                ordering = (ordering,)
            queryset = queryset.order_by(*ordering)
        return queryset
