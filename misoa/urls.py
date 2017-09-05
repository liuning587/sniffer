"""sniffer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    url(r'^online/', views.online, name='online'),
    url(r'^end_online/', views.end_online, name='end_online'),
    url(r'^today_online/', views.today_online, name='today_online'),
    url(r'^on_online/', views.on_online, name='on_online'),
    url(r'^today_online_mail/', views.today_online_mail, name='today_online_mail'),

    # url(r'^month_online/', views.month_online, name='month_online'),
]
