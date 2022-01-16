from http.client import HTTPResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Beer, BeerReview
from .forms import BeerForm, BeerReviewForm


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
            return redirect('beer_reviews', beer_id=beer.id)
        else:
            return HTTPResponse('Oops! Something went wrong')
    else:
        form = BeerForm()
        data = {
            "type": "New",
            "form": form
        }
        return render(request, "beer/beer_form.html", data)


@login_required
def beer_reviews(request, beer_id):
    beer = Beer.objects.get(id=beer_id)
    data = {
        "beer": beer,
        "reviews": beer.reviews.all(),
        "user": request.user
    }
    return render(request, "beer/beer_reviews.html", data)


@login_required
def new_review(request, beer_id):
    beer = Beer.objects.get(id=beer_id)
    if request.method == "POST":
        form = BeerReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.added_by = request.user
            review.beer_name = beer
            review.save()
            return redirect('beer_reviews', beer_id=beer.id)
        else:
            return HTTPResponse('Oops! Something went wrong')
    else:
        form = BeerReviewForm()
        data = {
            "type": "New",
            "form": form
        }
        return render(request, "beer/review_form.html", data)


@login_required
def edit_review(request, beer_id, review_id):
    beer = Beer.objects.get(id=beer_id)
    review = BeerReview.objects.get(id=review_id)
    if request.method == "POST":
        form = BeerReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.added_by = request.user
            review.beer_name = beer
            review.save()
            return redirect('beer_reviews', beer_id=beer.id)
        else:
            return HTTPResponse('Oops! Something went wrong')
    else:
        form = BeerReviewForm(instance=review)
        data = {
            "type": "Edit",
            "form": form
        }
        return render(request, "beer/review_form.html", data)


@login_required
def delete_review(request, beer_id, review_id):
    review = BeerReview.objects.get(id=review_id)
    review.delete()
    return redirect('beer_reviews', beer_id=beer_id)
