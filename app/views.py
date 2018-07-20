from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse

@login_required
def index(request):
    context = {'title': 'トップ', 'site_title': 'ユーザサイト'}
    return render(request, 'app/index.html', context)
