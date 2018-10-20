# Create your views here.
from django.views.generic import TemplateView
from django.shortcuts import render
from apps.libros.models import Libros

class BuscarView(TemplateView):

    def post(self, request, *args, **kwargs):
        buscar = request.POST['buscalo']

        libros = Libros.objects.filter(nombre__contains = buscar)
        listacategoria = Libros.objects.filter(categoria__contains = buscar)

        #verifica si en buscar no se tipeo nada, es decir, si damos click a buscar sin haber
        #escrito la pagina nos tirar un mensaje diciendo que la entrada esta vacia
        #y que vuelva a tipear
        if(len(buscar)==0):
            return render(request,'buscar/buscar.html',
            {'vacio':True})


        if not(len(listacategoria)==0):
            return render(request,'buscar/buscar.html',
            {'categoria':True,'lista':listacategoria,'vacio':False})

        #elif (len(buscar)==0) and (len(listacategoria)==0):
        #    return render(request,'buscar/buscar.html',
        #    {'buscar':True,'categoria':False})

        elif libros:
            return render(request,'buscar/buscar.html',
            {'libros':libros,'libro':True,'cat':False})

        else:
            return render(request,'buscar/buscar.html',
            {'aux':True})
