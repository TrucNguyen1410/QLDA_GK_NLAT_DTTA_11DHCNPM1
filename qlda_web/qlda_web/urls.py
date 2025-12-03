from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('workflow.urls')),  # toàn bộ route chính ở app workflow
]
