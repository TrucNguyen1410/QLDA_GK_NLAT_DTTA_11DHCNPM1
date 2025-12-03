import os
import django

# ⚙️ Khởi tạo môi trường Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qlda_web.settings')
django.setup()

from django.contrib.auth.models import User

users_data = [
    ("tonnuthuykhanh", "Khanh1234@", "STAFF"),
    ("tranhonghanh", "Hanh1234@", "TEACHER"),
    ("tranquocanh", "Quocanh1234@", "TEACHER"),
    ("tranhoangkhai", "Khai1234@", "TEACHER"),
    ("trancongminh", "Minh1234@", "TEACHER"),
    ("phamminhphuong", "Phuong1234@", "TEACHER"),
    ("lethanhthao", "Thao1234@", "TEACHER"),
    ("nguyenthanhtuan", "Luan1234@", "TEACHER"),
    ("dotienhoang", "Hoang1234@", "TEACHER"),
    ("hoangminhhai", "Haui1234@", "TEACHER"),
    ("leminhtue", "Tue1234@", "TEACHER"),
    ("tranthanhquang", "Quang1234@", "TEACHER"),
]

for username, password, role in users_data:
    try:
        user = User.objects.get(username=username)
        print(f"⚠️ User {username} đã tồn tại, bỏ qua.")
    except User.DoesNotExist:
        user = User.objects.create_user(username=username, password=password)
        if role == "STAFF":
            user.is_staff = True
            user.is_superuser = False
        elif role == "TEACHER":
            user.is_staff = False
            user.is_superuser = False
        user.save()
        print(f"✅ Tạo user {username} ({role}) thành công!")
