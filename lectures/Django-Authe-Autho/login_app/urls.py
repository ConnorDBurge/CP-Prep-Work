from unicodedata import name
from django.urls import include, path
from login_app import views

app_name = 'login_app'

urlpatterns = [
    path('', views.index, name='home'),
    path('view', views.view_something, name='view_something'),
    path('edit', views.edit_something, name='edit_something'),
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/signup', views.SignUp.as_view(), name='signup'),
    path('error/', views.error, name='error'),
]
