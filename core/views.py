from .models import Engineeer
from django.shortcuts import get_object_or_404, render, redirect

from .models import Engineeer, Material, Project
from .forms import EngineerForm, MateralForm


def index(request):
    return render(request, 'index.html')


def engineer_list(request):
    engineers = Engineeer.objects.all()
    return render(request, 'engineer/engineers.html', {'engineers': engineers})


def engineer_create(request):
    form = EngineerForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('engineers')

    return render(request, 'engineer/engineer_form.html', {'form': form})


def engineer_update(request, id):
    engineer = Engineeer.objects.get(id=id)
    form = EngineerForm(request.POST or None, instance=engineer)

    if form.is_valid():
        form.save()
        return redirect('engineers')

    return render(request, 'engineer/engineer_form.html', {'form': form, 'engineer': engineer})


def engineer_delete(request, id):
    engineer = Engineeer.objects.get(id=id)

    if request.method == 'POST':
        engineer.delete()
        return redirect('engineers')

    return render(request, 'engineer/engineer_delete.html', {'engineer': engineer})


#-----------------------materials--------------------#
def material_list(request):
    materials = Material.objects.all()
    return render(request, 'material/materials.html', {'materials': materials})


def material_create(request):
    form = MateralForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('materials')

    return render(request, 'material/material_form.html', {'form': form})


def material_update(request, id):
    material = Material.objects.get(id=id)
    form = MateralForm(request.POST or None, instance=material)

    if form.is_valid():
        form.save()
        return redirect('materials')

    return render(request, 'material/material_form.html', {'form': form, 'material': material})


def material_delete(request, id):
    material = Material.objects.get(id=id)

    if request.method == 'POST':
        material.delete()
        return redirect('materials')

    return render(request, 'material/material_delete.html', {'material': material})


#-----------------------projects--------------------#
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project/projects.html', {'projects': projects})


def project_create(request):
    engineers = Engineeer.objects.all()
    materials = Material.objects.all()
    if request.method == 'POST':
        project_name = request.POST.get('project_name')
        engineer_id = request.POST.get('engineer_id')
        area = request.POST.get('area')
        bedrooms = request.POST.get('bedrooms')
        bathrooms = request.POST.get('bathrooms')
        floors = request.POST.get('floors')
        materials_selected = request.POST.getlist('materials')
        quantities = request.POST.getlist('quantities')

        project = Project.objects.create(name=project_name, engineer_responsible_id=engineer_id, area=area, 
                                         bedrooms=bedrooms, bathrooms=bathrooms, floors=floors)
        
        subtotal = 0
        for material_id, quantity in zip(materials_selected, quantities):
            material = Material.objects.get(pk=material_id)
            quantity = int(quantity)
            total_value = material.price * quantity
            subtotal += total_value
            project.materials.add(material, through_defaults={'quantity': quantity, 'total_value': total_value})
        
        project.subtotal = subtotal
        project.save()
        return redirect('projects')

    context = {'engineers': engineers, 'materials': materials}
    return render(request, 'project/project_form.html', context)


def project_update(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    engineers = Engineeer.objects.all()
    materials = Material.objects.all()

    if request.method == 'POST':
        project_name = request.POST.get('project_name')
        engineer_id = request.POST.get('engineer_id')
        area = request.POST.get('area')
        bedrooms = request.POST.get('bedrooms')
        bathrooms = request.POST.get('bathrooms')
        floors = request.POST.get('floors')
        materials_selected = request.POST.getlist('materials')
        quantities = request.POST.getlist('quantities')

        project.name = project_name
        project.engineer_responsible_id = engineer_id
        project.area = area
        project.bedrooms = bedrooms
        project.bathrooms = bathrooms
        project.floors = floors
        
        project.materials.clear()  # Remove todos os materiais associados ao projeto

        subtotal = 0
        for material_id, quantity in zip(materials_selected, quantities):
            material = Material.objects.get(pk=material_id)
            quantity = int(quantity)
            total_value = material.price * quantity
            subtotal += total_value
            project.materials.add(material, through_defaults={'quantity': quantity, 'total_value': total_value})

        project.subtotal = subtotal
        project.save()
        return redirect('projects')

    context = {
        'project': project,
        'engineers': engineers,
        'materials': materials,
    }
    return render(request, 'project/project_update.html', context)


def project_delete(request, id):
    project = Project.objects.get(id=id)

    if request.method == 'POST':
        project.delete()
        return redirect('projects')

    return render(request, 'project/project_delete.html', {'project': project})
