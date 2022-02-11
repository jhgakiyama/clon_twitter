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

## Follows y Tuits:

### 7. Seguir y Dejar de Seguir

### 8. Crear logica para los Tuits 

### 9. Ver tuits

## Formularios y Submits:

### 10. Crear tuits

### 11. Prevenir doble creacion de tuits 

### 12. Mejorar el FrontEnd

