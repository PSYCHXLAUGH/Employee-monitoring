from django import template
import manager.views as views
from manager.models import Booking
from manager.models import Address
from manager.models import Table

register = template.Library()


@register.simple_tag()
def get_booking():
    booking = Booking.objects.all()
    return {'booking': booking}


@register.simple_tag()
def get_address():
    address = Address.objects.all()
    return {'address': address}


@register.simple_tag()
def get_tables():
    tables = Table.objects.all()
    return {'table': tables}

