from django.http import JsonResponse
from .models import Student, Course
from .serializers import StudentSerializer

def all_students(request):
    students = Student.objects.all()
    serialized_students = StudentSerializer(students).all_students
    return JsonResponse(data=serialized_students, status=200)

def detail_student(request, student_id):
    pass

def edit_student(request, student_id):
    pass

def delete_student(request, student_id):
    pass
