from django.urls import get_resolver
from django.http import HttpResponse
from django.shortcuts import redirect

class AdminMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        resolver = get_resolver(None)
        resolver_match = resolver.resolve(request.path_info)
        action = resolver_match.app_names[0] + ':' + resolver_match.url_name
        if not request.user.is_active or not request.user.is_superuser:
            if not action in ['admin:login', 'admin:logout', 'app:index']:
                return redirect('admin:login')
        response = self.get_response(request)
        return response
