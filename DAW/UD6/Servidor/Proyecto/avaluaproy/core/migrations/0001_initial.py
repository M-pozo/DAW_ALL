# Generated by Django 4.2 on 2023-11-17 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10, unique=True, verbose_name='Código')),
                ('nombre', models.CharField(max_length=256, unique=True, verbose_name='Nombre')),
            ],
        ),
        migrations.CreateModel(
            name='ResAprendizaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10, unique=True, verbose_name='Código')),
                ('descirpcion', models.TextField(verbose_name='Descripción')),
                ('modulo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.modulo', verbose_name='Módulo')),
            ],
        ),
        migrations.CreateModel(
            name='CritEvaluacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=4, verbose_name='Código')),
                ('descirpcion', models.TextField(verbose_name='Descripción')),
                ('minimo', models.CharField(max_length=10, unique=True, verbose_name='Código')),
                ('resultado_aprendizaje', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.resaprendizaje', verbose_name='Código')),
            ],
        ),
    ]
