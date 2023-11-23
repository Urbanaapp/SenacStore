from django.shortcuts import render
from StoreApp.models import Departamento
# Create your views
def index(request):

    departamentos = Departamento.objects.all()
    context ={
        'departamentos' : departamentos
    }
    return render(request, 'index.html',context)


def produto_lista(request):
    return render(request,'produtos.html')


def produto_detalhe(request):
    return render(request,'produto_detalhes.html')
