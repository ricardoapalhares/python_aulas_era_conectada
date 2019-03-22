from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import PacienteForm, DietaForm

def paciente_view(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PacienteForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/pacientes')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PacienteForm()

    return render(request, 'template/paciente.html', {'form': form})

def dieta_view(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DietaForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/dietas')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DietaForm()

    return render(request, 'template/dieta.html', {'form': form})    