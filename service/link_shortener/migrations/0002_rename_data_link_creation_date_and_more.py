# Generated by Django 4.0.1 on 2022-07-21 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('link_shortener', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='link',
            old_name='data',
            new_name='creation_date',
        ),
        migrations.RenameField(
            model_name='link',
            old_name='user',
            new_name='link_creator',
        ),
        migrations.AddField(
            model_name='link',
            name='following_count',
            field=models.IntegerField(default=0),
        ),
    ]