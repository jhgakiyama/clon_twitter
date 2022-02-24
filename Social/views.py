from django.views.generic import ListView
from tuiter.models import Tuit
from tuiter.forms import TuitModelForm
from django.shortcuts import render, redirect


# class HomeTuitsListView(ListView):
#     model = Tuit
#     template_name = 'home.html'
#
#     def get_queryset(self):
#         """
#         Recupero todos los tuits, de los Perfiles que sigue el User autenticado
#         Se excluyen los tuits del User autenticado
#         """
#
#         if self.request.user.is_authenticated:
#             return Tuit.objects.filter(
#                 # user__perfil__in=self.request.user.perfil.follows.all()).exclude(user=self.request.user)
#                 user__perfil__in=self.request.user.perfil.follows.all()
#             )
#         return None
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         form = TuitModelForm()
#         context["form"] = form
#         return context
#
#     def post(self, request, *args, **kwargs):
#         """
#         https://stackoverflow.com/questions/33876790/how-to-check-for-a-post-method-in-a-listview-in-django-views-im-getting-a-405
#         """
#         form = TuitModelForm(request.POST)
#         if form.is_valid():
#             tuit = form.save(commit=False)
#             tuit.user = request.user
#             tuit.save()
#             return redirect("home")


def home(request):
    """
    Redefino la clase de arriba y dejo de usar CBV por el momento
    En teoria deberia ser mas facil
    """
    # Armar la logica del form
    # Devolver la coleccion de tuits
    # Tengo que renderizar el template
    template_name = 'home.html'
    context = {}

    form = TuitModelForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            tuit = form.save(commit=False)
            tuit.user = request.user
            tuit.save()
            return redirect("home")

    if request.user.is_authenticated:
        object_list = Tuit.objects.filter(
            user__perfil__in=request.user.perfil.follows.all()).exclude(user=request.user)
    else:
        object_list = None

    context["form"] = form
    context["object_list"] = object_list

    return render(request, template_name, context)
