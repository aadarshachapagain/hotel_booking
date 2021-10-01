from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render

from account.models import User
from account.owner_profile.models import OwnerProfile
from account.staff_profile.models import StaffProfile


@login_required
def dashboard(request):
    user_id = request.user.id
    user_instance = User.objects.get(id=user_id)
    if request.user.is_superuser == True:
        response = render(request, 'travel/admin_dashboard.html')
        response.set_cookie('current_hotel', 'empty')
        response.set_cookie('current_module', 'empty')
        response.set_cookie('current_company', 'empty')
        response.set_cookie('current_tourpackage', 'empty')
        response.set_cookie('hotel_inventory', 'empty')
        response.set_cookie('current_inventory', 'empty')
        response.set_cookie('current_rental', 'empty')
        return response
    context = {
        'account_types': user_instance.account_type.filter(),
    }

    acc_types = user_instance.account_type.filter()
    for acc_type in acc_types:
        if 'owner' in acc_type.type:
            print('user_id')
            print(user_id)
            profile = OwnerProfile.objects.get(user_id=user_id)
            if profile.name:
                return render(request, 'travel/user_dashboard.html', context)
            else:
                # return redirect('ownerprofileupdate', user_id)
                return redirect('OwnerNPropertyDetail')
            # return redirect('ownerprofileupdate', user_id)
        else:
            profile = StaffProfile.objects.get(user_id=user_id)
            if profile.name:
                # print(profile)
                return render(request, 'travel/user_dashboard.html', context)
            else:
                return redirect('staffupdate', user_id)


# for account_type in account_types:


def current_module(request, module_name):
    User.objects.filter(id=request.user.id).update(current_module=module_name)
    # return after cookie is set
    if module_name == 'hotel':
        response = redirect('hotel:hotelselect')
        response.set_cookie('current_module', module_name)
        return response


# elif module_name == 'travel_tour':
# 	# return redirect('travel_tour:tourcompanyindex')
# 	response = redirect('travel_tour:travelselect')
# 	response.set_cookie('current_module', module_name)
# 	return response
# elif module_name == 'rental':
# 	# return redirect('travel_tour:tourcompanyindex')
# 	response = redirect('rental:rentalselect')
# 	response.set_cookie('current_module', module_name)
# 	return response
# elif module_name == 'restaurant':
# 	# return redirect('travel_tour:tourcompanyindex')
# 	response = redirect('restaurant:restaurantselect')
# 	response.set_cookie('current_module', module_name)
# 	return response


def check_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return redirect('login')


def error(request):
    return render(request, 'travel/404error.html')


#
def forbidden(request):
    return render(request, 'registration/403.html')


def handler404(request, *args, **argv):
    response = render(request, 'travel/404error.html')
    response.status_code = 404
    return response


def handler403(request, *args, **argv):
    response = render(request, 'registration/403.html')
    response.status_code = 403
    return response


def termsandconditions(request):
    return render(request, 'travel/terms_conditions.html')


def checkEmail(request):
    return render(request, 'registration/checkEmail.html')
