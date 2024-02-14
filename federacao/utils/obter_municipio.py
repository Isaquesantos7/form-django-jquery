from django.http import JsonResponse

from federacao.models import Municipio


def obter_municipio(request):
    # buscando index da uf selecionada
    index = request.POST.get('uf')

    # listando municipios conforme unidade federativa
    lista_municipio = Municipio.objects.filter(uf__index=index).values('index', 'nome').order_by('nome').distinct()

    municipios = [{'index': municipio['index'], 'nome': municipio['nome']} for municipio in lista_municipio]

    return JsonResponse(municipios, safe=False)