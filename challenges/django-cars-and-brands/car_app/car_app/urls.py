from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('brands/', include('cars_and_brands.urls')),
]
