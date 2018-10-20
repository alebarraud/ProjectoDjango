# Create your views here.
from django.views.generic import TemplateView

class Index(TemplateView):
    template_name = 'inicio/index.html'
