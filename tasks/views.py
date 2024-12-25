from bisect import insort
from itertools import product

from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm


def home(request):
    tasks = Task.objects.all()
    return render(request, 'home.html', {'tasks': tasks })

def create_task(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'task_form.html', {'form': form})

def update_task(request,pk):
    task = get_object_or_404(Task, id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'task_form.html', {'form': form})


def delete_task(request, pk):
     task =(get_object_or_404(Task, id=pk))
     task.delete()
     return redirect('home')

def detail_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    return render(request, 'task_detail.html', {'task': task})