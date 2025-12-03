from django.core.exceptions import PermissionDenied
from functools import wraps


def group_required(group_name):
    """
    Chỉ cho phép user thuộc đúng 1 group được truy cập.
    Dùng cho view cần hạn chế 1 nhóm duy nhất.
    Ví dụ:
        @login_required
        @group_required('TEACHER')
        def submit_task(...):
            ...
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated and request.user.groups.filter(name=group_name).exists():
                return view_func(request, *args, **kwargs)
            raise PermissionDenied  # Trả về lỗi 403 nếu không đủ quyền
        return _wrapped_view
    return decorator


def groups_required(*group_names):
    """
    Cho phép user thuộc 1 trong nhiều group được truy cập.
    Dùng cho view mà nhiều nhóm cùng có quyền.
    Ví dụ:
        @login_required
        @groups_required('ADMIN_STAFF', 'HEAD')
        def reports(...):
            ...
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated and request.user.groups.filter(name__in=group_names).exists():
                return view_func(request, *args, **kwargs)
            raise PermissionDenied  # 403 Forbidden
        return _wrapped_view
    return decorator
