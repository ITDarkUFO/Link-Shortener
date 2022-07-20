from django.http import HttpResponse
from django.conf import settings
from django import template
import logging

register = template.Library()


# Пример шаблона
# @register.tag(name="temp") - если нужно
# @register.simple_tag(takes_context = True)
# def getInfo(context, temp):
# 	Тело функции


@register.simple_tag(takes_context = True)
def meta(context):
    static = settings.STATIC_URL
    page = str(context['request']).split('/')[1].lower()

    return f'''
    <title>Hyper - сокращатель ссылок</title>
    <meta name="viewport" content="width=device-width, initial-scale=1"/>
    <link rel="shortcut icon" type="image/x-icon" href="{static}main/images/favicon.ico">

    <link rel="stylesheet" type="text/css" href="{static}main/styles/base.css">
    <link rel="stylesheet" type="text/css" href="{static}{page}/styles/{page}.css">
    '''