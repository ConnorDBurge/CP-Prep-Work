from django.urls import path
import school_attendance.views as views

urlpatterns = [
    path('', views.index, name='home_page')
]
