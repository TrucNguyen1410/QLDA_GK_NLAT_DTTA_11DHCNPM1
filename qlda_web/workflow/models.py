from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    TYPE_CHOICES = [
        ('TEACH', 'Giảng dạy'),
        ('RESEARCH', 'Nghiên cứu'),
        ('REPORT', 'Báo cáo'),
        ('OTHER', 'Khác'),
    ]

    PRIORITY_CHOICES = [
        ('LOW', 'Thấp'),
        ('MED', 'Trung bình'),
        ('HIGH', 'Cao'),
    ]

    STATUS_CHOICES = [
        ('NEW', 'Mới tạo'),
        ('DOING', 'Đang thực hiện'),
        ('EVAL', 'Đã đánh giá'),
        ('DONE', 'Hoàn thành'),
        ('APPROVED', 'Đã phê duyệt'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='NEW')
    start_date = models.DateField()
    due_date = models.DateField()
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='creator')

    def __str__(self):
        return self.title


class Evidence(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='evidences/')
    note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def filename(self):
        return self.file.name.split('/')[-1]

    def __str__(self):
        return f"{self.task.title} - {self.uploader.username}"


class Evaluation(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    evaluator = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(blank=True)
    score = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Đánh giá {self.task.title} - {self.score} điểm"
