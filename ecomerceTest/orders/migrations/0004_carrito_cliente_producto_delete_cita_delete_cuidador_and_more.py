# Generated by Django 4.2.1 on 2023-06-15 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_cita_cuidador_paciente_delete_ejemplo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carrito_cliente', models.TextField(max_length=100)),
                ('carrito_producto', models.TextField(max_length=100)),
                ('precio', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.IntegerField(unique=True)),
                ('name_cliente', models.TextField(unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('tel', models.IntegerField()),
                ('direccion', models.TextField(max_length=100)),
                ('Barrio', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_producto', models.TextField(null=True)),
                ('precio_compra', models.IntegerField(null=True)),
                ('precio_venta', models.IntegerField(null=True)),
                ('descripcion', models.TextField(max_length=300, null=True)),
                ('imagen_Producto', models.ImageField(null=True, upload_to='')),
                ('fecha_vencimiento', models.DateTimeField(null=True)),
                ('existencia', models.BooleanField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Cita',
        ),
        migrations.DeleteModel(
            name='Cuidador',
        ),
        migrations.DeleteModel(
            name='Paciente',
        ),
    ]
