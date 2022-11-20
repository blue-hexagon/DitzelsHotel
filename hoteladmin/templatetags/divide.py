from django import template

register = template.Library()

@register.filter(name="divide", is_safe=True)
def divide(value, arg):
    try:
        return int(value) // int(arg)
    except (ValueError, ZeroDivisionError):
        return None