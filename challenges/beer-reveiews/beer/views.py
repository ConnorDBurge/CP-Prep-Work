from http.client import HTTPResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Beer
from .forms import BeerForm
from django.contrib.auth.models import User


@login_required
def all_beer(request):
    user = request.user
    beers = Beer.objects.all().order_by('beer_name')
    return render(request, "beer/all_beer.html", {"user": user, "beers": beers})


@login_required
def new_beer(request):
    if request.method == "POST":
        form = BeerForm(request.POST)
        if form.is_valid():
            beer = form.save(commit=False)
            beer.added_by = request.user
            beer.save()
            return redirect('all_beer')
        else:
            return HTTPResponse('Oops! Something went wrong')
    else:
        form = BeerForm()
        data = {
            "user": request.user,
            "type": "New",
            "form": form
        }
        return render(request, "beer/beer_form.html", data)
