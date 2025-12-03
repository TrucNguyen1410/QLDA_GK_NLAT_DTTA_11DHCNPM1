from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Task
from .forms import TaskForm

@csrf_exempt
def api_tasks(request):
    if request.method == 'GET':
        tasks = list(Task.objects.values())
        return JsonResponse(tasks, safe=False)

@csrf_exempt
def api_task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        return JsonResponse({
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'status': task.status
        })
