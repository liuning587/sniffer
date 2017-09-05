from django.conf.urls import include, url
from . import views
#主要用于执行脚本，定时任务
urlpatterns = [
     # url(r'^$', views.index, name = 'index'),
     url(r'^online/', views.online, name = 'online'),
     url(r'^end_online/', views.end_online, name = 'end_online'),
     url(r'^today_online/', views.today_online, name = 'today_online'),
     url(r'^weeks_online/', views.weeks_online, name = 'weeks_online'),
     url(r'^month_online/', views.month_online, name = 'month_online'),

]
