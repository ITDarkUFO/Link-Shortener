# Generated by Django 4.0.1 on 2022-07-21 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('link_shortener', '0003_alter_link_creation_date_alter_link_following_count_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'verbose_name': 'Ссылка', 'verbose_name_plural': 'Ссылки'},
        ),
    ]
