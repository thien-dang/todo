from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404

from .models import Task


def create_task(request):
    new_task = request.POST['task']
    if new_task:
        Task.objects.get_or_create(task=new_task)
    return redirect('home')


def mark_as_done(request, pk):
    try:
        task = get_object_or_404(Task, pk=pk)
        task.is_completed = True
        task.save()
    except Http404:
        pass  # TODO: Add a feature to handle Http404 if needed.

    return redirect('home')


def mark_as_undone(request, pk):
    try:
        task = get_object_or_404(Task, pk=pk)
        task.is_completed = False
        task.save()
    except Http404:
        pass  # TODO: Add a feature to handle Http404 if needed.

    return redirect('home')


def edit_task(request, pk):
    current_task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        new_task = request.POST['new task']
        current_task.task = new_task
        current_task.save()
        return redirect('home')
    else:
        context = {
            'current_task': current_task
        }
        return render(request, 'edit_task.html', context=context)
