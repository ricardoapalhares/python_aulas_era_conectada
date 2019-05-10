from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import *
from .models import *

def country_view(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CountryForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/countries')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CountryForm()

    return render(request, 'template/form.html', {'form': form})

def mortality_view(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MortalityForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/mortalities')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = MortalityForm()

    return render(request, 'template/form.html', {'form': form})

def mortality_o_view(request):
    mortalities = Mortality.objects.all()
    return render(request, 'template/country.html', {'mortalities': mortalities})

