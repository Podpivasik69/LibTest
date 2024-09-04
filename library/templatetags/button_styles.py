from django import template

register = template.Library()

@register.filter
def btn_primary(value):
    return f'{value} btn btn-primary'

@register.filter
def btn_secondary(value):
    return f'{value} btn btn-secondary'

@register.filter
def btn_success(value):
    return f'{value} btn btn-success'

@register.filter
def btn_danger(value):
    return f'{value} btn btn-danger'

@register.filter
def btn_warning(value):
    return f'{value} btn btn-warning'

@register.filter
def btn_info(value):
    return f'{value} btn btn-info'

@register.filter
def btn_light(value):
    return f'{value} btn btn-light'

@register.filter
def btn_dark(value):
    return f'{value} btn btn-dark'

@register.filter
def btn_link(value):
    return f'{value} btn btn-link'

# @register.simple_tag
# def styled_button(url, text, style_class):
#     return f'<a class="btn {style_class}" href="{url}" role="button">{text}</a>'