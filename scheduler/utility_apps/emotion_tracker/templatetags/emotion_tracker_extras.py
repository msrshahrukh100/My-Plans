from django import template
import random
register = template.Library()


@register.filter(name='get_random')
def get_random(value):
    return random.sample(value, 1)[0]
