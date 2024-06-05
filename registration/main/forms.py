from .models import Patients
from django.forms import ModelForm, Form, TextInput, EmailInput, DateInput, CharField


class PatientsForm(ModelForm):
    class Meta:
        model = Patients
        fields = ['last_name', 'first_name', 'middle_name',
                  'email', 'phone',
                  'address', 'birth_date']
        widgets = {
            "last_name": TextInput(attrs={
                "id": "lastname",
                "placeholder": "Иванов",
                "required": True,
                "pattern": "^[а-яА-ЯёЁa-zA-Z]+[\s\-]?$",
                "minlength": "2",
                "maxlength": "50"
            }),
            "first_name": TextInput(attrs={
                "id": "name",
                "placeholder": "Иван",
                "required": True,
                "pattern": "^[а-яА-ЯёЁa-zA-Z]+$",
                "maxlength": "50"
            }),
            "middle_name": TextInput(attrs={
                "id": "middlename",
                "placeholder": "Иванович",
                "pattern": "^[а-яА-ЯёЁa-zA-Z]+$",
                "minlength": "2",
                "maxlength": "50"
            }),
            "email": EmailInput(attrs={
                "id": "email",
                "placeholder": "example@eg.com",
                "maxlength": "254"
            }),
            "phone": TextInput(attrs={
                "id": "phone",
                "placeholder": "+7(123) 456-78-90",
                "required": True,
                "pattern": "^[\w\.-]+@[\w\.-]+\.\w+$",
                "minlength": "11",
                "maxlength": "15"
            }),
            "address": TextInput(attrs={
                "id": "address",
                "placeholder": "Город, улица, дом, квартира",
                "required": True,
                "pattern": "^[а-яА-ЯёЁa-zA-Z]+,\s?[а-яА-ЯёЁa-zA-Z]+\s?\w*,\s?\d+[а-яА-Яa-zA-Z]?,\s?\d+$",
                "minlength": "12",
                "maxlength": "254"
            }),
            "birth_date": DateInput(attrs={
                "type": "date",
                "id": "birthdate",
                "required": True,
                "min": "1900-01-01"
            }),
        }


class SearchForm(Form):
    query = CharField(max_length=200,
                      widget=TextInput(attrs={
                        "id": "patient-name",
                        "placeholder": "Фамилия | Имя | Отчество",
                        "required": True,
                        "style": "text-align: center",
                      }))