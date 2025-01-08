from django.template import Library
from ..models import *
import jdatetime

register = Library()

@register.simple_tag()
def important_tasks_count(group: TaskGroup) -> int:
    return Task.objects.filter(group= group, is_important= True).count()


@register.simple_tag()
def isdone_tasks_count(group: TaskGroup) -> int:
    return Task.objects.filter(group= group, is_done= True).count()


@register.simple_tag()
def ismiss_tasks_count(group: TaskGroup) -> int:
    return Task.objects.filter(group= group, is_miss= True).count()


@register.filter()
def translate_bool(order: bool) -> str:
    if order:
        return 'شده'
    return 'نشده'


@register.simple_tag()
def calc_percent(total: int, part: int) -> int:
    
    try:
        return float(f'{part / total:2f}') * 100
    
    except ZeroDivisionError:
        raise 'Zero Division Error!'
    

@register.simple_tag()
def show_other_percent(total: int, dones: int) -> int:
    
    try:
        return 100 - (float(f'{dones / total:2f}') * 100)
    
    except ZeroDivisionError:
        raise 'Zero Division Error!'
    