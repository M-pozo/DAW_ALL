# Generated by Django 4.2 on 2023-11-08 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='nombre',
            field=models.CharField(max_length=256, verbose_name='Nombre'),
        ),
    ]
