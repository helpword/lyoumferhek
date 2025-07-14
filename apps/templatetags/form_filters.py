# yourapp/templatetags/form_filters.py
from django import template

register = template.Library()

@register.filter(name='as_widget')
def as_widget(value, attrs):
    return value.as_widget(attrs={'class': 'form-control'})
