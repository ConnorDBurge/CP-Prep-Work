from django.urls import path
from . import views

urlpatterns = [
    path('', views.landmark_list, name='landmark_list'),
    path('<int:landmark_id>', views.landmark_detail, name='landmark_detail'),
    path('top_headlines', views.top_headlines, name='top_headlines'),
]
