from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import ToDo
from .forms import ToDoForm


def index(request):
    all_todo = ToDo.objects.all()
    data = {
        'all_todo': all_todo
    }
    return render(request, 'todo/index.html', data)


def create(request):
    if request.method == "POST":
        form = ToDoForm(request.POST)
        if form.is_valid():
            todo = form.save()
            return redirect('view', todo_id=todo.id)
    else:
        form = ToDoForm()
    data = {
        'form': form,
        'method': 'Create New ToDo'
    }
    return render(request, 'todo/new_todo.html', data)


def edit(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    if request.method == "POST":
        form = ToDoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save()
            return redirect('index')
    elif request.method == "GET":
        form = ToDoForm(instance=todo)
        data = {
            'todo': todo,
            'form': form,
            'method': 'Edit ToDo'
        }
        return render(request, 'todo/edit_todo.html', data)


def view(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    data = {'todo': todo}
    return render(request, 'todo/view.html', data)


def delete(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.delete()
    return redirect('index')
