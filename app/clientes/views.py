from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import cliente
from .forms import AddClienteForm, EditClienteForm
from django.contrib import messages
# Create your views here.

@login_required
def cliente_views(request):
    Cliente = cliente.objects.all()
    form_personal = AddClienteForm
    form_editar = EditClienteForm
    context = {
        'cliente' : Cliente,
        'form_personal' : form_personal,
        'form_editar' : form_editar
    }
    return render(request, 'clientes.html',context)

def add_cliente_views(request):
    if request.POST:
        form = AddClienteForm(request.POST,request.FILES)
        if form.is_valid:
            try:
                form.save()
            except:
                messages(request,"Error al guardar el Cliente")
                return redirect('clientes')
    return redirect('clientes')

def edit_cliente_views(request):
    if request.POST:
        Cliente = cliente.objects.get(pk=request.POST.get('id_personal_editar'))
        form = EditClienteForm(request.POST,request.FILES,instance=Cliente)
        if form.is_valid:
            form.save()
    return redirect('clientes')

def delete_cliente_views(request):
    if request.POST:
        Cliente= cliente.objects.get(pk=request.POST.get('id_personal_eliminar'))
        Cliente.delete()
    return redirect('clientes')