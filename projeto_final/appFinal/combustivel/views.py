from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import *
from .models import *

def combustivel_view(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CombustivelForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/pacientes')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CombustivelForm()

    return render(request, 'template/form.html', {'form': form})
