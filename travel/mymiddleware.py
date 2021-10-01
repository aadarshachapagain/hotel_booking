from django.utils.deprecation import MiddlewareMixin


class MyMiddleware(MiddlewareMixin):
	def process_request(self, request):
		if request.user.is_authenticated:
			absolute_path = request.path
			user_groups = request.user.groups.all()
			permission_list = []
			permission = ''
			for group in user_groups:
				permission = group.permissions.all()
			for per in permission:
				permission_list.append(per.id)
			print("request")
