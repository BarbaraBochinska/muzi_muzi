# Generated by Django 2.2.1 on 2019-05-07 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('muzi_muzi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvertListView',
            fields=[
                ('advert_type', models.TextField()),
                ('first_name', models.CharField(max_length=40)),
                ('city', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('posted_on', models.DateTimeField(primary_key=True, serialize=False)),
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
            name='UserListView',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=100)),
                ('photo_url', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=50)),
                ('prof', models.TextField()),
                ('genre', models.TextField()),
            ],
            options={
                'db_table': 'user_list_view',
                'managed': False,
            },
        ),
    ]