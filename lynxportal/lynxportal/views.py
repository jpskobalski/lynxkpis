import datetime
from django.http import HttpResponse
from django.template import Template, Context
from .models.lynxHistorical import LynxHistorical
from django.shortcuts import render
import pandas as pd

# def tablaTest(request):
#     data = pd.DataFrame(list(LynxHistorical.objects.all().values()))
#     return render(request, 'template1.html', {'data': data})
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
