from django.shortcuts import render
from .models import Event


def index(request):
    return render(request, 'events/index.html')
