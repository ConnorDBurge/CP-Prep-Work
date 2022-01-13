from django.shortcuts import render
from .models import Event


def index(request):
    events = Event.objects.order_by('starts_at')
    data = {'events': events}
    return render(request, 'events/index.html', data)
