# Generated by Django 5.1 on 2024-08-28 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sucursales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_sucursal', models.CharField(max_length=100)),
                ('direccion_sucursal', models.CharField(max_length=100)),
            ],
        ),
    ]
