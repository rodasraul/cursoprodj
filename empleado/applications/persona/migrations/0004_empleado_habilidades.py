# Generated by Django 4.1.2 on 2022-10-18 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0003_habilidades'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='habilidades',
            field=models.ManyToManyField(to='persona.habilidades'),
        ),
    ]
