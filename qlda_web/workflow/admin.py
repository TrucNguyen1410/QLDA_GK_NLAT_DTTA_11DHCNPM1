from django.contrib import admin
from .models import Task, Evidence, Evaluation


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'priority', 'status', 'start_date', 'due_date', 'assignee')
    list_filter = ('status', 'priority', 'type')
    search_fields = ('title', 'description', 'assignee__username')


@admin.register(Evidence)
class EvidenceAdmin(admin.ModelAdmin):
    list_display = ('task', 'uploader', 'file', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('task__title', 'uploader__username')


@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    list_display = ('task', 'evaluator', 'score', 'created_at')  
    list_filter = ('score', 'created_at')                        
    search_fields = ('task__title', 'evaluator__username')
