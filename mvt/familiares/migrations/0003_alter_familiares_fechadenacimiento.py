# Generated by Django 4.0.5 on 2022-07-28 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familiares', '0002_familiares_apellido_familiares_nombre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familiares',
            name='fechaDeNacimiento',
            field=models.DateField(),
        ),
    ]