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

@register.tag(name="signed")
@register.simple_tag(takes_context = True)
def header(context, signed):
    header_content = f'''
    <header>
        <div class="header-logo-wrapper">
            <div class="header-logo"></div>
            <div class="header-text-wrapper">
                <span>Hyper</span>
                <span class="header-text">Сервис сокращения ссылок</span>
            </div>
        </div>'''
    
    if (signed == "True"):
        header_content += '''
        <div class="account-wrapper">
            <div></div>
            <button></button>
        </div>
        '''
         
    elif (signed == "False"):
        header_content += '''
        <div class="header-sign-wrapper">
            <button>Войти</button>
            <button>Зарегистрироваться</button>
        </div>'''

    header_content += f'''</header>'''
    return header_content