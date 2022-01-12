from django.urls import path, include

urlpatterns = [
    # points to the url.py file under the polls directory
    # 'polls/' is just the entry point for the polls app.
    path('polls/', include('polls.urls'))
]
