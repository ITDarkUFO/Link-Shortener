# Generated by Django 4.0.1 on 2022-07-23 09:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('link_shortener', '0007_alter_link_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='following_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 23, 14, 0, 12, 227236), verbose_name='Дата последнего перехода'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='link',
            name='original_link',
            field=models.URLField(max_length=300, verbose_name='Оригинальная ссылка'),
        ),
    ]