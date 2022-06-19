from pipes import Template
from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render


def start_page(request):    # primera vista
    doc_externo = open('C:/__ANDROID_WORK_SUZDALENKO_ALEXEI/python/Projecto1/Projecto1/templates/start.html')
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    documento = plt.render(ctx)
    
    return HttpResponse(documento)

# http://127.0.0.1:8000/fecha/
def dame_fecha(request):    
    doc_externo = loader.get_template('fecha.html')
    documento = doc_externo.render({'name': 'alexei', 'email': 'saron.alexei@gmail.com'})
    return HttpResponse(documento)    

def calcAge(request, id):
    more = '<a href="http://127.0.0.1:8000/start/">index page</a><br>'
    return HttpResponse(more + ' id = ' + str(id))  

def two(request, x, y):
    return HttpResponse(' x = ' + str(x) + ' y = ' + str(y)) 

def super_contr(request):
    data = {'name': 'methodo', 'email': 'avanzado'}
    return render(request, 'fecha.html', data)