from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Staff, Storage, Machine


class StaffCreationForm(forms.Form):
    first_name = forms.CharField(label='Имя', max_length=20)
    last_name = forms.CharField(label='Фамилия', max_length=20)
    storage = forms.ModelChoiceField(Storage.objects, label='Склад')

    class Meta:
        model = Staff
        fields = ('first_name', 'last_name', 'storage')


class StorageCreationFrom(forms.Form):
    name = forms.CharField(label='Название нового склада')


class MachineCreationForm(forms.Form):
    maker = forms.CharField(label='Производитель', max_length=200)
    country = forms.CharField(label='Страна производителя', max_length=30)
    type = forms.CharField(label='Модель', max_length=200)
    answerable = forms.ModelChoiceField(label='Ответсвенный кладовщик', queryset=Staff.objects)