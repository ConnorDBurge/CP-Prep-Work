from django.http.response import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'p_and_c/index.html')


def post_view(request, post_id):
    return HttpResponse(f'This is the post view for the post with id: {post_id}')


def comment(request, post_id):
    return HttpResponse(f'This is the comment view for the post with id: {post_id}')
