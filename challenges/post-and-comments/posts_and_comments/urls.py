from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.post_view, name='post_view'),
    path('<int:post_id>/comment', views.comment, name='comment')
]
