from django.urls import path
from . import views

urlpatterns = [
    # a list of all the car brands
    path('', views.brand_list, name='brand_list'),
    # form for a new car brand
    path('new', views.brand_new, name='brand_new'),
    # see a specific car brand
    path('<int:brand_id>', views.brand_detail, name='brand_detail'),
    # edit page for a specific car brand
    path('<int:brand_id>/edit', views.brand_edit, name='brand_edit'),

    # form for a new car under a specific car brand
    path('<int:brand_id>/cars/new', views.car_new, name='car_new'),
    # see a specific car for a specific car brand
    path('<int:brand_id>/cars/<int:car_id>',
         views.car_detail, name='car_detail'),
    # edit page for a specific car under a specific car brand
    path('<int:brand_id>/cars/<int:car_id>/edit',
         views.car_edit, name='car_edit'),
]
