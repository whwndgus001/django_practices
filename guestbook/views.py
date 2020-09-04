# from django.http import Httpresponse

from django.shortcuts import render

def index(request):
    return render(request, 'guestbook/index.html')
