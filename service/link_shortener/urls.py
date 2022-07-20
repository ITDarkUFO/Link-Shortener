from django.urls import path
from . import views

urlpatterns = [
    # При отключении редиректа позволит получать в корневом каталоге
	path('', views._home, name='_home'),
    path('login/', views._login, name='_login'),
    path('home/', views._home, name='_home'),
]