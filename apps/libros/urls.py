from django.conf.urls import patterns, include, url
from .views import ReportarLibros

urlpatterns = patterns('',
    url(r'^reportar/$',ReportarLibros.as_view(), name = 'reportar_libros'),
)
