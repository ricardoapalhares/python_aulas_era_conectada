from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import *
from .models import *


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

    return render(request, 'template/form.html', {'form': form})

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

    return render(request, 'template/form.html', {'form': form})    

def especialidade_view(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EspecialidadeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/especialidades')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EspecialidadeForm()

    return render(request, 'template/form.html', {'form': form})    

def nutricionista_view(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NutricionistaForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/nutricionistas')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NutricionistaForm()

    return render(request, 'template/form.html', {'form': form})    

def consulta_view(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ConsultaForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/consultas')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ConsultaForm()

    return render(request, 'template/form.html', {'form': form})    

def avaliacao_view(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AvaliacaoForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/avaliacoes')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AvaliacaoForm()

    return render(request, 'template/form.html', {'form': form})    
