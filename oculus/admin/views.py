# oculus

from django.views.generic import TemplateView

from application.views import LoginRequiredMixin


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "oculus/admin/index.html"


class AJAXIndexView(LoginRequiredMixin, TemplateView):
    template_name = "oculus/admin/ajax_index.html"
