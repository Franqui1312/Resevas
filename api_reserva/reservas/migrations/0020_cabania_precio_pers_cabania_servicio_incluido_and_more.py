# Generated by Django 4.2.1 on 2023-12-29 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0019_remove_reserva_precio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cabania',
            name='precio_pers',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='cabania',
            name='servicio_incluido',
            field=models.CharField(default='ninguno', max_length=100),
        ),
        migrations.AddField(
            model_name='reserva',
            name='cant_personas',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='reserva',
            name='servicio',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='reservas.servicio'),
        ),
        migrations.AlterField(
            model_name='cabania',
            name='capacidad',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cabania',
            name='precio',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='dni',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='encargado',
            name='dni',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='seña',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='precio',
            field=models.FloatField(),
        ),
    ]
