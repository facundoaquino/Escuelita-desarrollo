from django.shortcuts import render
from django.http import HttpResponse
from bdlogueo.models import UsuariosBO
from bdlogueo.models import *

# # # # Create your views here.
def loguin(request):
    return render(request,'index.html')
     # logueo=UsariosBO{"log":log}
      # if request.POST['usuario']=={logueo.usuario} ^ request.POST['contrasena']== {logueo.contraseña}:
    #     return render('Inicio.html')
     # else:
    #return HttpResponse('Usted no puede ingresar')

def ingresarUs(request,usuario,contrasena,oblea,legajo):
    return HttpResponse('hola')
    # us= ingresarUs.object.all()
    # us= UsuariosBO(usuario='usuario',contrasena='contrasena',oblea='oblea',legajo='legajo')
    # us= UsariosBO(usuario=request.POST['usuario'],contrasena=request.POST['contrasena'],oblea=request.POST['oblea'],legajo=request.POST['legajo'])
    # us.save()

    # request HttpResponse(f'Ha ingresado a con nuevo usuario')