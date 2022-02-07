from django.contrib import admin
from django.contrib.auth.models import User, Group


class UserAdmin(admin.ModelAdmin):
    model = User
    # Only display the "username" field
    fields = ["username"]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
admin.site.site_header = "Clon Tuiter | Admin Ver 1.0.0"
admin.site.index_title = "Tuiter Django 2021 | Admin Dashboard"