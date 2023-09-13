from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from todo.models import Task
# Create your views here.


def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')


def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')


def mark_as_not_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')


def edit_task(request, pk):
    curr_task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        new_task = request.POST['task']
        curr_task.task = new_task
        curr_task.save()
        return redirect('home')
    else:
        context = {
            'get_task': curr_task
        }
        return render(request, 'edit_task.html', context)


def delete(request, pk):
    get_task = get_object_or_404(Task, pk=pk)
    get_task.delete()
    return redirect('home')
