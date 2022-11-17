from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def usuarios_view(request):
    #Departamentos = departamento.objects.all()
   # context = {
    #    'rubros': Rubros,
   # }
    return render(request, 'usuarios.html')