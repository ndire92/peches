from django.shortcuts import render, redirect

from django.contrib import messages
from peche.DimPecheInnovat import pecino
from peche.PechTAAssurance import petttassu
from peche.PechTACommerc import pectom
from peche.PechTAFinance import pectafina
from peche.PechTransformArtisan import pectranf
from peche.PecheTAInnovation import pectaino

from peche.dimpechear import DPA
from peche.dimpecheas import DPAS
from peche.dimpechecom import DPC
from peche.dimpechefi import DPFI

from peche.models import DimPechTAAssurance, DimPechTACommerc, DimPechTAFinance, DimPechTransformArtisan, DimPecheArtisan, DimPecheAssure, DimPecheCommerce, DimPecheFinance, DimPecheInnovat, DimPecheTAInnovat

# Create your views here.


def pec_art(request):
    if request.method == 'POST':
        form = DPA(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/peche/dimpecart/')
    else:
        form = DPA()
        return render(request, 'peche/dimpecheart.html', {'form': form, 'dataObject': DimPecheArtisan.objects.all()})


# update art
def update_ar(request, id):
    dataObject = DimPecheArtisan.objects.get(id=id)
    form = DPA(instance=dataObject)
    if request.method == 'POST':
        form = DPA(request.POST, instance=dataObject)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/peche/dimpecart/')

    context = {

        'form': form

    }
    return render(request, 'peche/dimpecheart.html', context)


def delete_ar(request, id):
    dataObject = DimPecheArtisan.objects.get(id=id)
    if request.method == 'POST':
        dataObject.delete()
        return redirect('/peche/dimpecart/')
    context = {

        'item': dataObject, }
    return render(request, 'peche/delete_ar.html', context)


def pech_assu(request):
    if request.method == 'POST':
        form = DPAS(request.POST)
        if form.is_valid():

            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/peche/dimpecass/')
    else:
        form = DPAS()

        return render(request, 'peche/dimpecheass.html', {'form': form, 'dataObject': DimPecheAssure.objects.all()})


# update ass
def update_ass(request, id):
    dataOd = DimPecheAssure.objects.get(id=id)
    form = DPAS(instance=dataOd)
    if request.method == 'POST':
        form = DPAS(request.POST, instance=dataOd)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/peche/dimpecass/')

    context = {

        'form': form,

    }
    return render(request, 'peche/dimpecheass.html', context)


def delete_ass(request, id):
    dataOd = DimPecheAssure.objects.get(id=id)
    if request.method == 'POST':
        dataOd.delete()
        return redirect('/peche/dimpecass/')
    context = {

        'item': dataOd, }
    return render(request, 'peche/delete_ass.html', context)


def pech_fin(request):
    if request.method == 'POST':
        form = DPFI(request.POST)
        if form.is_valid():

            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/peche/dimpecfin/')
    else:
        form = DPFI()

        return render(request, 'peche/dimpechefin.html', {'form': form, 'dataObject': DimPecheFinance.objects.all()})


# update finace
def update_fin(request, id):
    dataOf = DimPecheFinance.objects.get(id=id)
    form = DPFI(instance=dataOf)
    if request.method == 'POST':
        form = DPFI(request.POST, instance=dataOf)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/peche/dimpecfin/')

    context = {

        'form': form,

    }
    return render(request, 'peche/dimpechefin.html', context)


def delete_fin(request, id):
    dataOf = DimPecheFinance.objects.get(id=id)
    if request.method == 'POST':
        dataOf.delete()
        return redirect('/peche/dimpecfin/')
    context = {

        'item': dataOf, }
    return render(request, 'peche/delete_fin.html', context)


def pech_ec(request):
    if request.method == 'POST':
        form = DPC(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/peche/dimpecec/')
    else:
        form = DPC()
        return render(request, 'peche/dimpechecomm.html', {'form': form, 'dataObject': DimPecheCommerce.objects.all()})


# update commm
def update_com(request, id):
    dataOC = DimPecheCommerce.objects.get(id=id)
    form = DPC(instance=dataOC)
    if request.method == 'POST':
        form = DPC(request.POST, instance=dataOC)
        if form.is_valid():
            messages.success(request, " Are Successfully Added !")
            form.save()
            return redirect('/peche/dimpecec/')

    context = {

        'form': form,

    }
    return render(request, 'peche/dimpechecomm.html', context)


def delete_com(request, id):
    dataOC = DimPecheCommerce.objects.get(id=id)
    if request.method == 'POST':
        dataOC.delete()
        return redirect('/peche/dimpecec/')
    context = {

        'item': dataOC, }
    return render(request, 'peche/delete_com.html', context)


def pech_inov(request):
    if request.method == 'POST':
        form = pecino(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/peche/pech_ino/')
    else:
        form = pecino()
        return render(request, 'peche/peche_ino.html', {'form': form, 'dataObject': DimPecheInnovat.objects.all()})


# update commm
def update_ino(request, id):
    dataOC = DimPecheInnovat.objects.get(id=id)
    form = pecino(instance=dataOC)
    if request.method == 'POST':
        form = pecino(request.POST, instance=dataOC)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/peche/pech_ino/')

    context = {

        'form': form,

    }
    return render(request, 'peche/peche_ino.html', context)


def delete_ino(request, id):
    dataOC = DimPecheInnovat.objects.get(id=id)
    if request.method == 'POST':
        dataOC.delete()
        return redirect('/peche/pech_ino/')
    context = {

        'item': dataOC, }
    return render(request, 'peche/delete_ino.html', context)


# peche trans

def pechtrans(request):
    if request.method == 'POST':
        form = pectranf(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/peche/pech_trans/')
    else:
        form = pectranf()
        return render(request, 'peche/peche_transf.html', {'form': form, 'dataObject': DimPechTransformArtisan.objects.all()})


# update commm
def update_trs(request, id):
    dataOC = DimPechTransformArtisan.objects.get(id=id)
    form = pectranf(instance=dataOC)
    if request.method == 'POST':
        form = pectranf(request.POST, instance=dataOC)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/peche/pech_trans/')

    context = {

        'form': form,

    }
    return render(request, 'peche/peche_transf.html', context)


def delete_trs(request, id):
    dataOC = DimPechTransformArtisan.objects.get(id=id)
    if request.method == 'POST':
        dataOC.delete()
        return redirect('/peche/pech_trans/')
    context = {

        'item': dataOC, }
    return render(request, 'peche/delete_trans.html', context)


# pechetaassu

def pechtassu(request):
    if request.method == 'POST':
        form = petttassu(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/peche/pech_taassu/')
    else:
        form = petttassu()
        return render(request, 'peche/peche_tass.html', {'form': form, 'dataObject': DimPechTAAssurance.objects.all()})


# update commm
def update_tassu(request, id):
    dataOC = DimPechTAAssurance.objects.get(id=id)
    form = petttassu(instance=dataOC)
    if request.method == 'POST':
        form = petttassu(request.POST, instance=dataOC)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/peche/pech_taassu/')

    context = {

        'form': form,

    }
    return render(request, 'peche/peche_tass.html', context)


def delete_tasuu(request, id):
    dataOC = DimPechTAAssurance.objects.get(id=id)
    if request.method == 'POST':
        dataOC.delete()
        return redirect('/peche/pech_taassu/')
    context = {

        'item': dataOC, }
    return render(request, 'peche/delete_taassu.html', context)


# pechet

def petacom(request):
    if request.method == 'POST':

        form = pectom(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/peche/pech_tacom/')
    else:
        form = pectom()
        return render(request, 'peche/peche_tacom.html', {'form': form, 'dataObject': DimPechTACommerc.objects.all()})


# update commm
def update_tacom(request, id):
    dataObject = DimPechTACommerc.objects.get(id=id)
    form = pectom(instance=dataObject)
    if request.method == 'POST':
        form = pectom(request.POST, instance=dataObject)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/peche/pech_tacom/')

    context = {

        'form': form,

    }
    return render(request, 'peche/peche_tacom.html', context)


def delete_tacom(request, id):
    dataObject = DimPechTACommerc.objects.get(id=id)
    if request.method == 'POST':
        dataObject.delete()
        return redirect('/peche/pech_tacom/')
    context = {

        'item': dataObject, }
    return render(request, 'peche/delete_tacom.html', context)


# pechetpech_tainov

def pech_tainov(request):
    if request.method == 'POST':
        form = pectaino(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/peche/pech_taino/')
    else:
        form = pectaino()
        return render(request, 'peche/peche_taino.html', {'form': form, 'dataObject': DimPecheTAInnovat.objects.all()})


# update commm
def up_taino(request, id):
    dataOC = DimPecheTAInnovat.objects.get(id=id)
    form = pectaino(instance=dataOC)
    if request.method == 'POST':
        form = pectaino(request.POST, instance=dataOC)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/peche/pech_taino/')

    context = {

        'form': form,

    }
    return render(request, 'peche/peche_taino.html', context)


def de_taino(request, id):
    dataOC = DimPecheTAInnovat.objects.get(id=id)
    if request.method == 'POST':
        dataOC.delete()
        return redirect('/peche/pech_taino/')
    context = {

        'item': dataOC, }
    return render(request, 'peche/delete_taino.html', context)


# pechetpech_tainov

def pechtafina(request):
    if request.method == 'POST':
        form = pectafina(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/peche/pech_tafina/')
    else:
        form = pectafina()
        return render(request, 'peche/peche_fina.html', {'form': form, 'dataObject': DimPechTAFinance.objects.all()})


# update commm
def up_fina(request, id):
    dataOC = DimPechTAFinance.objects.get(id=id)
    form = pectafina(instance=dataOC)
    if request.method == 'POST':
        form = pectafina(request.POST, instance=dataOC)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/peche/pech_tafina/')

    context = {

        'form': form,

    }
    return render(request, 'peche/peche_fina.html', context)


def de_fina(request, id):
    dataOC = DimPechTAFinance.objects.get(id=id)
    if request.method == 'POST':
        dataOC.delete()
        return redirect('/peche/pech_tafina/')
    context = {

        'item': dataOC, }
    return render(request, 'peche/delete_tafina.html', context)


# pechetpech_fac
def pcount(request):

    pfina = DimPecheFinance.objects.all().count()
    peche = DimPecheArtisan.objects.all().count()
    pcom = DimPecheCommerce.objects.all().count()
    peino = DimPecheInnovat.objects.all().count()

    context = {
        'peche': peche,
        'pfina': pfina,
        'peino': peino,
        'pcom': pcom,

    }
    return render(request, 'peche/hm.html', context)
