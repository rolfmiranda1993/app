from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import egresos
from .forms import AddEgresoForm, EditEgresoForm
from django.contrib import messages

# Create your views here.

@login_required
def egresos_views(request):
    Egreso = egresos.objects.all()
    form_personal = AddEgresoForm
    form_editar = EditEgresoForm
    context = {
        'egresos': Egreso,
        'form_personal' : form_personal,
        'form_editar' : form_editar
    }
    return render(request, 'egresos.html', context)

def add_egresos_views(request):
    if request.POST:
        form = AddEgresoForm(request.POST,request.FILES)
        if form.is_valid:
            try:
                form.save()
            except:
                messages(request,"Error al guardar el egreso")
                return redirect('egresos')
    return redirect('egresos')

def edit_egresos_views(request):
    if request.POST:
        Egreso = egresos.objects.get(pk=request.POST.get('id_personal_editar'))
        form = EditEgresoForm(request.POST,request.FILES,instance=Egreso)
        if form.is_valid:
            form.save()
    return redirect('egresos')

def delete_egresos_views(request):
    if request.POST:
        Egreso = egresos.objects.get(pk=request.POST.get('id_personal_eliminar'))
        Egreso.delete()
    return redirect('egresos')