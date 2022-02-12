from django.views.generic import TemplateView


class DashboardView(TemplateView):
    template_name = 'home.html'
    #
    # def get_context_data(self, **kwargs):
    #     object =
