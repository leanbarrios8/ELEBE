# Generated by Django 5.0.6 on 2024-07-15 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudios',
            name='duracion',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='estudios',
            name='nota',
            field=models.CharField(max_length=20),
        ),
    ]
