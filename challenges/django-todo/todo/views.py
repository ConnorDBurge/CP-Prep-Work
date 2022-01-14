from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import ToDo
from .forms import ToDoForm


def create(request):
    if request.method == "POST":
        form = ToDoForm(request.POST)
        if form.is_valid():
            todo = form.save()
            return redirect('view', todo_id=todo.id)
    else:
        form = ToDoForm()
    data = {
        'form': form
    }
    return render(request, 'todo/new_todo.html', data)


def view(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    data = {'todo': todo}
    return render(request, 'todo/view.html', data)
