from django.urls import path
from . import views

appname = 'todo'

urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.create, name='create'),
    path('<int:todo_id>', views.view, name='view')
]
