from django.urls import path
from .views import PerfilListView

urlpatterns = [
    # path("", dashboard, name="dashboard"),
    path("perfil_list/", PerfilListView.as_view(), name="perfil_list"),
]
