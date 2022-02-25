from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Perfil, Tuit
from django.forms.widgets import Textarea


class PerfilInline(admin.StackedInline):
    model = Perfil


class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username", "last_name", "first_name"]
    list_display = ["id", "username", "last_name", "first_name"]
    inlines = [PerfilInline]
    list_per_page = 10


class TuitAdmin(admin.ModelAdmin):
    model = Tuit
    list_display = ["body_min", "user", "contar_caracteres", "created", "modified"]
    list_filter = ["user"]
    readonly_fields = ["contar_caracteres"]
    formfield_overrides = {
        models.CharField: {
            'widget': Textarea,
        }
    }
    list_per_page = 10

# class PerfilAdmin(admin.ModelAdmin):
#     model = Perfil
#     list_display = ["id", "user", "user_id"]


admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
# admin.site.register(Perfil, PerfilAdmin)
admin.site.register(Tuit, TuitAdmin)
admin.site.site_header = "Clon Tuiter | Admin Ver 1.0.0"
admin.site.index_title = "Tuiter Django 2022 | Admin Dashboard"
