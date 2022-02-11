from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Perfil


class PerfilListView(ListView):
    model = Perfil

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Perfil.objects.exclude(user=self.request.user)
        else:
            return Perfil.objects.all()


class PerfilDetailView(DetailView):
    model = Perfil
