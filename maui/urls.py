from django.conf.urls import include, url
from . import views

# 主要用于新增和修改用例
urlpatterns = [
    url(r'^add_url_cases/', views.add_url_cases, name='add_url_cases'),
    url(r'^add_url/', views.add_url, name='add_url'),
    url(r'^url_add/', views.url_add, name='url_add'),
    url(r'^select_id/', views.select_id, name='select_id'),
    url(r'^update/', views.update, name='update'),
    url(r'^result/', views.result, name='result'),
    url(r'^add_cases/', views.add_cases, name='add_cases'),
    url(r'^selectCases/', views.select_cases, name='selectCases'),
    url(r'^select_cases_id/', views.select_cases_id, name='select_cases_id'),
    url(r'^update_cases/', views.update_cases, name='update_cases'),
    url(r'^run/', views.run, name='run'),

]
