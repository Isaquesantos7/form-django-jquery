from django.http import JsonResponse

from federacao.models import Bairro


def obter_bairro(request):

    # obtendo index do municipio selecionado
    index = request.POST.get('municipio')

    # lista de bairros com base no municipio escolhido
    lista_bairros = Bairro.objects.filter(municipio__index=index).values('index', 'nome').order_by('nome').distinct().all()

    bairros = [{'index': bairro['index'], 'nome': bairro['nome']} for bairro in lista_bairros]

    return JsonResponse(bairros, safe=False)