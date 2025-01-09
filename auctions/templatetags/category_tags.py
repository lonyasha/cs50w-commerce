from django import template
from auctions.models import Category

register = template.Library()


@register.inclusion_tag('auctions/category_list.html')
def category_list():
    categories = Category.objects.all().order_by('name')
    categories_data = []
    for category in categories:
        count = category.listings.filter(active=True).count()
        categories_data.append({
            'name': category.name,
            'count': count,
            'id': category.id
        })
    return {'categories': categories_data}
