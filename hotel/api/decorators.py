from django.core.exceptions import PermissionDenied

from account.staff_profile.models import StaffProfile
from hotel.models import Hotels
from hotel.staff.models import HotelStaff

def check_auth_token(function):
    def wrap(request, *args, **kwargs):
        entry = Hotels.objects.get(pk=kwargs['pk'])
        userko_id = request.user.id
        usertmp = request.user.account_type.all()
        for user in usertmp:
            if (user.type == 'hotel_owner' and entry.owner_id_id == request.user.id):
                return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    return wrap

