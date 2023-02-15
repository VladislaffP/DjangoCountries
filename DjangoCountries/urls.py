from django.contrib import admin
from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.home),
    path('country/<path:id>/', views.view_country),
    path('countries-list', views.countries_list),
    path('languages', views.langs)
]