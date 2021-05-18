from django.shortcuts import render, redirect, get_object_or_404
from .forms import TodoForm
from .models import Todo
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def get_showing_todos(request, todos):
    if request.method == 'GET' and request.GET.get('filter'):
        if request.GET.get('filter') == 'incomplete':
            return todos.filter(is_completed = False)

        if request.GET.get('filter') == 'complete':
            return todos.filter(is_completed = True)
    return todos

@login_required
def home(request):
    todos = Todo.objects.filter(owner = request.user)
    completed = todos.filter(is_completed=True).count()
    incompleted = todos.filter(is_completed=False).count()
    all_todos_count = todos.count()
    return render(request, 'todo/index.html', {'todos':get_showing_todos(request, todos), 'all_todos_count':all_todos_count, 'completed':completed, 'incompleted':incompleted, 'all_todos_count':all_todos_count})

@login_required
def create_todo(request):
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = Todo()
            todo.title = form.cleaned_data.get('title')
            todo.description = form.cleaned_data.get('description')
            todo.is_completed = form.cleaned_data.get('is_completed')
            # print("cleaned data here:", form.cleaned_data.get('title'))
            # todo = form.save()
            # print(todo.id)
            todo.owner = request.user
            todo.save()
            messages.add_message(request, messages.SUCCESS, "Todo Created")
            return redirect('todo:todo-detail', id=todo.id)
    return render(request, 'todo/create_todo.html', {'form':form, "value":"Add Todo"})

@login_required
def todo_detail(request, id):
    # todo = Todo.objects.get(id=id)
    todo = get_object_or_404(Todo, pk=id)
    return render(request, 'todo/todo_detail.html', {'todo':todo})

@login_required
def todo_delete(request, id):
    todo = get_object_or_404(Todo, pk=id)
    if request.method == "POST" and todo.owner == request.user:
        todo.delete()
        messages.add_message(request, messages.SUCCESS, "Todo Deleted")
        return redirect('todo:home')
    return render(request, 'todo/todo_delete.html', {'todo':todo})

@login_required
def todo_edit(request, id):
    todo = get_object_or_404(Todo, pk=id)
    form = TodoForm(instance=todo)
    if request.method == "POST" and todo.owner == request.user:
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save()
            # print(todo.id)
            messages.add_message(request, messages.SUCCESS, "Todo Updated")
            return redirect('todo:todo-detail', id=todo.id)
    return render(request, 'todo/create_todo.html', {'todo':todo, "form":form, "value":"Update Todo"})

