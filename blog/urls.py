from . import views
from django.urls import path, re_path

urlpatterns = [

	
	re_path(r'^$', views.PostList, {'ct_name': 'home'},name='home'),
    re_path(r'^about/$', views.about, name='aboutme'),
    re_path(r'^article/(?P<id>\d+)/', views.PostDetail, name='post_detail'),


    re_path(r'^category/(?P<ct_name>\w+)/', views.PostList, name='category'),
    re_path(r'^tag/(?P<ct_name>\w+)/', views.PostList, name='tag'),
    re_path(r'^about/$', views.about, name='aboutme'),


] 
