# workflow/templatetags/form_filters.py
from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css):
    """Thêm class CSS vào form field."""
    return field.as_widget(attrs={"class": css})
