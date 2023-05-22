from django.shortcuts import render
from django.views.generic import TemplateView


class ListaSalonesView(TemplateView):
    template_name = 'salones/lista-salones.html'


class SalonView(TemplateView):
    template_name = 'salones/salon-evento.html'
