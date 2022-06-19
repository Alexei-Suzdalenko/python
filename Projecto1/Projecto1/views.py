from pipes import Template
from django.http import HttpResponse
import datetime
from django.template import Template, Context

def start_page(request):    # primera vista
    doc_externo = open('C:/__ANDROID_WORK_SUZDALENKO_ALEXEI/python/Projecto1/Projecto1/templates/start.html')
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    documento = plt.render(ctx)
    
    return HttpResponse(documento)

def dame_fecha(request):    
    doc_externo = open('C:/__ANDROID_WORK_SUZDALENKO_ALEXEI/python/Projecto1/Projecto1/templates/fecha.html')
    plt = Template(doc_externo.read())
    doc_externo.close()

    name = 'alexei'; email = 'saron.alexei';
    ctx = Context({'name' : name, 'email' : email})
    documento = plt.render(ctx)
    return HttpResponse(documento)    

def calcAge(request, id):
    more = '<a href="http://127.0.0.1:8000/start/">index page</a><br>'
    return HttpResponse(more + ' id = ' + str(id))  

def two(request, x, y):
    return HttpResponse(' x = ' + str(x) + ' y = ' + str(y)) 

