from django.conf.urls import include, url
from . import views
#主要用于新增和修改用例
urlpatterns = [
     url(r'^$', views.index, name='index'),
     url(r'^add/', views.add, name='add'),
     url(r'^addCases/', views.addCases, name='addCases'),
     url(r'^update/', views.update, name='update'),
     url(r'^selectCases/', views.selectCases, name='selectCases'),
     url(r'^select/', views.select, name='select'),
     url(r'^update/', views.update, name='update'),
     url(r'^selectid/', views.selectid, name='selectid'),
   # 报警管理
     url(r'^warningUser/', views.select_warning_user, name='select_warning_user'),
     url(r'^addWarningUser/', views.add_warning_user, name='add_warning_user'),
     url(r'^updateUser/', views.update_user, name='update_user'),
     # url(r'^selectWarningMobile/', views.select_warning_mobile, name='select_warning_mobile'),
     url(r'^selectWarningUser/', views.select_warning_user, name='select_warning_user'),

]
