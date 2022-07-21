from django.db import models
from django.contrib.auth.models import User


class Link(models.Model):
    original_link = models.URLField(max_length=300, verbose_name="Ссылка")
    short_link = models.URLField(max_length=20, unique=True, verbose_name="Короткая ссылка")
    creation_date = models.DateTimeField(verbose_name="Дата создания")
    link_creator = models.ForeignKey(User, related_name="link_creator", on_delete=models.CASCADE, verbose_name="Пользователь")
    following_count = models.IntegerField(default=0, verbose_name="Количество переходов")

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'