# Generated by Django 4.1.2 on 2022-10-18 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empleado',
            options={'ordering': ['last_name', '-first_name'], 'verbose_name': 'Trabajadores de la empresa', 'verbose_name_plural': 'Colaboradores'},
        ),
        migrations.AddField(
            model_name='empleado',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='empleado'),
        ),
        migrations.AlterUniqueTogether(
            name='empleado',
            unique_together={('last_name', 'first_name')},
        ),
    ]