from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_beer, name="all_beer"),
    path("new_beer", views.new_beer, name="new_beer"),
]
