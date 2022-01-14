from django.urls import path
from . import views

appname = 'todo'

urlpatterns = [
    path('new', views.create, name='create'),
    path('<int:todo_id>/view', views.view, name='view')
]
