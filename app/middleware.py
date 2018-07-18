from django.urls import get_resolver
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

class AdminMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        resolver = get_resolver(None)
        resolver_match = resolver.resolve(request.path_info)
        if not request.user.is_active or not request.user.is_superuser:
            if not resolver_match.url_name in ['login', 'logout', 'home']:
                return HttpResponse('404')
        response = self.get_response(request)
        return response
