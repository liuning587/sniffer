from django.conf.urls import include, url
from . import views

# 主要用于新增和修改用例
urlpatterns = [
    url(r'^snifferresult/', views.sniffercount, name='sniffercount'),
    url(r'^result/', views.result, name='reslut'),
    url(r'^statistics/', views.statistics, name='statistics'),
    url(r'^svncount/', views.svn_count, name='svn_count'),
    url(r'^svnchart/', views.svn_chart, name='svn_chart'),
    url(r'^img_email/', views.img_email, name='img_email'),
]
