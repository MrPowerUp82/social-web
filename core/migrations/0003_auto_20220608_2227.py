# Generated by Django 2.2.9 on 2022-06-08 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='posts/', verbose_name='Image!'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='perfil_image',
            field=models.ImageField(blank=True, null=True, upload_to='profiles/', verbose_name='Foto de Perfil!'),
        ),
    ]
