from django import template
from auctions.models import Watchlist

register = template.Library()


@register.simple_tag(takes_context=True)
def watchlist_count(context):
    request = context['request']
    if request.user.is_authenticated:
        watchlist, created = Watchlist.objects.get_or_create(user=request.user)
        return watchlist.listings.count()
    return 0
