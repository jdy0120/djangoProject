from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *

# Create your views here.

def index(request):
    tasks = Task.objects.all() # Task는 title, complete, created가 담겨있는 class

    form = TaskForm() # 자주 사용하는 form을 저장했다.

    if request.method =='POST':
        form = TaskForm(request.POST) # form이 있는지 확인
        if form.is_valid():
            form.save() # 저장
        return redirect('/')

    context = {'tasks':tasks, 'form':form}
    return render(request, 'tasks/list.html', context) # context object를 해당 html파일에 보낸다

def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}

    return render(request,'tasks/update_task.html', context) 

def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method =="POST":
        item.delete()
        return redirect('/')


    context = {'item':item}
    return render(request,'tasks/delete.html',context)