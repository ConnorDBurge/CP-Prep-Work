from django.shortcuts import render, redirect
from .models import Landmark


def landmark_list(request):
    all_landmarks = Landmark.objects.all()
    return render(request, 'map/landmark_list.html', {'all_landmarks': all_landmarks})


def landmark_detail(request, landmark_id):
    landmark = Landmark.objects.get(id=landmark_id)
    return render(request, 'map/landmark_detail.html', {'landmark': landmark})


def top_headlines(request):

    return render(request, 'map/top_headlines.html', data)
