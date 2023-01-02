# Generated by Django 4.1.2 on 2022-10-18 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0002_alter_empleado_options_empleado_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilidad', models.CharField(max_length=50, verbose_name='Habilidad')),
            ],
            options={
                'verbose_name': 'Habilidad',
                'verbose_name_plural': 'Habilidades del empleado',
            },
        ),
    ]
