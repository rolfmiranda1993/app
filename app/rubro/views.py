from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from rubro.models import rubro
from .forms import AddRubroForm, EditRubroForm
from django.contrib import messages

# Create your views here.

@login_required
def rubros_views(request):
    Rubros = rubro.objects.all()
    form_personal = AddRubroForm()
    form_editar = EditRubroForm()
    context = {
        'rubros': Rubros,
        'form_personal': form_personal,
        'form_editar': form_editar
    }
    return render(request, 'rubros.html',context)

def add_rubros_views(request):
    if request.POST:
        form = AddRubroForm(request.POST, request.FILES)
        if form.is_valid:
            try:
                form.save()
            except:
                messages(request, "Error al guardar el Rubro")
                return redirect('Rubros')
    return redirect('Rubros')

def edit_rubros_views(request):
    if request.POST:
        rubros = rubro.objects.get(pk=request.POST.get('id_personal_editar'))
        form = EditRubroForm(request.POST,request.FILES,instance=rubros)
        if form.is_valid:
            form.save()
    return redirect('Rubros')

def delete_rubros_views(request):
    if request.POST:
        rubros = rubro.objects.get(pk=request.POST.get('id_personal_eliminar'))
        rubros.delete()
    return redirect('Rubros')