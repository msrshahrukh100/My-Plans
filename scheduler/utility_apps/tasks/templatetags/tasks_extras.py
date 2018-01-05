from django import template
from ..api.utils import get_color_from_score
register = template.Library()


@register.filter(name='getcolor')
def getcolor(value):
    return get_color_from_score(value)
