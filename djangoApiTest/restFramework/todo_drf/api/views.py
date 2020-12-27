from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer

from .models import Task
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/task-list/',
        'Detail View':'/task-detail/<str:pk>/',
        'Create':'/task-create/',
        'Update':'/task-update/<str:pk>/',
        'Delete':'/task-delete/<str:pk>/',
        }

    return Response(api_urls)

@api_view(['GET'])
def taskList(request): # 모든 list데이터 출력
    tasks = Task.objects.all() # 모든 pk값을 가져온다
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskDetail(request,pk): # 특정 pk값을 가지는 데이터 출력
    tasks = Task.objects.get(id=pk) # 특정 pk값을 url에서 가져온다
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)

@api_view(['POST']) # 데이터 삽입
def taskCreate(request):
    serializer = TaskSerializer(data=request.data) # data=request 데이터를 적을 칸 생성

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request,pk): # 데이터 수정
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request,pk): # 데이터 삭제
    task = Task.objects.get(id=pk)
    task.delete()

    return Response("Item successfully delete!")