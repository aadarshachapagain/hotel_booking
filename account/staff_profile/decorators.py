from django.core.exceptions import PermissionDenied
from hotel.staff.models import HotelStaff


def staff_create_decorator(function):
    def wrap(request, *args, **kwargs):
        usertmp = request.user.account_type.all()
        for user in usertmp:
            if user.type=='hotel_owner':
                    return function(request, *args, **kwargs)
            else:
                raise PermissionDenied
    return wrap

def staff_update_decorator(function):
    def wrap(request, *args, **kwargs):
        entry = HotelStaff.objects.get(pk=kwargs['pk'])
        usertmp = request.user.account_type.all()
        print(usertmp)
        for user in usertmp:
            print('1')
            if user.type=='hotel_owner' or (user.type=='hotel_staff' and request.user.id==entry.user_id):
                return function(request, *args, **kwargs)
        raise PermissionDenied
    return wrap

def hotel_ownercreate_decorator(function):
    def wrap(request, *args, **kwargs):        
        if request.user.is_superuser:
            return function(request, *args, **kwargs)         
        else:
            raise PermissionDenied
    return wrap

