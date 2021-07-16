
from django import template


register = template.Library()

@register.filter
def is_upper_filter(value):
    try:
        an_upper = str(value)
        an_uppercase_check = an_upper.isupper()
    except:
        return False

    return an_uppercase_check

