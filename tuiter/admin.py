from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Perfil, Tuit


class PerfilInline(admin.StackedInline):
    model = Perfil


class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username", "last_name", "first_name"]
    list_display = ["id", "username"]
    inlines = [PerfilInline]


class PerfilAdmin(admin.ModelAdmin):
    model = Perfil
    list_display = ["id", "user", "user_id"]


class TuitAdmin(admin.ModelAdmin):
    model = Tuit
    list_display = ["body_min", "user", "created", "modified"]
    list_filter = ["user"]


admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
admin.site.register(Perfil, PerfilAdmin)
admin.site.register(Tuit, TuitAdmin)
admin.site.site_header = "Clon Tuiter | Admin Ver 1.0.0"
admin.site.index_title = "Tuiter Django 2022 | Admin Dashboard"
