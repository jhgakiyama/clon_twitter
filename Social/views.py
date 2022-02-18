from django.views.generic import ListView
from tuiter.models import Tuit


class HomeTuitsListView(ListView):
    model = Tuit
    template_name = 'home.html'

    def get_queryset(self):
        """
        Recupero todos los tuits , de los Perfiles que sigue el User autenticado
        Se excluyen los tuits del User autenticado
        """

        if self.request.user.is_authenticated:
            return Tuit.objects.filter(
                user__perfil__in=self.request.user.perfil.follows.all()).exclude(user=self.request.user)

        return None
