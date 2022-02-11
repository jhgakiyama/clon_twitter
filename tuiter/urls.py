from django.urls import path
from .views import PerfilListView, PerfilDetailView

urlpatterns = [
    # path("", dashboard, name="dashboard"),
    path("perfil_list/", PerfilListView.as_view(), name="perfil_list"),
    path("perfil/<int:pk>", PerfilDetailView.as_view(), name="perfil_detail"),
]
