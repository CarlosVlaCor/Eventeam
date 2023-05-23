from django.contrib import admin

from .models import Tags, Salon, Espacio

# Register your models here.
admin.site.register(Salon)
admin.site.register(Tags)
admin.site.register(Espacio)