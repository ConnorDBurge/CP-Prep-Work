from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Event
from .forms import EventForm
from django.contrib.auth.models import User


def index(request):
    if request.method == "POST":
        print(request.method)
        form = EventForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            event = form.save(commit=False)
            event.name = data['name']
            event.description = data['description']
            event.starts_at = data['starts_at']
            event.ends_at = data['ends_at']
            event.save()
            return redirect('index')
    else:
        events = Event.objects.order_by('starts_at')
        form = EventForm()
        data = {
            'events': events,
            'form': form
        }
        return render(request, 'events/index.html', data)


def new_event(request):
    return index(request)


def delete_event(request, event_id):
    event = Event.objects.get(id=event_id)
    event.delete()
    return redirect('index')
