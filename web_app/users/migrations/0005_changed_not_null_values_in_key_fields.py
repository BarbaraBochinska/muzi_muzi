# Generated by Django 2.2.1 on 2019-06-04 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190528_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='muzi_muzi.City'),
        ),
        migrations.AlterField(
            model_name='users',
            name='role',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='muzi_muzi.Role'),
        ),
        migrations.AlterField(
            model_name='users',
            name='video',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='muzi_muzi.Videos'),
        ),
    ]
