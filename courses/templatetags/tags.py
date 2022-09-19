from django import template
from courses.models import *
register = template.Library()

def cart_count(user):
    cart = Cart.objects.get(user=user)
    count = cart.courses.count()
    return count if count != 0 else ""

def cart_total_price(cart):
    total = 0
    for item in cart.courses.all():
        total += item.final_price
    return total

register.filter('cart_count', cart_count)
register.filter('cart_total_price', cart_total_price)
