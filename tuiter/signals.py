from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Perfil


@receiver(post_save, sender=User)
def crear_perfil(sender, instance, created, **kwargs):
    if created:
        print(f"instance= {instance}")
        user_perfil = Perfil(user=instance)
        user_perfil.save()  # hago el save para obtener el User.id
        print("instance.perfil.id" + str(instance.perfil.id))
        user_perfil.follows.set([instance.perfil.id])
        # leer esto para many to many,
        # https://docs.djangoproject.com/en/dev/topics/db/examples/many_to_many/
        # alternativa: # no necesito pasarle el id, le paso el objeto completo
        # user_perfil.follows.add(instance.profile) , es mas eficiente xq agrego un solo elemento.
        # No tengo que iterar

        user_perfil.save()


# post_save.connect(crear_perfil, sender=User) ,lo quito: estoy usando el decorador
