from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import departamentos
from .forms import AddDepartamentoForm, EditDepartamentoForm



# Create your views here.

@login_required
def departamentos_views(request):
    Dpto = departamentos.objects.all()
    form_personal = AddDepartamentoForm()
    form_editar = EditDepartamentoForm()
    context = {
        'departamentos': Dpto,
        'form_personal' : form_personal,
        'form_editar' : form_editar
    }
    return render(request, 'departamentos.html',context)

def add_departamentos_views(request):
    if request.POST:
        form = AddDepartamentoForm(request.POST,request.FILES)
        if form.is_valid:
            try:
                form.save()
            except:
                messages(request,"Error al guardar la tarea")
                return redirect('departamentos')
    return redirect('departamentos')

def edit_departamentos_views(request):
    if request.POST:
        Dpto = departamentos.objects.get(pk=request.POST.get('id_personal_editar'))
        form = EditDepartamentoForm(request.POST,request.FILES,instance=Dpto)
        if form.is_valid:
            form.save()
    return redirect('departamentos')

def delete_departamentos_views(request):
    if request.POST:
        Dpto = departamentos.objects.get(pk=request.POST.get('id_eliminar_personal'))
        Dpto.delete()
    return redirect('departamentos')

