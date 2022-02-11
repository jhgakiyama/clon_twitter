from django.db import models
from django.contrib.auth.models import User


class TimeStampedModel(models.Model):
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='creado',
        help_text='fecha de creacion'
    )

    modified = models.DateTimeField(
        auto_now=True,
        verbose_name='modificado',
        help_text='fecha de modificacion'
    )

    class Meta:
        abstract = True


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


class Tuit(TimeStampedModel):
    user = models.ForeignKey(
        User,
        related_name="tuits",  # con esto puedo acceder a los tuits del lado de User
        on_delete=models.DO_NOTHING
    )
    body = models.TextField(
        verbose_name='mensaje',
        max_length=140
    )

    def __str__(self):
        return f"@{self.user} ({self.created:%Y-%m-%d %H:%M}) {self.body[:30]}..."

    def body_min(self):
        return f"{self.body[:30]}..."

    body_min.short_description = "Mensaje"
