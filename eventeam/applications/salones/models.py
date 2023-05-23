from django.db import models


class Tags(models.Model):
    nombre = models.CharField(verbose_name='Nombre del tag', max_length=100)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.nombre


class Espacio(models.Model):
    nombre = models.CharField(verbose_name='Nombre del espacio', max_length=100)

    class Meta:
        verbose_name = 'Espacio'
        verbose_name_plural = 'Espacio'

    def __str__(self):
        return self.nombre


class Salon(models.Model):
    class Rango(models.IntegerChoices):
        DIEZ_CINCUENTA = (1, 'De 10 a 50')
        CINCUENTA_CIEN = (2, 'De 50 a 100')
        CIEN_QUINIENTOS = (3, 'De 100 a 500')
        QUINIENTOS_MIL = (4, 'De 500 a 1000')
        MAS = (5, 'Mas de 1000')

    nombre = models.CharField(verbose_name='Nombre del salon', max_length=50, unique=True)
    ciudad = models.CharField(verbose_name='Ciudad', max_length=50)
    region = models.CharField(verbose_name='Region', max_length=100)
    direccion = models.CharField(verbose_name='Direccion', max_length=100)
    description = models.CharField(verbose_name='Descripcion', max_length=200)
    alquiler = models.DecimalField(verbose_name='Alquiler', decimal_places=3, max_digits=7)
    rango = models.IntegerField(verbose_name='Rango', choices=Rango.choices)
    tags = models.ManyToManyField(Tags)
    espacios = models.ManyToManyField(Espacio)

    class Meta:
        verbose_name = 'Salon'
        verbose_name_plural = 'Salones'

    def __str__(self):
        return self.nombre


class SalonImages(models.Model):
    image = models.ImageField(blank=False, null=False, upload_to='salones/')
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Imagen del salon'
        verbose_name_plural = 'Imagenes del salon'

    def __str__(self):
        return 'imagen del salon %s' % self.salon.name
