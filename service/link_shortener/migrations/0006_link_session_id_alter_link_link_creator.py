# Generated by Django 4.0.1 on 2022-07-23 08:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('link_shortener', '0005_rename_link_link_original_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='session_id',
            field=models.CharField(default=0, max_length=32, verbose_name='ID сессии'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='link',
            name='link_creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='link_creator', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]