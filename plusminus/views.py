from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import generic
from django.template import loader, RequestContext
from django.contrib import messages

from .models import Player

def index(request):
    template = loader.get_template("plusminus/index.html")
    return HttpResponse(template.render())

def results(request): 
    name = request.POST.get('name')
    fgm = int(request.POST.get('fgm'))
    fga = int(request.POST.get('fga'))
    if fga <= 0:
        return HttpResponse("Since you made no field goal attempts, your Field Goal Percentage is 0%.")

    fgp = fgm/fga*100

    if (fgp > 100):
        return HttpResponse("You made more shots than your attempts. That's impossible. Try again.")
    else:        
        return HttpResponse("%s attempted %d shots and made %d of them. \nThe Field Goal Percentage: %d%%." % (name, fga, fgm, fgp))