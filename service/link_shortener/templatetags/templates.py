import logging

from django import template
from django.conf import settings
from django.contrib.sites.models import Site
from django.views.decorators.csrf import csrf_protect

register = template.Library()

# Пример шаблона
# @register.tag(name="temp") - если нужно
# @register.simple_tag(takes_context = True)
# def getInfo(context, temp):
# 	Тело функции


@register.simple_tag(takes_context=True)
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


@register.simple_tag(takes_context=False)
def header_logo():
    site_url = Site.objects.get_current().domain
    return f'''
    <div class="logo-wrapper">
            <a style="display: contents;" href="{site_url}">
                <div id="logo"></div>
                <div class="name-wrapper">
                    <span id="name">Hyper</span>
                    <span id="description">Сервис сокращения ссылок</span>
                </div>
            </a>
        </div>
    '''

@register.simple_tag(takes_context=False)
def footer():
    return f'''
    <footer>
        <span>© 2022 Hyper</span>
    </footer>
    '''
