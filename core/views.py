from .models import Engineeer
from django.shortcuts import render, redirect
from .models import Engineeer, Material
from .forms import EngineerForm, MateralForm


def index(request):
    return render(request, 'index.html')


def list_engineer(request):
    engineers = Engineeer.objects.all()
    return render(request, 'engineer/engineers.html', {'engineers': engineers})


def create_engineer(request):
    form = EngineerForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('engineers')

    return render(request, 'engineer/engineer_form.html', {'form': form})


def update_engineer(request, id):
    engineer = Engineeer.objects.get(id=id)
    form = EngineerForm(request.POST or None, instance=engineer)

    if form.is_valid():
        form.save()
        return redirect('engineers')

    return render(request, 'engineer/engineer_form.html', {'form': form, 'engineer': engineer})


def delete_engineer(request, id):
    engineer = Engineeer.objects.get(id=id)

    if request.method == 'POST':
        engineer.delete()
        return redirect('engineers')

    return render(request, 'engineer/engineer_delete.html', {'engineer': engineer})

#-----------------------materials--------------------#
def list_material(request):
    materials = Material.objects.all()
    return render(request, 'material/materials.html', {'materials': materials})


def create_material(request):
    form = MateralForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('materials')

    return render(request, 'material/material_form.html', {'form': form})


def update_material(request, id):
    material = Material.objects.get(id=id)
    form = MateralForm(request.POST or None, instance=material)

    if form.is_valid():
        form.save()
        return redirect('materials')

    return render(request, 'material/material_form.html', {'form': form, 'material': material})


def delete_material(request, id):
    material = Material.objects.get(id=id)

    if request.method == 'POST':
        material.delete()
        return redirect('materials')

    return render(request, 'material/material_delete.html', {'material': material})