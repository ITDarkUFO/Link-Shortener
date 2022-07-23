from django.urls import path, re_path
from . import views

urlpatterns = [
    # При отключении редиректа позволит получать в корневом каталоге
	path('', views.page_home, name='home'),
    path('login/', views.page_login, name='login'),
    path('home/', views.page_home, name='home'),
    re_path(r'go/*', views.page_go, name='go')
]