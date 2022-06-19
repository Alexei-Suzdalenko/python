http://suzdalenko.pythonanywhere.com/ -> admin: alexei.saron@gmail.com


# install and create app
django-admin startproject Projecto1
python manage.py migrate
C:\__ANDROID_WORK_SUZDALENKO_ALEXEI\python\Projecto1> python manage.py runserver
# run server
python manage.py runserver


# run server independient
python -m http.server 5050



# create new project tiendaOnline
1. django-admin startproject tiendaOnline            // creamos nuevo proyecto
2. python manage.py startapp gestionPedidos          // creacion de una aplicacion
3. python manage.py check gestionPedidos             // comprobar que todo va bien
4. python manage.py makemigrations                   // creacion de base datos y migracion modelos   
5. python manage.py sqlmigrate gestionPedidos 0001   // creacion de sql codigo 
6. python manage.py migrate                          // por fin creamos tablas