# Generated by Django 4.2.1 on 2023-06-26 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_alter_producto_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='image',
            field=models.ImageField(upload_to='media/image/'),
        ),
    ]