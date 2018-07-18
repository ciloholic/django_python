from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse

@login_required
def index(request):
    if request.user.is_superuser:
        return HttpResponse('admin')
    else:
        return HttpResponse('guest')
    # return render(request, 'admin/base_site.html')
