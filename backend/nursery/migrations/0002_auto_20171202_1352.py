# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-02 13:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('nursery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('sort', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='question',
            old_name='question',
            new_name='text',
        ),
        migrations.RemoveField(
            model_name='question',
            name='city',
        ),
        migrations.AddField(
            model_name='city',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='parent_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='nursery.Question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='score',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nursery.City'),
        ),
        migrations.AddField(
            model_name='question',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='nursery.Category'),
        ),
    ]