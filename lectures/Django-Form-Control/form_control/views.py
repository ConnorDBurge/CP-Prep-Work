from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Profile
from .forms import ProfileForm


def form(request):
    submitted = False
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('?submitted=True')
    else:
        form = ProfileForm()
        if 'submitted' in request.GET:
            submitted = True
        return render(request, 'form_control/form.html', {"form": form, "submitted": submitted})
