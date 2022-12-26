from django import template 
from menus.models import Menu 
register = template.Library() 


@register.inclusion_tag('menu.html')
def draw_menu(menu_name, name=None):
    '''отрисовывает меню, имя которого передано в качестве первого аргумента.
    В качестве второго аргумента принимает необязательный параметр,
    который будет передан в функцию, отрисовывающую выбранное меню'''
    menu_collection = {
        'main_menu': main_menu
    }
    return menu_collection[menu_name](name)

def main_menu(name):
    '''отрисовывает основное меню на главной странице, с закрытыми блоками'''
    if not name: 
        return {"menu_items": Menu.objects.all().filter(lvl=0)}
    obj = Menu.objects.get(name=name)
    return {
        "obj": obj,
        "menu_items": Menu.objects.all().filter(lvl=0)
    }


@register.inclusion_tag('childs.html')
def get_childs(name):
    '''принимает name объекта Menu, и отрисовывает все родительские 
    и дочерние (на 1 уровень) пункты меню '''
    menu_all = Menu.objects.all()
    menu_obj = menu_all.get(name=name)
    qs = menu_obj.child.all()
    ids = get_parents_ids(menu_obj, list(qs.values_list("id", flat=True)))
    childs = menu_all.filter(id__in=ids).order_by('lvl', 'position')
    return {
        "menu_obj": menu_obj,
        "childs": childs,
    }

def get_parents_ids(obj: Menu, ids=None):
    '''принимает объект Menu, возвращает список id всех родительских 
    и дочерних пунктов меню'''
    ids = ids if ids else []
    if x:= obj.parent:
       l = list(x.child.all().values_list("id", flat=True))
       ids.extend(l)
       return get_parents_ids(x, ids)
    return ids