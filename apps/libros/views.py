# Create your views here.
from .models import Libros
from django.views.generic import CreateView,TemplateView,ListView

class ReportarLibros(ListView):
    template_name = 'libros/reportarlibros.html'
    model = Libros
