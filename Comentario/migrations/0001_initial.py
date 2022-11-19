# Generated by Django 4.1.3 on 2022-11-19 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(help_text='Ingrese el estado del Paciente', max_length=20)),
                ('comentario', models.CharField(help_text='Ingrese el comentario', max_length=300)),
                ('fecha_comentario', models.DateTimeField()),
            ],
        ),
    ]
