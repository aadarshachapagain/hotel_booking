from django.core.exceptions import PermissionDenied


def if_admin_decorator(function):
    def wrap(request, *args, **kwargs):
        if (request.user.is_superuser):
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrap

