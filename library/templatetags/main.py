from django import template
from ..models import *

register = template.Library()

@register.filter
def replacer(value):
    value = str(value)
    if value=='Пушкинн2':
        return value +'* Для дошкольного возраста'
    return value

@register.simple_tag
def total_book():
    return Book.objects.count()

# @register.inclusion_tag('library/book/type_book.html')
# def show_author_book():
#     author = Author.objects.all()
#     return {'author': author}