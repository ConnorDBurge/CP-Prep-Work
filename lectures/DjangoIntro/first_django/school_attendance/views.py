from django.shortcuts import render
from school_attendance.models import Student


def index(request):
    return render(request, 'school_attendance/index.html')


def attendance(request):
    data = {
        'students': Student.objects.all()
    }
    return render(request, 'school_attendance/index.html', data)
