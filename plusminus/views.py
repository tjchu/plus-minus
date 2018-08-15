from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import generic
from django.template import loader, RequestContext
from django.contrib import messages

from .models import Player

def index(request):
    template = loader.get_template("plusminus/index.html")
    return HttpResponse(template.render())

"""
def get_stats(request, fga, fgm):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = StatsForm(request.POST, fga=fga, fgm=fgm)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            request.session['fga'] = form.fga
            request.session['fgm'] = form.fgm
            return HttpResponseRedirect('/results/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = StatsForm(fga=fga, fgm=fgm)
"""

def results(request): 
    fgm = int(request.POST.get('fgm'))
    fga = int(request.POST.get('fga'))
    if fga <= 0:
        return HttpResponse("Since you made no field goal attempts, your Field Goal Percentage is 0%.")

    fgp = fgm/fga*100

    if (fgp > 100):
        return HttpResponse("You made more shots than your attempts. That's impossible. Try again.")
    else:        
        return HttpResponse("You attempted %d shots and made %d of them. Your Field Goal Percentage: %d%%." % (fga, fgm, fgp))