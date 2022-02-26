from django.urls import path
from .views import PerfilListView, detailperfil

urlpatterns = [
    # path("", dashboard, name="dashboard"),
    path("perfil_list/", PerfilListView.as_view(), name="perfil_list"),
    path("perfil/<int:pk>", detailperfil, name="perfil_detail"),
]
