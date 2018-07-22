from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
import datetime

@login_required
def index(request):
    histories = [
        {'timestamp': datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'), 'name': 'update_file'},
        {'timestamp': datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'), 'name': 'update_file'},
        {'timestamp': datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'), 'name': 'download_file'},
    ]
    context = {'title': 'トップ', 'site_title': 'ユーザサイト', 'histories': histories}
    return render(request, 'app/index.html', context)
