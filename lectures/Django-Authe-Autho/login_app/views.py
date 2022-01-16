from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required, permission_required


def index(request):
    return render(request, 'pages/home.html')


def error(request):
    return HttpResponse('You do not have permissions to view this page')


@login_required
def view_something(request):
    return render(request, 'pages/view.html')


@login_required
# @permission_required('auth.my_edit_perm', login_url='login_app:error')
def edit_something(request):
    if request.user.is_authenticated:
        if request.user.has_perm('auth.my_edit_perm'):
            return render(request, 'pages/edit.html')
        else:
            return redirect('login_app:error')


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login_app:login')
    template_name = 'registration/signup.html'
