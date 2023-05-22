import datetime
from django.http import HttpResponse
from django.template import Template, Context
from .models import models
from django.shortcuts import render

def my_view(request):
    records = models.LynxHistorical.objects.all()  # or use a filter if you don't want all records
    return render(request, 'template1.html', {'records': records})

def tablaTest(request):

    altFile = open("/Users/robot314/IdeaProjects/lynxkpi/lynxportal/lynxportal/templates/template1.html")

    plt = Template(altFile.read())
    altFile.close()
    ctx = Context()

    documento = plt.render(ctx)

    return HttpResponse(documento)

def tiempoFecha(request):

    fechaActual = datetime.datetime.now()

    return HttpResponse(fechaActual)
