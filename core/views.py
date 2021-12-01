from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .form import CadastroForm


def index(request):
    return render(request, "index.html")


@login_required
def cadastro(request):
    form = CadastroForm()
    return render(request, "cadastro.html", {"form": form})


def cadastro_novo(request):
    form = CadastroForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Sua mensagem foi enviada com sucesso!')
        return redirect('index')
    else:
        messages.error(
            request, 'Houve um erro, reenvie novamente a mensagem!')
        return redirect('index')
