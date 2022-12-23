from django import template 
from menus.models import Menu 
register = template.Library() 


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context):
    menu_items = Menu.objects.all() 
    return {
        "menu_items": menu_items,
    }