# DjangoProject

## ToDoApp
>todoapp

### django로 구현한 todo앱

<img src="https://github.com/jdy0120/djangoProject/blob/master/djangoToDoApp/img/index.PNG">

```python
# list.html에 필요한 자료를 보내주는 함수
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

```

<img src="https://github.com/jdy0120/djangoProject/blob/master/djangoToDoApp/img/update.PNG">

```python
# update_task.html에 필요한 내용을 보내주는 함수
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
```

<img src="https://github.com/jdy0120/djangoProject/blob/master/djangoToDoApp/img/delete.PNG">

```python
# delete.html에 필요한 내용을 보내주는 함수
def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method =="POST":
        item.delete()
        return redirect('/')

    context = {'item':item}
    return render(request,'tasks/delete.html',context)
```

## ApiTest
>testApi

### api를 json으로 출력하는 기본적인 api테스트 파일입니다.

<img src="djangoApiTest\restFramework\todo_drf\img\api.png" width=300 height=200>

```python
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
```

<img src="djangoApiTest\restFramework\todo_drf\img\task-list.png" width=200 height=500>

```python
@api_view(['GET'])
def taskList(request): # 모든 list데이터 출력
    tasks = Task.objects.all() # 모든 pk값을 가져온다
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)
```

<img src="djangoApiTest\restFramework\todo_drf\img\task-detail.png" width=300 height=200>

```python
@api_view(['GET'])
def taskDetail(request,pk): # 특정 pk값을 가지는 데이터 출력
    tasks = Task.objects.get(id=pk) # 특정 pk값을 url에서 가져온다
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)
```

<img src="djangoApiTest\restFramework\todo_drf\img\task-create.png" width=300 height=200>

```python
@api_view(['POST']) # 데이터 삽입
def taskCreate(request):
    serializer = TaskSerializer(data=request.data) # data=request 데이터를 적을 칸 생성

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

```

<img src="djangoApiTest\restFramework\todo_drf\img\task-update.png" width=300 height=200>

```python
@api_view(['POST'])
def taskUpdate(request,pk): # 데이터 수정
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
```

<img src="djangoApiTest\restFramework\todo_drf\img\task-delete.png" width=300 height=200>

```python
@api_view(['DELETE'])
def taskDelete(request,pk): # 데이터 삭제
    task = Task.objects.get(id=pk)
    task.delete()

    return Response("Item successfully delete!")
```

## PollingApp

>pollster
투표 프로젝트 입니다.

<img src="djangoPollingApp\pollster\img\index.png">

```python
# 질문을 가져와 출력해준다
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
```

<img src="djangoPollingApp\pollster\img\polls.png">

```python
# 질문 목록을 보여주고 선택할 수 있는 화면
def detail(request, question_id):
  try:
    question = Question.objects.get(pk=question_id)
  except Question.DoesNotExist:
    raise Http404("Question does not exist")
  return render(request, 'polls/detail.html', { 'question': question })
```

<img src="djangoPollingApp\pollster\img\result.png">

```python
# 결과를 보여준다
def results(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return render(request, 'polls/results.html', { 'question': question })
```

<img src="djangoPollingApp\pollster\img\vote.png">

```python
# 투표한다.
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
```