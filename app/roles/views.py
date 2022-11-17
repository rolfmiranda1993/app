from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from roles.models import roles
from .forms import AddRolesForm,EditRolesForm
from django.contrib import messages
# Create your views here.

@login_required
def roles_views(request):
    Roles = roles.objects.all()
    form_personal = AddRolesForm()
    form_editar = EditRolesForm()
    context = {
        'roles' : Roles,
        'form_personal' : form_personal,
        'form_editar' : form_editar
    }
    return render(request, 'roles.html',context)

def add_roles_views(request):
    if request.POST:
        form = AddRolesForm(request.POST,request.FILES)
        if form.is_valid:
            try:
                form.save()
            except:
                messages(request,"Error al guardar el rol")
                return redirect('roles')
    return redirect('roles')

def edit_roles_views(request):
    if request.POST:
        Roles = roles.objects.get(pk=request.POST.get('id_personal_editar'))
        form = EditRolesForm(request.POST,request.FILES,instace=Roles)
        if form.is_valid:
            form.save()
    return redirect('roles')

def delete_roles_views(request):
    if request.POST:
        Roles = roles.objects.get(pk=request.POST.get('id_personal_eliminar'))
        Roles.delete()
    return redirect('roles')