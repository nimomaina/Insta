# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-10 16:52
from __future__ import unicode_literals

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
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='uploads/')),
                ('name', models.CharField(max_length=30)),
                ('caption', models.TextField(blank=True)),
                ('profile', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.ImageField(blank=True, upload_to='')),
                ('bio', models.CharField(max_length=255)),
                ('owner', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='picture',
            name='profile_details',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insta.Profile'),
        ),
    ]
