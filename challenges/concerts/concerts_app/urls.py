from django.urls import path
from . import views

app_name = 'concerts_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_results, name='search_results'),
]
