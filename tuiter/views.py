from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Perfil


class PerfilListView(ListView):
    model = Perfil

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Perfil.objects.exclude(user=self.request.user).order_by('user__username')

        return Perfil.objects.all().order_by('user__username')


class PerfilDetailView(DetailView):
    model = Perfil
