from django import template
from ..models import SubCategory

register = template.Library()


@register.inclusion_tag('vendor/menu.html', takes_context=True)
def draw_menu(context, menu_name: str) -> dict:

    tree = SubCategory.objects.select_related('category').all()

    global category
    subcategory = []

    for sub in tree:
        if sub.category and sub.category.name == menu_name:
            category = sub.category
        subcategory.append(sub)

    return {
        'category': category,
        'subcategory': subcategory
    }
