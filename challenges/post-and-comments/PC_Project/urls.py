from django.urls import path, include

urlpatterns = [
    path('post/', include('posts_and_comments.urls')),
]
