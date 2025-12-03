from django.urls import path
from . import views

urlpatterns = [
    # Auth
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    # Tasks
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/create/', views.task_create, name='task_create'),
    path('tasks/<int:task_id>/', views.task_detail, name='task_detail'),
    path('tasks/<int:task_id>/edit/', views.task_edit, name='task_edit'),
    path('tasks/<int:task_id>/delete/', views.task_delete, name='task_delete'),

    # New: Cập nhật trạng thái
    path('tasks/<int:task_id>/update_status/', views.update_status, name='update_status'),

    # Evidence
    path('tasks/<int:task_id>/submit/', views.submit_evidence, name='submit_evidence'),
    path('evidence/<int:ev_id>/delete/', views.delete_evidence, name='delete_evidence'),
    path('evidence/<int:ev_id>/download/', views.download_evidence, name='download_evidence'),

    # Evaluation
    path('tasks/<int:task_id>/evaluate/', views.evaluate_task, name='evaluate_task'),
    path('tasks/<int:task_id>/approve/', views.approve_task, name='approve_task'),

    # Reports
    path('reports/', views.reports, name='reports'),
    path('export/excel/', views.export_tasks_excel, name='export_tasks_excel'),
]
