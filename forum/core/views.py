from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexTemplateView(TemplateView):
    template_name = 'index.html'