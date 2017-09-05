from django.conf.urls import include, url
from . import views
#主要用于新增和修改用例
# 所有的外链接都去掉，指定访问/statSVN/monthstat/
urlpatterns = [
     url(r'^monthstat/', views.monthStat, name='monthStat'),
     url(r'^weeksstat/', views.weeksStat, name='weeksStat'),
     url(r'^daystat/', views.dayStat, name='dayStat'),
     url(r'^adduser/', views.adduser, name='adduser'),
]
