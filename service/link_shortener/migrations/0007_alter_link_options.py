# Generated by Django 4.0.1 on 2022-07-23 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('link_shortener', '0006_link_session_id_alter_link_link_creator'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'verbose_name': 'ссылка', 'verbose_name_plural': 'ссылки'},
        ),
    ]
