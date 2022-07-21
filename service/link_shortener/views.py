import datetime
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
import logging

from .models import Link

def auth(request):
    """Функция проверки входа в систему"""
    if request != None:
        # Проверка, что пользователь уже вошел в систему
        if request.user.is_authenticated:
            return True

        # Проверка флажка "Запомнить меня"
        if request.POST.get('action') == 'login':
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


def _login(request):
    """Функция отображения для страницы входа"""
    # Проверка, что пришла форма на выход из системы
    if request.POST.get('action') == 'exit':
        logout(request)
    elif auth(request):
        return redirect('/home/')

    return render(request, './home/index.html')


def _home(request):
    if request.method == 'POST':
        if request.POST.get('link'):
            link=Link()
            link.original_link = request.POST.get('link')
            link.short_link = "https://example.com/"
            link.creation_date = datetime.datetime.now()
            link.link_creator = request.user
            link.save()

    return render(request, './home/index.html')
