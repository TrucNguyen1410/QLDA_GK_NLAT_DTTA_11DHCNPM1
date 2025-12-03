from django import forms
from .models import Task, Evidence, Evaluation

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'type', 'priority', 'start_date', 'due_date', 'description', 'assignee']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-select'}),
            'priority': forms.Select(attrs={'class': 'form-select'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'assignee': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'title': 'Tên công việc',
            'type': 'Loại công việc',
            'priority': 'Độ ưu tiên',
            'start_date': 'Ngày bắt đầu',
            'due_date': 'Hạn chót',
            'description': 'Mô tả',
            'assignee': 'Người thực hiện',
        }


class EvidenceForm(forms.ModelForm):
    class Meta:
        model = Evidence
        fields = ['file', 'note'] # Tên trường của bạn là 'note' (số ít)
        labels = {
            'file': 'Chọn file minh chứng',
            'note': 'Ghi chú (nếu có)',
        }
        widgets = {
            'file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'note': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

class EvaluationForm(forms.ModelForm):
    class Meta:
        model = Evaluation
        fields = ['score', 'comment'] # Tên trường của bạn là 'score' và 'comment'
        labels = {
            'score': 'Điểm số',
            'comment': 'Nhận xét',
        }
        widgets = {
            # Giả sử 'score' là ô nhập số. Dùng Select nếu nó là ChoiceField
            'score': forms.NumberInput(attrs={'class': 'form-control', 'value': 0}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }
