from django.shortcuts import redirect, get_object_or_404
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
