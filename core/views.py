from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect #nova importacao

from .forms import ContatoForm, ProdutoModelForm
from .models import Produto


def index(request):
    context = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'index.html', context)

def contato(request):
    if str(request.user) != 'AnonymousUser':
        form = ContatoForm(request.POST or None)

        if str(request.method) == 'POST':
            if form.is_valid():

                form.save() #criado para tentar authenticar usuarios! obs: indo dormi  esta funcionando

                form.send_email()

                messages.success(request, 'E-mail enviado com sucesso!')
                form = ContatoForm()
            else:
                messages.error(request, 'Erro ao enviar e-mail!')
        context = {
        'form': form,
    }
        return render(request, 'contato.html', context)
    else:
        return redirect('index')


def produto(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = ProdutoModelForm(request.POST, request.FILES)
            if form.is_valid():

                form.save()

                messages.success(request, 'Produto Salvo com sucesso!')
                form = ProdutoModelForm()
            else:
                messages.error(request, 'Erro ao salvar produto!')
        else:
            form = ProdutoModelForm()
        context = {
              'form': form
        }
        return render(request, 'produto.html', context)
    else:
        return redirect('index')