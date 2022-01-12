from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Post


def index(request):
    posts = Post.objects.all()
    data = {'posts': posts}
    return render(request, 'p_and_c/index.html', data)


def post_view(request, post_id):
    post = Post.objects.get(id=post_id)
    data = {'post': post}
    return render(request, 'p_and_c/post_view.html', data)


def comment(request, post_id):
    return HttpResponse(f'This is the comment view for the post with id: {post_id}')
