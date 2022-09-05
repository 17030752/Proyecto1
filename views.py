from pydoc import doc
from django.http import HttpResponse
import datetime
from django.template import loader #cargador de plantillas
from django.shortcuts import render #forma aun mas corta de cargar plantillas
from django.template import Template, Context
def saludo(request):
    docHTML =open('/home/david/Documentos/PYTHON/Proyecto1/Proyecto1/templates/saludo_template.html')
    template = Template(docHTML.read())
    docHTML.close()
    context = Context()
    renderHTML = template.render(context)
    return HttpResponse(renderHTML)
def fechaActual(request):
    fecha = datetime.datetime.now()
    listFechas=["16 de septiembre","21 noviembre"]
    """ TODO ESTO SE AHORRA CON EL CARGADOR DE PLANTILLAS loader
    docHTML = open('/home/david/Documentos/PYTHON/Proyecto1/Proyecto1/templates/fecha_actual_template.html')
    template = Template(docHTML.read())
    docHTML.close()
    """
    #con render de shorcuts podemos comentar ahora el loader
    #template = loader.get_template('fecha_actual_template.html')

    """ SE QUITA ESTO CUANDO SE USA loader , se pasa directo el diccionario
    context = Context({
        "fecha":fecha,
        "feriados":listFechas
    })"""
    #con render de shorcuts podemos comentar esto
    """render = template.render({
        "fecha":fecha,
        "feriados":listFechas
    })"""
    #htmlTag="""%s""" % fecha #se llama marcadores de posicion, repasar
    #con render de shorcuts el return no usa HttpResponse , si no render(request,nombre_plantilla,contexto==diccionario)
    #return HttpResponse(render)
    context={
    "fecha":fecha,
    "feriados":listFechas
    }
    return render( request,'fecha_actual_template.html',context)
def edadFutura(request,age,year):
    currentYears = datetime.datetime.now().year - age
    print(currentYears)
    period = year - datetime.datetime.now().year
    print(period)
    futureAge=0
    futureAge = currentYears + period
    html ="""
    <html>
    <body>
    <h2>
    En el año %s tendras: %s
    </h2>
    </body>
    </html>
    """ %(year,futureAge) 
    return HttpResponse(html)

