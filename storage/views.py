from django.db.models import ProtectedError
from django.shortcuts import render, redirect, get_object_or_404
from .models import Machine, Staff, Storage
from django.http import HttpResponseRedirect, HttpResponse
from .forms import StaffCreationForm, StorageCreationFrom, MachineCreationForm


def index(request):
    objects = Machine.objects.all()
    date = {
        "objects": objects,
    }
    return render(request, 'index.html', date)


def delete_item(request, pk):
    obj = Machine.objects.get(id=pk)
    obj.delete()
    return HttpResponseRedirect('/')


def add_staff(request):
    form = StaffCreationForm
    if request.method == "POST":
        form = StaffCreationForm(request.POST)
        if form.is_valid():
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            storage = Storage.objects.get(id=request.POST['storage'])
            staff = Staff(
                first_name=first_name,
                last_name=last_name,
                storage=storage,
            )
            staff.save()
            return redirect('home')
    data = {
        "form": form,
    }
    return render(request, 'staff.html', data)


def add_storage(request):
    form = StorageCreationFrom
    if request.method == "POST":
        form = StorageCreationFrom(request.POST)
        if form.is_valid():
            name = request.POST['name']
            stor = Storage(name=name)
            stor.save()
            return redirect('home')
    data = {
        "form": form,
    }
    return render(request, 'storage.html', data)


def delete_storage(request, pk):
    stor = Storage.objects.get(id=pk)
    try:
        stor.delete()
    except ProtectedError:
        return HttpResponse('Сначала необходимо перенаправить работников на другой склад')

    return HttpResponseRedirect('/')


def add_machine(request):
    form = MachineCreationForm()
    if request.method == "POST":
        form = MachineCreationForm(request.POST)
        if form.is_valid():
            maker = request.POST['maker']
            country = request.POST['country']
            type1 = request.POST['type']
            answerable = Staff.objects.get(id=request.POST['answerable'])
            machine = Machine(maker=maker, country=country, type=type1, answerable=answerable)
            machine.save()
            return redirect('home')
    data = {
        "form": form,
    }
    return render(request, 'machine.html', data)


def one_storage(request, pk):
    stor = get_object_or_404(Storage, pk=pk)
    objects = Machine.objects.filter(answerable__storage_id=pk)
    data = {
        "objects": objects,
        "stor": stor,
    }
    return render(request, 'one_storage.html', data)
