from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import ingresos
from .forms import AddIngresoForm, EditIngresoForm
from django.contrib import messages
# Create your views here.

@login_required
def ingresos_views(request):
    Ingreso = ingresos.objects.all()
    form_personal = AddIngresoForm
    form_editar = EditIngresoForm
    context = {
        'Ingresos': Ingreso,
        'form_personal' : form_personal,
        'form_editar' : form_editar
    }
    return render(request, 'ingresos.html',context)

def add_ingresos_views(request):
    if request.POST:
        form = AddIngresoForm(request.POST,request.FILES)
        if form.is_valid:
            try:
                form.save()
            except:
                messages(request,"Error al guardar el ingreso")
                return redirect('Ingresos')
    return redirect('Ingresos')

def edit_ingresos_views(request):
    if request.POST:
        Ingreso = ingresos.objects.get(pk=request.POST.get('id_personal_editar'))
        form = EditIngresoForm(request.POST,request.FILES,instance=Ingreso)
        if form.is_valid:
            form.save()
    return redirect('Ingresos')

def delete_ingresos_views(request):
    if request.POST:
        Ingreso = ingresos.objects.get(pk=request.POST.get('id_personal_eliminar'))
        Ingreso.delete()
    return redirect('Ingresos')