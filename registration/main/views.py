from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Patients
from .forms import PatientsForm
from .forms import SearchForm
import time


# Create your views here.
def main_page(request):
    return render(request, 'main/index.html',
                  {'title': 'Главная страница',
                   'header': 'Главная страница'})


def register(request):
    if request.method == 'POST':
        form = PatientsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/success')

    form = PatientsForm()
    data = {'title': 'Регистрация',
            'header': 'Регистрация пациента',
            'form': form}

    return render(request, 'register/register.html', data)


def change(request):
    searchForm = SearchForm()
    patients = Patients.objects.all().order_by('last_name', 'first_name', 'middle_name')

    query = None
    results = []
    if 'query' in request.GET:
        pageForm = SearchForm(request.GET)
        if pageForm.is_valid():
            query = pageForm.cleaned_data['query']
            query = query.lower()
            for patient in patients:
                if (query in patient.first_name.lower() or
                        query in patient.last_name.lower() or
                        query in patient.middle_name.lower()):
                    results.append(patient)
    else:
        pageForm = SearchForm()

    return render(request, 'change/change.html',
                  {'patients': patients,
                   'searchForm': searchForm,
                   'pageForm': pageForm,
                   'query': query,
                   'results': results,
                   'title': 'Данные пациента',
                   'header': 'Изменение данных пациента'})


def success(request):
    return render(request, 'main/success.html')