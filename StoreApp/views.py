from django.shortcuts import render
from django.core.mail import send_mail
from StoreApp.models import Departamento, Produto
from StoreApp.forms import ContatoForm, ClienteForm

# Create your views
def index(request):    
    produtos_em_destaque = Produto.objects.filter(destaque = True)    

    context ={
        'produtos': produtos_em_destaque

    }

    return render(request, 'index.html',context)


def produto_lista(request):
    # Buscando produtos no banco 
    produtos = Produto.objects.all()

    context = {
        'produtos' : produtos,
        'categoria': 'Todos Produtos'
    }

    return render(request,'produtos.html',context)

def produto_lista_por_id(request,id):
    # Buscando produtos no banco  filtrando por detpo
    produtos = Produto.objects.filter(departamento_id = id)
    # Buscar departamento no banco
    departamento = Departamento.objects.get(id = id)
    context = {
        'produtos' : produtos,
        'categoria': departamento.nome
    }

    return render(request,'produtos.html',context)


def produto_detalhe(request, id):
    produto = Produto.objects.get(id = id)
    produtos_relacionados = Produto.objects.filter(departamento_id = 
                                                   produto.departamento.id).exclude(id = id)[:4]
    
    context = {
        'produto': produto,
        'produtos_relacionados' : produtos_relacionados
    }
    return render(request,'produto_detalhes.html', context)

def institucional(request):           
    return render(request,'institucional.html')

def contato(request):     
    mensagem = ''
    # Se o form foi enviado (botao enviar)
    if request.method == 'POST':
        nome = request.POST['nome']
        telefone = request.POST['telefone']
        assunto = request.POST['assunto']
        mensagem = request.POST['mensagem']
        remetente = request.POST['email']
        destinatario = ['matheus10.c48@gmail.com']
        corpo = f'Nome: {nome} \nTelefone:{telefone} \nMensagem: {mensagem}'

        try:               
            # fazer o envio do e-mail
            send_mail (assunto, corpo, remetente, destinatario )
            mensagem = 'Envido com sucesso :)'
        except:
            mensagem = 'Erro ao enviar a Mesagem :('
    # Criando uma instancia do form de Contato
    formulario = ContatoForm()

    context = {
        'form_contato' : formulario, 
        'mensagem' : mensagem   
    }
    return render(request,'contato.html', context)

def cadastro(request):
    mensagem = ''
    # quando envio o formulario preenchido
    if request.method == 'POST':  
        formulario = ClienteForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            formulario = ClienteForm()
            mensagem = 'Clientec cadastrado com sucesso :)'
        else:
            mensagem = 'Verifique os erros abaixo: '    
    else:
        formulario = ClienteForm()
    
    context = {
        'form_cadastro': formulario,
        'mensagem': mensagem
    }
    return render(request, 'cadastro.html', context)

