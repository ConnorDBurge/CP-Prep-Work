from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_students, name='all_students'),
    # path('<int:student_id>', view.detail_student, name='detail_student'),
    # path('<int:student_id>/edit', view.edit_student, name='edit_student'),
    # path('<int:student_id>/delete', view.delete_student, name='delete_student'),
]