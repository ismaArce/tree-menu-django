from django import template
from django.template.defaultfilters import safe
from menu.models import Menu

import re

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):

    request = context['request']
    current_url = re.sub(r'^/', '', request.path)
    
    menu_items = Menu.objects.filter(name=menu_name).select_related('parent')

    parent_map = {}
    for item in menu_items:
        parent_map.setdefault(item.parent_id, []).append(item)

    def render_menu_items(items, parent_active=False):
        html = "<ul>"
        for item in items:
            active = item.url == current_url or item.has_active_child(current_url)
            hidden_class = "hidden" if not active and not item.has_active_child(current_url) and not parent_active else ""
            html += f"<li class='nav-item  {hidden_class}'><a class='nav-link {'dropdown-toggle' if item.has_children() else ''}' href='{item.url}'>{item.name}</a>"
            children = item.children.all()
            if children:
                html += render_menu_items(children, active)
            html += "</li>"
        html += "</ul>"
        return safe(html)

    html = render_menu_items(parent_map.get(None, []), True)
    return html