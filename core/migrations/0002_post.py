# Generated by Django 2.2.9 on 2022-06-08 22:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Image!')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('body', models.TextField(verbose_name='Text')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_id_post', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
