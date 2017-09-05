from django.conf.urls import include, url
from . import views
from . import questions
#主要用于新增和修改用例
urlpatterns = [
     url(r'^add/', views.add, name='add'),
     url(r'^addQuestion/', views.addQuestion, name='addQuestion'),
     url(r'^selectQuestion/', views.selectQuestion, name='selectQuestion'),
     url(r'^updateQuestion/', views.updateQuestion, name='updateQuestion'),
     url(r'^update/', views.update, name='update'),
     url(r'^selectid/', views.selectid, name='selectid'),
     url(r'^download/', questions.download, name='download'),


]
