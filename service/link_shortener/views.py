import datetime
import logging
import random

from django.contrib.auth import authenticate, login, logout
from django.contrib.sites.models import Site
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import messages

from .forms import NewUserForm
from .models import Link


def get_short_link(length: int = 8):
    permitted_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    output_link = Site.objects.get_current().domain + '/go/'

    for _ in range(length):
        output_link += random.choice(permitted_chars)

    if (Link.objects.filter(short_link=output_link).exists()):
        get_short_link()

    return output_link


def validate_link(link: str):
    if (link.find("https://") == 0 or (link.find("http://") == 0)):
        return True
    return False


def auth(request):
    """Функция проверки входа в систему"""
    # Проверка, что пользователь уже вошел в систему
    if request.user.is_authenticated:
        return True

    # Проверка флажка "Запомнить меня"
    if request.POST.get('remember-me') == 'on':
        request.session.set_expiry(2628000)
    else:
        request.session.set_expiry(0)

    # Проверка данных входа
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return True

    return False


def register(request):
    form = NewUserForm(request.POST)
    if form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, "Вы были зарегистрированы.")
        return redirect('/home/')
    messages.error(request, "Произошла ошибка, введена неверная информация.")
    return render(request, './register/index.html')

# Страницы сайта


def page_login(request):
    """Функция отображения для страницы входа"""
    # Проверка, что пришла форма на вход или выход из системы
    if request.POST.get('action') == 'exit':
        logout(request)
        return redirect('/home/')
    elif request.POST.get('action') == 'sign-in':
        if (auth(request)):
            return redirect('/home/')
        else:
            messages.error(request, "Неправильный логин или пароль!")
            return render(request, './login/index.html')

    # Иначе отрисовываем страницу
    if (request.user.is_authenticated):
        return redirect('/home/')
    else:
        return render(request, './login/index.html')


def page_register(request):
    # Проверка, что пришла форма регистрации
    if request.POST.get('action') == 'sign-up':
        register(request)
    if (request.user.is_authenticated):
        return redirect('/home/')
    else:
        return render(request, './register/index.html')


def page_home(request):
    if request.method == 'POST':
        if request.POST.get('action') == 'create-link':
            link = Link()

            if (validate_link(request.POST.get('link'))):
                link.original_link = request.POST.get('link')
            else:
                link.original_link = f"http://{request.POST.get('link')}"

            link.short_link = get_short_link()
            link.creation_date = datetime.datetime.now()

            if request.user.is_authenticated:
                link.link_creator = request.user
                link.session_id = request.session.session_key
            else:
                link.link_creator = None

                if not request.session or not request.session.session_key:
                    request.session.save()

                link.session_id = request.session.session_key

            link.save()
            return HttpResponseRedirect("/home/")

    if request.user.is_authenticated:
        links = Link.objects.filter(link_creator=request.user)
    else:
        links = Link.objects.filter(session_id=request.session.session_key)

    return render(request, './home/index.html', {'links': links})


def page_go(request):
    current_url = Site.objects.get_current().domain + request.path
    link = Link.objects.filter(short_link=current_url)
    if (link.exists()):
        link.update(following_count=link[0].following_count + 1)
        link.update(following_date=datetime.datetime.now())
        return redirect(link[0].original_link)
    else:
        return redirect('/home/')
