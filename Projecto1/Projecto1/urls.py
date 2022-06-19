from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from Projecto1.controllers import start_page, dame_fecha, calcAge,two,super_contr


urlpatterns = [
    path('admin/', admin.site.urls),
    path('start/', start_page),
    path('fecha/', dame_fecha),         # http://127.0.0.1:8000/fecha
    path('id/<str:id>', calcAge),       # http://127.0.0.1:8000/id/ijijijiji
    path('two/<str:x>/<str:y>', two),   # http://127.0.0.1:8000/two/a/b
    path('super/', super_contr),        # http://127.0.0.1:8000/two/a/b


    
]
