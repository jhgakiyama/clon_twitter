# clon_twitter
Editor online: https://dillinger.io/

## Proyecto basado en el siguiente post:
https://realpython.com/django-social-network-1/

## Modelos y Relaciones:

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

Agrego en el admin , dentro de Usuario , la vista para agregar perfiles

### 3. Asignar perfiles cuando se crea el usuario

#### 3.1 Django Signals 

Lo que quiero hacer es que cuando se cree un Usuario ,automaticamente se cree un Perfil de ese usuario.
Y a la vez se siga a si mismo. 

Agrego en apps.py, dentro de la clase de la app

    def ready(self):
        import tuiter.signals

Creo signals.py y agrego el tigre que va a ejecutarse

Importo el decorador. Agrego una funcion que me permite crear y asociar un Perfil cuando se da de alta un User

## Templates y Estilos en el FrontEnd:

https://realpython.com/django-social-front-end-2/
### 4. Creo el Template Base con Bulma
Creo el directorio 'templates' dentro de la carpeta del proyecto
Aca iran el base.html y el home.html

Agrego en los setting,  'DIRS': [BASE_DIR / 'templates'],

Agrego el archivo 'base.html'

Agrego el CDN de Bulma

~~Incluyo las url de la aplicacion en urls.py del Proyecto~~

~~Creo el file urls.py dentro de la app~~

~~Creo la funcion dashboard en tuiter/views.py~~

~~Agrego la url en la app~~

Crear una Vista Basada en Clases (VBC) , para renderizar el home

Creo el file views.py dentro de la carpeta del Proyecto

Agrego las url para la Clase


### 5. Listado de Perfiles

No voy a utilizar una funcion. Voy a crear el List View (VBC) de los Perfiles.

Excluyo mi propio perfil cuando estoy logueado

Sino traigo todos los perfiles , es decir cuando soy un 'Usuario Anonimo'

Sobre escribo el metodo get_queryset

Creo dentro de la carpeta de la app, /templates/tuiter/perfil_list.html

Respeto el nombre, para no utilizar el atributo 'template_name' en la VBC

En este momento elimino del repo la bd sqlite
Quite de views.py --> app_name = "tuiter"
En este momento no me acuerdo para que servia.

### 6. Vista de un Perfil

Agrego el nuevo 'endpoint' para ver un Perfil. Le tengo que pasar como parametro la clave primaria (pk)

Creo la VBC , heredo DetailView.

Edito un poco a mi gusta el perfil_detail.html

Agrego link para poder ver el listado de perfiles y el detalle de un perfil 

https://realpython.com/django-social-post-3/
## Follows y Tuits:

### 7. Seguir y Dejar de Seguir

Se agregan 2 botones

Cuando deberian aparecer los botones:
1. Hay que estar logueado. falta
2. No estar mirando mi propio perfil. OK
3. El boton verde activado , si no lo sigo. OK
4. El boton rojo activado , si lo sigo. OK

TODO: 

FALTA TERMINAR LA FUNCION PARA HACER FOLLOW O UNFOLLOW

### 8. Crear logica para los Tuits 

Crear el modelo para los Tuits

Agrego un modelo abstracto para la fecha de creacion y modificacion

Lo agrego al Admin

Creo varios tuits para ver desde el Admin

Duda: se ve mal la hora desde el admin

### 9. Ver tuits
Hago mejoras en perfil_detail , agrego los tuits

Agrego humanize a las app en settings para ver el atrib datetime

Crear un dashborad (yo le diria home), donde voy a ver dos cosas:
1. Todos los tuits de los "Perfiles" que sigo
2. Poder crear mis Tuits

## Formularios y Submits:

1. Crear Forms
2. Prevenir el doble 'envio' y mostrar los errores

### 10. Crear tuits

Creo forms.py

Creo el ModelForm basado en el Modelo Tuit

Edito un poco el form agregando widget

Agrego el boton para el 'submit'

***
En esta etapa tengo diferencias con el codigo del tutorial 

Porque estoy utilizando Vistas Basadas en Clases para la vista del "home"

En el tutorial utiliza una funcion:

```
def dashboard(request): 
   codigo...
```
***
### 11. Prevenir doble creacion de tuits - Manejo de errores

El problema se da en este momento que al recargar la pagina (ctrl + r) se hace un nuevo envio del Form

Importamos "Django redirect"

```
from django.shortcuts import redirect
```

En esta etapa del proyecto, decido cambiar la vista del home, por una Vista Basada en Funcion para no complicarme la vida

### 12. Mejorar el FrontEnd

## Buenas practicas a seguir



### Orden de los atributos y metodos en los modelos

1. constants (for choices and others)
2. fields of the model
3. custom manager indication
4. meta
5. ```def __unicode__ # python 2 def __str__ # python 3 ```
6. other special methods
7. def clean
8. def save
9. def get_absolute_url
10. other methods


https://medium.com/@rodrigogr/sobrescribir-metodo-get-queryset-django-a91c5872152