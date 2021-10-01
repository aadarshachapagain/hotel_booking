import functools

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect

from account.staff_profile.models import StaffProfile
from hotel.models import Hotels
from hotel.staff.models import HotelStaff
from rest_framework.authtoken.models import Token
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash,
)

def hotel_delete_decorator(function):
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


def hotel_update_decorator(function):
    def wrap(request, *args, **kwargs):
        entry = Hotels.objects.get(pk=kwargs['pk'])
        userko_id = request.user.id
        usertmp = request.user.account_type.all()
        if(request.user.is_superuser):
            return function(request, *args, **kwargs)
        else:
            for user in usertmp:
                if (user.type == 'hotel_owner' and entry.owner_id_id == request.user.id):
                    return function(request, *args, **kwargs)
            else:
                raise PermissionDenied
    return wrap


def hotel_create_decorator(function):
    def wrap(request, *args, **kwargs):
        allusers = request.user.account_type.all()
        for user in allusers:
            if user.type == "hotel_owner":
                return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    return wrap


def check_logged_in(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            return function(request, *args, **kwargs)

    return wrap


def acl_decorator(model, method):
    def decorator(function):
        def wrapper(request,*args, **kwargs):
            result = function(request,*args, **kwargs)
            user_groups = request.user.groups.all()
            group_permission_list = []
            model_permission_list = []
            permission = ''
            for group in user_groups:
                permission = group.permissions.all()
            user_individual_permission = request.user.user_permissions.all()
            for per1 in permission:
                group_permission_list.append(per1.id)
                
            for per2 in user_individual_permission:
                if per2.id not in group_permission_list:
                    group_permission_list.append(per2.id)
            
            content_type = ContentType.objects.get_for_model(model)
            all_permissions = Permission.objects.filter(content_type=content_type, codename__icontains=method)
            for per3 in all_permissions:
                model_permission_list.append(per3.id)
                
            group_permission_list = set(group_permission_list)
            model_permission_list = set(model_permission_list)
            intersection = model_permission_list.intersection(group_permission_list)
            if intersection:
                return result
            else:
                raise PermissionDenied
        return wrapper
    return decorator



def is_superuser(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_superuser:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    return wrap



