# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
from models import Tabla
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def server(request):
    verb = request.method
    recurso = request.path

    if verb == 'GET':
        if recurso == '/':
             return HttpResponse("<h1>Insertar en el put con el siguiente formato:</h1>"
                                +"<p>nombre,fecha(YYYY-MM-DD)</p>")
        else:
            try:
                print Tabla.objects.all()
                record = Tabla.objects.get(nombre = recurso[1:])
                return HttpResponse("<p>Fecha de "+recurso[1:]+"= "+ str(record.fecha) +"</p>")
            except Tabla.DoesNotExist:
                return HttpResponseNotFound("Page not found: %s." % recurso[1:])

    elif verb == 'PUT':
        cuerpo = request.body.split(',')
        name = cuerpo[0]
        date = cuerpo[1]
        db = Tabla(nombre = name,fecha = date)
        db.save()
        return HttpResponse('<h1>Nombre y fecha almacenados</h1>')
