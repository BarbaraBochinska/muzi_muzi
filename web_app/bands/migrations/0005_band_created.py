# Generated by Django 2.2.1 on 2019-05-31 16:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0004_auto_20190522_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
