from http.client import HTTPResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def all_beer(request):
    user = request.user
    return render(request, "beer/all_beer.html", {"user": user})
