from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from mi_app.models import familia, Juego, Auto
from mi_app.forms import Cargar_juego, Cargar_familiar, Cargar_auto
from django.template import loader



def listar_familia (request):
    context = {}
    context ["familia"] = familia.objects.all()

    return render(request, "mi_app/lista_familia.html", context)


def listar_juegos (request):
    context = {}
    context ["juegos"] = Juego.objects.all()  #Tengo que poner el mismo nombre que en el html

    return render(request, "mi_app/lista_juego.html", context)


def listar_autos (request):
    context = {}
    context ["autos"] = Auto.objects.all()  #Tengo que poner el mismo nombre que en el html

    return render(request, "mi_app/lista_auto.html", context)




def instanciar_juegos(request):

    if request.method == 'POST':

        miFormulario = Cargar_juego(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            juego = Juego (nombre=informacion['nombre'], max_jugadores=informacion['max_jugadores'], min_edad=informacion['min_edad'])

            juego.save()

            return render(request, "mi_app/base.html")

    else:

        miFormulario = Cargar_juego() #Formulario vacío para construir el html
    
    return render(request, "mi_app/instanciar_juego.html", {"miFormulario":miFormulario})


def instanciar_familiar(request):

    if request.method == 'POST':

        Form_Familia = Cargar_familiar(request.POST)

        print(Form_Familia)

        if Form_Familia.is_valid:

            informacion = Form_Familia.cleaned_data

            familiar = familia (nombre=informacion['nombre'], apellido=informacion['apellido'], edad=informacion['edad'])

            familiar.save()

            return render(request, "mi_app/base.html")

    else:

        Form_Familia = Cargar_familiar() #Formulario vacío para construir el html
    
    return render(request, "mi_app/instanciar_familiar.html", {"Form_Familia":Form_Familia})


def instanciar_auto(request):

    if request.method == 'POST':

        Form_Auto = Cargar_auto(request.POST)

        print(Form_Auto)

        if Form_Auto.is_valid:

            informacion = Form_Auto.cleaned_data

            auto = Auto (marca=informacion['marca'], modelo=informacion['modelo'], año=informacion['año'])

            auto.save()

            return render(request, "mi_app/base.html")

    else:

        Form_Auto = Cargar_auto() #Formulario vacío para construir el html
    
    return render(request, "mi_app/instanciar_auto.html", {"Form_Auto":Form_Auto})


def buscar_juego(request):
    context = { }

    if request.GET:   #Si el formulario tiene información busca (true), sino no entra en el if

        variable = request.GET["juego"] #Aca estoy metiendo en la variable, el valor que se ingresó en el formulario
        filtro = Juego.objects.filter(nombre__icontains = variable)

        context = {"buscados" : filtro}   #buscados es el nombre que tiene que coincidir con el html

    plantilla = loader.get_template("mi_app/buscar_juego.html")
    documento = plantilla.render (context)

    return HttpResponse (documento)
    


   

