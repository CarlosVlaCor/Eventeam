# Generated by Django 4.2.1 on 2023-05-23 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salones', '0004_alter_espaciosalon_nombre_alter_servicios_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='salon',
            name='description',
            field=models.CharField(default='a', max_length=200, verbose_name='Descripcion'),
            preserve_default=False,
        ),
    ]
