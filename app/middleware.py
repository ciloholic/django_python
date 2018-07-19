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
        allow_actions = ['admin:login', 'admin:logout', 'app:index']
        if not request.user.is_superuser and not action in allow_actions:
            return redirect('app:index')
        response = self.get_response(request)
        return response
