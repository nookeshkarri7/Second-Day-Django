from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import datetime

def welcome(request):
    date=datetime.datetime.now()
    hours=int(date.strftime("%H"))
    if hours<12:
        msg="Good morning"
    else:
        msg="good night"

    return HttpResponse(msg+str(hours))
