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
from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^$', include('rail.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^rail/', include('rail.urls')),
    url(r'^way/', include('way.urls')),
    url(r'^result/', include('result.urls')),
    url(r'^statSVN/', include('statSVN.urls')),
    # url(r'^tdoa/', include('tdoa.urls')),
    url(r'^qualityS/', include('qualityS.urls')),
    url(r'^maui/', include('maui.urls')),
    url(r'^misoa/', include('misoa.urls')),
    url(r'^a/', include('a.urls')),
    url(r'^favicon.ico$',RedirectView.as_view(url=r'static/favicon.ico')),
    url(r'^about/$', TemplateView.as_view(template_name="about.html")),
    # url(r'^a/$', TemplateView.as_view(template_name="a.html")),
    url(r'^aback/$', TemplateView.as_view(template_name="aback.html")),
    url(r'^mo/$', TemplateView.as_view(template_name="mo.html")),
    url(r'^dmo/$', TemplateView.as_view(template_name="dmo.html")),
]
