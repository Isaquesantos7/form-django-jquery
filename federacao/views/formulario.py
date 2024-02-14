from django.shortcuts import render

from federacao.models import UF

def formulario(request):
    # lista de unidades federativas
    lista_ufs = UF.objects.order_by('sigla').all()

    context = {
        'lista_ufs': lista_ufs
    }
    
    return render(request, 'base.html', context)