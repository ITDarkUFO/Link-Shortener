from django.db import models
from django.contrib.auth.models import User


class Link(models.Model):
    original_link = models.URLField(max_length=300, verbose_name="Оригинальная ссылка")
    short_link = models.URLField(max_length=20, unique=True, verbose_name="Короткая ссылка")
    
    link_creator = models.ForeignKey(User, related_name="link_creator", null=True, on_delete=models.CASCADE, verbose_name="Пользователь")
    session_id = models.CharField(max_length=32, verbose_name="ID сессии")

    creation_date = models.DateTimeField(verbose_name="Дата создания")
    following_count = models.PositiveIntegerField(default=0, verbose_name="Количество переходов")
    following_date = models.DateTimeField(null=True, verbose_name="Дата последнего перехода")
    

    class Meta:
        verbose_name = 'ссылка'
        verbose_name_plural = 'ссылки'