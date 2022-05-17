# Generated by Django 4.0.4 on 2022-05-17 01:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Condominio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nro_vivienda', models.IntegerField(verbose_name='Nro de Viviendas')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
            ],
        ),
        migrations.CreateModel(
            name='Conserje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Espacio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('precio', models.PositiveIntegerField(blank=True, null=True)),
                ('aforo', models.PositiveIntegerField(max_length=3)),
                ('descripcion', models.TextField(max_length=200)),
                ('imagen', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Residente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vivienda', models.PositiveIntegerField(max_length=4)),
                ('rut', models.CharField(max_length=20)),
                ('telefono', models.PositiveIntegerField(max_length=9)),
                ('moroso', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PagoReserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.PositiveIntegerField()),
                ('fecha_pago', models.DateTimeField()),
                ('id_pago', models.CharField(max_length=100, null=True)),
                ('espacio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.espacio')),
                ('residente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.residente')),
            ],
        ),
        migrations.CreateModel(
            name='PagoGC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.PositiveIntegerField()),
                ('fecha_pago', models.DateTimeField(auto_now_add=True)),
                ('id_pago', models.CharField(max_length=100, null=True)),
                ('residente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.residente')),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conserje', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.conserje')),
            ],
        ),
        migrations.CreateModel(
            name='GastosComunes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.PositiveIntegerField()),
                ('fecha', models.DateField(auto_now_add=True)),
                ('condominio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.condominio')),
            ],
        ),
    ]