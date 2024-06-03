from django.shortcuts import render
from .models import Patients


# Create your views here.
def main_page(request):
    return render(request, 'main/index.html',
                  {'title': 'Главная страница',
                   'header': 'Главная страница'})


def register(request):
    return render(request, 'register/register.html',
                  {'title': 'Регистрация',
                   'header': 'Регистрация пациента'})


def change(request):
    patients = Patients.objects.all()
    return render(request, 'change/change.html',
                  {'patients': patients,
                   'title': 'Данные пациента',
                   'header': 'Изменение данных пациента'})
