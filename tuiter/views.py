from django.shortcuts import render
from django.views.generic import ListView
from .models import Perfil


class PerfilListView(ListView):
    model = Perfil

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Perfil.objects.exclude(user=self.request.user).order_by('user__username')

        return Perfil.objects.all().order_by('user__username')


def detailperfil(request, pk):
    context = {}
    perfil_actual = Perfil.objects.get(pk=pk)
    template_name = "tuiter/perfil_detail.html"

    if request.method == "POST":
        mi_perfil = request.user.perfil
        data = request.POST
        accion = data.get("btn_seguir")  # obtengo el 'value' del boton

        if accion == "seguir":
            mi_perfil.follows.add(perfil_actual)
        elif accion == "no_seguir":
            mi_perfil.follows.remove(perfil_actual)

        mi_perfil.save()

    context["object"] = perfil_actual

    return render(request, template_name, context)

