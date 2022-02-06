from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Student, Course
from .forms import StudentForm, CourseForm
from .serializers import StudentSerializer

def all_students(request):
    students = Student.objects.all()
    serialized_students = StudentSerializer(students).all_students
    return JsonResponse(data=serialized_students, status=200)

def detail_student(request, student_id):
    student = Student.objects.get(id=student_id)
    serialized_student = StudentSerializer(student).detail_student
    return JsonResponse(data=serialized_student, status=200)

@csrf_exempt
def new_student(request):
    if request.method == 'POST':
        data = json.load(request)
        form = StudentForm(data)
        if form.is_valid():
            student = form.save(commit=True)
            serialized_student = StudentSerializer(student).detail_student
            return JsonResponse(data=serialized_student, status=200)

@csrf_exempt
def edit_student(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        data = json.load(request)
        form = StudentForm(data, instance=student)
        if form.is_valid():
            student = form.save(commit=True)
            serialized_student = StudentSerializer(student).detail_student
            return JsonResponse(data=serialized_student, status=200)

@csrf_exempt
def delete_student(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return JsonResponse(data={'message': 'Student deleted'}, status=200)        