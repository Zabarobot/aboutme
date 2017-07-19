import os


from django.template import Library
from django.template.defaultfilters import stringfilter

from aboutme.settings import BASE_DIR

register = Library()


@register.filter(name='rel_path')
@stringfilter
def rel_path(value):
    return os.path.join(BASE_DIR, value)



