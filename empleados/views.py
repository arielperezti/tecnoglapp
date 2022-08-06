from wsgiref.util import request_uri
from django.shortcuts import render
from django.http import HttpResponse
from .models import Empleado
from jinja2 import Template
from django.contrib.auth.decorators import login_required #Para hacer obligatorio el inicio de sesion

# Create your views here.

@login_required(login_url='/account/login/') #Para cargar la vista, se requiere validacion

def index(request):
    empleados= Empleado.objects.all()
    data={'empleados':empleados}
    return render(request,'empleados/index.html',data)

@login_required(login_url='/account/login/') 
def nuevoEmpleado(request):
     empleados=Empleado.objects.all()
     data={'empleados':empleados}
     if request.method=='POST':
         #Recibe y guarda
        empleado=Empleado() # crea un obj de empleado
        empleado.nombre=request.POST.get('nombre')
        empleado.apellido=request.POST.get('apellido')
        empleado.cedula=request.POST.get('cedula')
        empleado.fechaNac=request.POST.get('fechanac')
        empleado.email=request.POST.get('email')
        empleado.telefono=request.POST.get('telefono')
        
        
      
        #Guarda en la BD
        empleado.save()
    
        data['msg']='Empleado registrado con éxito!'#adiciona una clave y valor al diccionario
        
     return render(request,'empleados/add.html',data)

@login_required(login_url='/account/login/') 
def modificarEmpleado(request,id):

     empleados = Empleado.objects.filter(id=id).first() 
     template = Template("{{date.strftime('%Y-%m-%d')}}")
     formated_date = template.render(date=empleados.fechaNac)
     empleados.fechaNac = formated_date
     
     data={'empleados':empleados}

     if request.method=='POST':
        
         #Recibe y guarda
         id=request.POST.get('idempleado')
         empleado=Empleado.objects.filter(id=id).first()
         empleado.nombre=request.POST.get('nombre')
         empleado.apellido=request.POST.get('apellido')
         empleado.cedula=request.POST.get('cedula')
         empleado.fechaNac=request.POST.get('fechanac')
         empleado.email=request.POST.get('email')
         empleado.telefono=request.POST.get('telefono')
        
        #Guarda en la BD
         empleado.save()
         data['msg']='Empleado modificado con éxito!'#adiciona una clave y valor al diccionario
     return render(request,'empleados/edit.html',data)

@login_required(login_url='/account/login/') 
def eliminarEmpleado(request,id):
    estado=Empleado.objects.filter(id=id).delete()
    empleados=Empleado.objects.all() 
    data={'empleados':empleados}
    print('Estado = ',estado)
    if estado:
        data['msg']='Empleado ha sido eliminado '
        
    return render(request,'empleados/index.html',data)   

