# clon_twitter
Editor online: https://dillinger.io/

## Proyecto basado en el siguiente post:
https://realpython.com/django-social-network-1/

### 1. Setup para el Proyecto Base

Instalo los requirimientos
pip install -r requirement.txt

Creo el proyecto:

django-admin startproject Social . 

Creo la aplicacion
py manage.py startapp tuiter

Registro la aplicacion en settings.py

en INSTALLED_APPS = [] la aplicacion: 
'tuiter.apps.TuiterConfig'

Agrego el idioma español Argentina y el uso horario

LANGUAGE_CODE = 'es-AR'

TIME_ZONE = 'America/Argentina/Buenos_Aires'

Hago las migraciones:

python manage.py migrate

Creo el super usuario:

python manage.py createsuperuser

#### Personalizar el Admin de Django

Para simplificar el django-admin (Edito tuiter/admin.py):

1. No utilizará los Grupos de Django , por lo que puede eliminarlo de su vista de administrador por completo.
2. La forma más básica de crear un usuario en Django es pasar solo un nombre de usuario.
También puede eliminar todos los demás campos de la pantalla del modelo Usuarios .

Quito la entrada "Grupos" del Admin

Modifico los campos del modelo "User", solo muestro el campo "username"

### 2. Extender el modelo User

Se utilizar el modelo User y un modelo para el 'perfil' de un usuario.
Usando una relacion 1 a 1

#### 2.1 Crear el modelo Profile 

