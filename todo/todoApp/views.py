from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Task
from django.views import View
from .forms import TaskForm

def home(request):
    tasks = Task.objects.all()
    context = {
        'tasks':tasks
    }
    return render(request,'home.html',context)

def add_task(request):
    form = TaskForm(request.POST)
    if 'submit' in request.POST:
        if form.is_valid():
            print(form.cleaned_data)
            task = form.save()
            task.save()
            print(task)
            return redirect("home")
    else:
        return render(request,'taskadd.html',context={'form':form})
    

def delete_task(request, id):
    task = Task.objects.get(pk = id)

    if request.method == 'POST':
        task.delete()
        return redirect('home')

    my_context = {
        'task':task
    }

    return render(request,'taskdelete.html',my_context)

def edit_task(request, id):
    task = Task.objects.get(pk=id)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
        return redirect('home')

    context = {
        'form': form,
    }
    return render(request,'taskedit.html',context)
    

