from django.conf import settings
from django.urls import path, re_path
from django.views.static import serve
from . import views

urlpatterns = [
    # При отключении редиректа позволит получать в корневом каталоге
	path('', views.page_home, name='home'),
    path('login/', views.page_login, name='login'),
    path('register/', views.page_register, name='register'),
    path('home/', views.page_home, name='home'),
    re_path(r'go/*', views.page_go, name='go'),
    re_path(r'^static/(?:.*)$', serve, {'document_root': settings.STATIC_DIR, })
]