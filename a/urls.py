from django.conf.urls import include, url
from . import views
#主要用于新增和修改用例
urlpatterns = [
     url(r'^add/', views.add, name='add'),
     url(r'^update/', views.update, name='update'),
     url(r'^select/', views.select_all, name='select_all'),
     url(r'^$', views.index, name='index'),

]
