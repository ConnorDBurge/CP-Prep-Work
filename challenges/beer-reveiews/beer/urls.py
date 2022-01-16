from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_beer, name="all_beer"),
    path("new_beer", views.new_beer, name="new_beer"),
    path("<int:beer_id>", views.beer_reviews, name="beer_reviews"),
    path("<int:beer_id>/review", views.new_review, name="new_review"),
    path("<int:beer_id>/<int:review_id>",
         views.delete_review, name="delete_review"),
    path("<int:beer_id>/review/<int:review_id>/edit",
         views.edit_review, name="edit_review"),
]
