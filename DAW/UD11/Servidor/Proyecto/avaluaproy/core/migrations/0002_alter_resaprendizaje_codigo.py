# Generated by Django 4.2 on 2023-11-17 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resaprendizaje',
            name='codigo',
            field=models.CharField(max_length=10, verbose_name='Código'),
        ),
    ]
