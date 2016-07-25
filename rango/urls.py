from django.conf.urls import url , patterns
from django.contrib import admin
from rango import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
]