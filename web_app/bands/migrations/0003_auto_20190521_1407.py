# Generated by Django 2.2.1 on 2019-05-21 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0002_band_members'),
    ]

    operations = [
        migrations.RunSQL("""
            drop view if exists band_members_view;

            create view band_members_view as
                select b.band_id, b.name, string_agg(u.first_name || ' ' || u.last_name, ', ') as members
                from band b
                         join user_band ub on b.band_id = ub.band_id
                         join users u on ub.users_id = u.user_id
                group by b.band_id;""")
    ]