# Generated by Django 4.2.1 on 2023-08-30 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0014_alter_encargado_dni'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encargado',
            name='dni',
            field=models.IntegerField(max_length=8),
        ),
    ]
