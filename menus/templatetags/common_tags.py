from django import template 
from menus.models import Menu 
register = template.Library() 


@register.inclusion_tag('menu.html')
def draw_menu(menu_name, tp=None, lvl=None, pos=None):
    menu_collection = {
        'main_menu': main_menu
    }
    return menu_collection[menu_name](tp, lvl, pos)


def main_menu(tp, lvl, pos):
    menu_items = Menu.objects.all() 
    return {
        "menu_items": menu_items,
    }