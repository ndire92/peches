
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# from django.template import engine
# from django.template import Engine, EngineHandler, engines
from app.models import CustomUser
from django.contrib import messages


from peche.models import DimPecheArtisan,DimPecheArtisan, DimPecheAssure, DimPecheCommerce,DimPecheFinance, DimPecheInnovat, Visiteur


# @login_required(login_url='/')
def Home(request):

    pfina = DimPecheFinance.objects.all().count()
    peche = DimPecheArtisan.objects.all().count()
    pcom = DimPecheCommerce.objects.all().count()
    peino = DimPecheInnovat.objects.all().count()
    nb_visite = Visiteur.objects.all().count()

    context = {
        'peche': peche,
        'pfina': pfina,
        'peino': peino,
        'pcom': pcom,
        'nb_visite':nb_visite,

    }
    return render(request, 'Hod/home.html', context)
