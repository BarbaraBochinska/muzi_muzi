# Generated by Django 2.2.1 on 2019-05-21 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0003_advert_user'),
    ]

    operations = [
        migrations.RunSQL("""

                drop view if exists advert_view;
                drop view if exists advert_list_view;
                create view advert_view as (
                    select first_name,
                           a.advert_id as advert_id,
                           c.name     city,
                           a.title,
                           a.description,
                           g.name     genre,
                           p.name     profession,
                           case
                               when a.band_id is not null then (
                                   select b.name
                                   from band b
                                            where b.band_id = a.band_id
                               )
                               else null
                               end as band_name
                    from users
                             join advert a on users.user_id = a.user_id
                             join profession p on a.profession_id = p.prof_id
                             join genre g on a.genre_id = g.genre_id
                             join city c on users.city_id = c.city_id
                );

                create view advert_list_view as (
                    select a.advert_id,
                           case
                               when a.band_id is not null then 'band advert'
                               else 'musician advert'
                               end as advert_type,
                           first_name,
                           c.name     city,
                           a.title,
                           a.posted_on,
                           g.name     genre,
                           p.name     profession,
                           case
                               when a.band_id is not null then (
                                   select b.name
                                   from band b
                                            where b.band_id = a.band_id
                               )
                               else null
                               end as band_name
                    from users
                             join advert a on users.user_id = a.user_id
                             join profession p on a.profession_id = p.prof_id
                             join genre g on a.genre_id = g.genre_id
                             join city c on users.city_id = c.city_id
                );
                                """)
    ]
