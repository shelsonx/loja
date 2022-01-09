from django import template
from ..models import Category

register = template.Library()

@register.simple_tag
def get_categories(count=3):
    return Category.objects.all()[:count]