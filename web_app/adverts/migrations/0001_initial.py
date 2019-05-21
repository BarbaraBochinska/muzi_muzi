# Generated by Django 2.2.1 on 2019-05-21 14:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdvertListView',
            fields=[
                ('advert_id', models.IntegerField(primary_key=True, serialize=False)),
                ('advert_type', models.TextField()),
                ('first_name', models.CharField(max_length=40)),
                ('city', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('posted_on', models.DateTimeField()),
                ('genre', models.CharField(max_length=50)),
                ('profession', models.CharField(max_length=50)),
                ('band_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'advert_list_view',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AdvertView',
            fields=[
                ('advert_id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=40)),
                ('city', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('genre', models.CharField(max_length=50)),
                ('profession', models.CharField(max_length=50)),
                ('band_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'advert_view',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('advert_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('posted_on', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'advert',
            },
        ),
    ]
