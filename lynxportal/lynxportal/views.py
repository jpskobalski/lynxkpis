import datetime
from django.http import HttpResponse
from django.template import Template, Context
from .models import models
from django.shortcuts import render
from django.db.models import Max, Sum

def my_view(request):
    # Get the current year
    current_year = datetime.datetime.now().year
    latest_timestamp = models.LynxHistorical.objects.aggregate(Max('timestamp'))['timestamp__max']

    if latest_timestamp is not None:
        # Filter for records from the latest timestamp and op_closedate year 2023
        records = models.LynxHistorical.objects.filter(
            timestamp=latest_timestamp,
            op_closedate__year=current_year,
            op_finalweight__isnull=False
        ).values('op_closedate__month').annotate(total_weight=Sum('op_finalweight')).order_by('op_closedate__month')

        timestamps = [record['op_closedate__month'] for record in records]
        weights = [record['total_weight'] for record in records]
    else:
        timestamps = []
        weights = []

    return render(request, 'template1.html', {'timestamp': timestamps, 'OP_FinalWeight': weights})
    # records = models.LynxHistorical.objects.all()  # or use a filter if you don't want all records
    # return render(request, 'template1.html', {'records': records})

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
