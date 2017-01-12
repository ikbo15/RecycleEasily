from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^danger/', views.danger, name='danger'),
	url(r'^metal/', views.metal, name='metal'),
	url(r'^glass/', views.glass, name='glass'),
	url(r'^plastic/', views.plastic, name='plastic'),
	url(r'^paper/', views.paper, name='paper'),
	url(r'^battery/', views.battery, name='battery'),
]
