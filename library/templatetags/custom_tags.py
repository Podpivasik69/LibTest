from django import template
from ..models import *  # Импорт модели тегов или категорий

register = template.Library()

@register.inclusion_tag('tags_list.html')
def render_tags():
    tags = Book.objects.all()  # Получение всех тегов или категорий
    return {'tags': tags}

@register.inclusion_tag('tags_list.html')
def render_tags(order_by=None):
    tags = Book.objects.all()
    if order_by:
        tags = tags.order_by(order_by)
    return {'tags': tags}
