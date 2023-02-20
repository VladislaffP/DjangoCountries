from django.contrib import admin
from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('country/<path:id>/', views.view_country, name='country'),
    path('countries-list', views.countries_list, name='countries-list'),
    path('languages', views.langs, name='languages-list'),
    path('languages/<path:id>/', views.view_lang, name='lang_detail')
]