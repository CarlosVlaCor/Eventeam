# Generated by Django 4.2.1 on 2023-05-24 05:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('salones', '0009_alter_salonimages_salon'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReservaSalon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inv_aprox', models.IntegerField(choices=[(1, '0-100'), (2, '100-200'), (3, '200 o más')], verbose_name='Invitados aproximados')),
                ('fecha', models.DateField(verbose_name='fecha')),
                ('salon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salones.salon')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]