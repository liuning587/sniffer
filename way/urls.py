from django.conf.urls import include, url
from . import views

# 主要用于执行脚本，定时任务
urlpatterns = [
    # url(r'^$', views.index, name = 'index'),
    url(r'^runApp/', views.runApp, name='runApp'),
    url(r'^runall/', views.runall, name='runall'),
    url(r'^runm2/', views.runm2, name='runm2'),
    url(r'^runother/', views.runother, name='runother'),
    url(r'^runCompass/', views.runCompass, name='runCompass'),
    url(r'^runBAMApp/', views.runBAMApp, name='runBAMApp'),
    url(r'^quartz/', views.quartz, name='quartz'),
    url(r'^r_socket/', views.r_socket, name='r_socket'),
]



