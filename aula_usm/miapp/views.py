from django.shortcuts import render
from django.http import HttpResponse
from .models import Entidad, Comunicado
from django.contrib.auth import get_user_model

# Create your views here.




#User = 'get_user_model()'

def index(request):
    title = "Sistema notificaciones usm"

    respuesta = request.GET.get('Departamento')

    entidades = Entidad.objects.all()

    if respuesta == "Departamento" or respuesta is None:
        comunicados = Comunicado.objects.all()
        comunicados = Comunicado.objects.filter(visible=True)
    else:
        filtro = Entidad.objects.get(nombre=respuesta)
        #logo = Entidad.logo.get(logo=respuesta)
        print("filtro: ",filtro.logo)

        comunicados = Comunicado.objects.filter(entidad=filtro).filter(visible=True)

        print("comunicados: ",comunicados)
        
    
    
    data = {
        "title": title,
        "entidades":entidades,
        "comunicados":comunicados,
        "respuesta":respuesta,

        
    }

    return render(request,'miapp/base.html', data)



