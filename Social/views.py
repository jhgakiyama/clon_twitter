from django.views.generic import ListView
from tuiter.models import Tuit
from django.contrib.auth.models import User


class HomeTuitsListView(ListView):
    model = Tuit
    template_name = 'home.html'

    def get_queryset(self):
        """
        Recupero todos los tuist , de los usuarios que yo sigo, excluyo mis tuits
        """
        if self.request.user.is_authenticated:
            return Tuit.objects.filter(user__in=User.objects.filter(
                id__in=self.request.user.perfil.follows.all())).exclude(user=self.request.user)

        return None
