from django.core.exceptions import PermissionDenied
from hotel.inventory.models import HotelInventory


def inventory_detail_decorator(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_superuser:
            return function(request, *args, **kwargs)
        elif request.user:
            inventory_id = kwargs['pk']
            if HotelInventory.objects.filter(user_id=request.user.id, id=inventory_id).exists():
                return function(request, *args, **kwargs)
            else:
                raise PermissionDenied
        else:
            raise PermissionDenied
    return wrap
