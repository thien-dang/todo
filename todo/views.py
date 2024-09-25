from django.shortcuts import redirect

from .models import Task


def create_task(request):
    new_task = request.POST['task']
    if new_task:
        Task.objects.get_or_create(task=new_task)
    return redirect('home')
