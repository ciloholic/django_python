from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse

@login_required
def index(request):
    histories = ['update_file', 'update_file', 'download_file']
    context = {'title': 'トップ', 'site_title': 'ユーザサイト', 'histories': histories}
    return render(request, 'app/index.html', context)
