from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render
import datetime

#Constructor de la clase
class Persona(object):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

def saludo(request): # primera vista

    '''
    template = loader.get_template('saludo.html')
    
    ctx = {"name":p1.name,"surname":p1.surname, "date" : fechaActual, "frameworks": frameworks }
    documento = template.render(ctx)
    '''
    p1 = Persona("Manuel","Leon Godinho")   
    fechaActual = datetime.datetime.now()
    frameworks = ["Django", "Flask", "Spring", "Symfony", "Laravel"]
    return render(request,'saludo.html',{"name":p1.name,"surname":p1.surname, "date" : fechaActual, "frameworks": frameworks })
    #return HttpResponse(documento)

def java (request):
    fechaActual = datetime.datetime.now()
    return render(request,'cursoJava.html',{"date" : fechaActual })

def adios(request): # primera vista
    return HttpResponse("<h1>Hasta luego con Django")

def currentTime(request):
    fechaActual = datetime.datetime.now()
    fecha = """<html>
    <h1>
    Fecha y hora actual: %s 
    </h1>
    </html>""" % fechaActual
    return HttpResponse(fecha)

def calcAge(request, age, year):
    yearUrl = year-2020
    futureAge = age + yearUrl
    fecha = """<html>
        <h1>
        En el año %s tendras %s años.
        </h1>
        </html>""" % (year, futureAge)
    return HttpResponse(fecha)

