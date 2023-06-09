# Generated by Django 4.2.1 on 2023-05-23 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salones', '0005_salon_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Espacio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre del espacio')),
            ],
            options={
                'verbose_name': 'Espacio',
                'verbose_name_plural': 'Espacio',
            },
        ),
        migrations.RemoveField(
            model_name='servicios',
            name='salon',
        ),
        migrations.DeleteModel(
            name='EspacioSalon',
        ),
        migrations.DeleteModel(
            name='Servicios',
        ),
        migrations.AddField(
            model_name='salon',
            name='espacios',
            field=models.ManyToManyField(to='salones.espacio'),
        ),
    ]
