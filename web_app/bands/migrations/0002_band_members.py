# Generated by Django 2.2.1 on 2019-05-21 14:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bands', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='members',
            field=models.ManyToManyField(db_table='user_band', to=settings.AUTH_USER_MODEL),
        ),
    ]
