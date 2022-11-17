from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import tarea
from .forms import AddTareaForm, EditTareaForm


# Create your views here.
@login_required
def tarea_views(request):
    Tarea = tarea.objects.all()
    form_personal = AddTareaForm()
    form_editar = EditTareaForm()
    context = {
        'tareas': Tarea,
        'form_personal' : form_personal,
        'form_editar' : form_editar
    }
    return render(request, 'tareas.html',context)

def add_tarea_views(request):
    if request.POST:
        form = AddTareaForm(request.POST,request.FILES)
        if form.is_valid:
            try:
                form.save()
            except:
                messages(request,"Error al guardar la tarea")
                return redirect('tareas')
    return redirect('tareas')

def edit_tarea_views(request):
    if request.POST:
        Tarea = tarea.objects.get(pk=request.POST.get('id_personal_editar'))
        form = EditTareaForm(request.POST,request.FILES,instance=Tarea)
        if form.is_valid:
            form.save()
    return redirect('tareas')

def delete_tarea_views(request):
    if request.POST:
        Tarea = tarea.objects.get(pk=request.POST.get('id_personal_eliminar'))
        Tarea.delete()
    return redirect('tareas')
