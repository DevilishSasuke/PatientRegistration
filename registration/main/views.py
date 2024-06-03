from django.shortcuts import render, redirect
from .models import Patients
from .forms import PatientsForm


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
            return redirect('/')

    form = PatientsForm()

    data = {'title': 'Регистрация',
            'header': 'Регистрация пациента',
            'form': form}

    return render(request, 'register/register.html', data)


def change(request):
    patients = Patients.objects.all().order_by('last_name', 'first_name', 'middle_name')
    form = PatientsForm()
    return render(request, 'change/change.html',
                  {'patients': patients,
                   'form': form,
                   'title': 'Данные пациента',
                   'header': 'Изменение данных пациента'})
