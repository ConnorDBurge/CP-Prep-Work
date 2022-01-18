from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import requests
from .classes.Event import Event


def home(request):  # redirects to home page
    return redirect('')


def search_results(request):
    search_topic = request.POST['query']
    search_phrase = 'Everything' if search_topic == '' else search_topic
    response = requests.get(
        f"https://app.ticketmaster.com/discovery/v2/events.json?apikey=3QoGKoIxgONT7MoA5NrrA1XKKXaktmfM&keyword={search_topic}").json()
    events = list()
    events_json = response['_embedded']['events']
    for event in events_json:
        events.append(Event(event))
    return render(request, 'concerts_pages/search_results.html', {'search_phrase': search_phrase, 'events': events})
