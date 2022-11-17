from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from miembro.models import miembro
from miembro.forms import AddMiembroForm, EditMiembroForm
from django.contrib import messages

# Create your views here.
@login_required
def miembro_views(request):
    Miembro = miembro.objects.all()
    form_personal = AddMiembroForm()
    form_editar = EditMiembroForm()
    context = {
    'miembro': Miembro,
    'form_personal' : form_personal,
    'form_editar' : form_editar
    }
    return render(request, 'miembro.html',context)

def add_miembro_views(request):
    if request.POST:
        form = AddMiembroForm(request.POST,request.FILES)
        if form.is_valid:
            try:
                form.save()
            except:
                messages(request, "Error al guardar el Miembro")
                return redirect('miembro')
    return redirect('miembro')

def edit_miembro_views(request):
    if request.POST:
        Miembros = miembro.objects.get(pk=request.POST.get('id_personal_editar'))
        form = EditMiembroForm(request.POST,request.FILES, instance=Miembros)
        if form.is_valid:
            form.save()
    return redirect('miembro')

def delete_miembro_views(request):
    if request.POST:
        Miembro = miembro.objects.get(pk=request.POST.get('id_personal_eliminar'))
        Miembro.delete()
    return redirect('miembro')
