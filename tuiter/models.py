from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE)

    follows = models.ManyToManyField(
        "self",
        related_name="followed_by",
        # permite acceder a las entradas de datos desde el otro extremo
        # de esa relación a través del nombre "followed_by".
        blank=True,
        symmetrical=False
        # el user 1 puede seguir al user 2,pero el user 2 -> no sigue al user1
        # https://docs.djangoproject.com/en/4.0/ref/models/fields/#django.db.models.ManyToManyField.symmetrical

    )

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "Perfiles"
