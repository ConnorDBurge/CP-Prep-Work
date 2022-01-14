from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.new_event, name='new_event'),
    path('<int:event_id>/delete', views.delete_event, name='delete'),
]
