from django import template
from django.db.models import Count
from io import BytesIO
from PIL import Image
from django.core.files.base import File

from booking.booking_table.models import BookingTable
from booking.module_booking.models import ModuleBooking
from hotel.address.models import HotelAddress
from hotel.bankDetail.models import BankDetail
from hotel.cancellation_policy.models import Cancellation_Policy
from hotel.gallery.models import HotelGallery
from hotel.models import Hotels

register = template.Library()

@register.filter(name='to_int')
def to_int(value):
    return int(value)

@register.filter(name='hotelBookingCount')
def hotelBookingCount(id):
    data = {}
    bookingtableinstancecount = 0
    modules = ModuleBooking.objects.filter(company_id=id)
    unique = modules.values('booking').annotate(dcount=Count('booking'))
    for item in unique:
        bookingid = item['booking']
        try:
            BookingTable.objects.get(id=bookingid, seenStatus=False)
            bookingtableinstancecount = bookingtableinstancecount + 1

        except BookingTable.DoesNotExist:
            bookingtableinstancecount = bookingtableinstancecount

    return bookingtableinstancecount


@register.filter(name='day_count')
def day_count(date2, date1):
    """Removes all values of arg from the given string"""
    return (date2 - date1).days


@register.filter(name='add_custom')
def add_custom(value1, value2):
    return value1 + value2


@register.filter(name='sub_custom')
def sub_custom(value1):
    return 100 - int(value1)


@register.filter(name='multiply_custom')
def multiply_custom(m):
    price = m.sub_total
    quantity = m.quantity
    night_count = (m.end_date - m.start_date).days
    total = price * quantity * night_count
    return total


@register.filter(name='total_calc')
def total_calc(module_list):
    total = 0
    for m in module_list:
        total = total + multiply_custom(m)
    return total


@register.filter(name='tax_calc')
def tax_calc(module_list):
    tax = 13
    total = total_calc(module_list)
    tax = (tax * total) / 100
    return tax


@register.filter(name='total_after_tax_calc')
def total_after_tax_calc(module_list):
    after_tax = total_calc(module_list) + tax_calc(module_list)
    return after_tax


@register.filter(name='add_notification')
def add_notification(val1, val2):
    add_notification = val1 + val2
    return add_notification


# percentage completion
@register.filter(name='hotelDetailCompletionPercentage')
def hotelDetailCompletionPercentage(id):
    try:
        hotelInstance = Hotels.objects.get(id=id)
        return hotelInstance.percentage_complete
    except Hotels.DoesNotExist:
        return 0
    except AttributeError:
        return 0


@register.filter(name='hotelAddressCompletionPercentage')
def hotelAddressCompletionPercentage(id):
    hotelAddrInstance = HotelAddress.objects.get(hotel=id)
    return hotelAddrInstance.percentage_complete


@register.filter(name='hotelCancellationCompletionPercentage')
def hotelCancellationCompletionPercentage(id):
    try:
        hotelCancelInstance = Cancellation_Policy.objects.filter(hotel=id).first()
        return hotelCancelInstance.percentage_complete
    except Cancellation_Policy.DoesNotExist:
        return 0
    except AttributeError:
        return 0


@register.filter(name='hotelBankCompletionPercentage')
def hotelBankCompletionPercentage(id):
    try:
        hotelBankInstance = BankDetail.objects.filter(hotel=id).first()
        return hotelBankInstance.percentage_complete
    except BankDetail.DoesNotExist:
        return 0
    except AttributeError:
        return 0


@register.filter(name='hotelGalleryCompletionPercentage')
def hotelGalleryCompletionPercentage(id):
    try:
        hotelGalleryInstance = HotelGallery.objects.filter(hotel_id=id).first()
        return hotelGalleryInstance.percentage_complete
    except HotelGallery.DoesNotExist:
        return 0
    except AttributeError:
        return 0


@register.filter(name='hotelGalleryAllow')
def hotelGalleryAllow(id):
    try:
        hotelGalleryAllow = HotelGallery.objects.filter(hotel_id=id).first()
        return hotelGalleryAllow.allow
    except HotelGallery.DoesNotExist:
        return 'go'
    except AttributeError:
        return 'go'


@register.filter(name='field_type')
def field_type(field):
    return field.field.widget.__class__.__name__


# shaw included these tags
@register.filter(name='amenityorfeature')
def amenityorfeature(amenity, feature):
    if amenity:
        return 'Amenities'
    if feature:
        return 'Features'

    return 'Rates'


@register.filter(name='propstatus')
def propstatus(status):
    if status == 'pending_approval':
        return ' APPROVAL UNDERPROCESS'
    elif status == 'verified':
        return 'verified'
    elif status == 'active':
        return ' Active'

    return ' Inactive'

# shaw included these tags
