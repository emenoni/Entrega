from django.shortcuts import render
from django.http import HttpResponse
from mi_app.models import familia


def listar_familia (request):
    context = {}
    context ["familiares"] = familia.objects.all()

    return render(request, "mi_app/lista_familia.html", context)



