# Generated by Django 4.1.3 on 2022-11-19 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingreso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_ingreso', models.DateField(blank=True, help_text='Ingrese la fecha de ingreso')),
                ('hora', models.DateTimeField(blank=True, help_text='Ingrese la hora de ingreso')),
                ('cant_sintomas', models.PositiveIntegerField(help_text='Ingrese la cantidad de sintomas que presenta el paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexo_biologico', models.CharField(help_text='Ingrese su sexo biologico', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Patologia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_patologia', models.CharField(help_text='Ingrese el nombre de la patologia', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sintomas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_sintoma', models.CharField(help_text='Ingrese el nombre del sintoma', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SintomasPaciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion_sintoma', models.CharField(help_text='Ingrese la descripcion del sintoma', max_length=50)),
            ],
            options={
                'verbose_name': 'Sintomas_Paciente',
            },
        ),
    ]
