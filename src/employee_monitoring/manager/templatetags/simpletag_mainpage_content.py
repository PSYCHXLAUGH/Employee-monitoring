from django import template
import manager.views as views


register = template.Library()


@register.simple_tag()
def mainpage_stats():
    return 1



