from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexTemplateView(LoginRequiredMixin,TemplateView): #LoginRequiredMixin will always redirect us to login url when not logged in
    template_name = 'index.html'