from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Prestacao, Visao_geral


def home(request):
    visao_geral = Visao_geral.objects.all()

    dados = {
        'visao_geral': visao_geral
    }

    return render(request, 'home.html', dados)

def prestacao(request, prestacao_id):
    prestacao = get_object_or_404(Prestacao, pk=prestacao_id)

    prestacao_a_exibir = {
        'prestacao' : prestacao
    }

    return render(request, 'valores_descricao.html', prestacao_a_exibir)