from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('concerts/', include('users_app.urls')),
    path('accounts/', include('django.contrib.auth.urls'), name='accounts'),
    path('', TemplateView.as_view(
        template_name='registration/home.html'), name='home'),
]
