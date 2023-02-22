from django.shortcuts import render, redirect
from foncier.DimFoncier import Dimfonfon
from foncier.FactFoncie import Dimff
from django.contrib import messages
from foncier.DimFoncierGouvernanc import Dimfong
from foncier.DimGeographie import Dimfgeo


from foncier.models import DimFoncier, DimFoncierGouvernanc, DimGeographie, FactFoncier

# Create your views here.


def DimFon(request):

    if request.method == 'POST':

        form = Dimfonfon(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/foncier/DimFoncier/')
    else:
        form = Dimfonfon()

    return render(request, 'pag/Dimfon.html', {'form': form, 'dataObject': DimFoncier.objects.all()})


# update Gouver
def update_fonc(request, id):
    dataObject = DimFoncier.objects.get(id=id)
    form = Dimfonfon(instance=dataObject)
    if request.method == 'POST':
        form = Dimfonfon(request.POST, instance=dataObject)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/foncier/DimFoncier/')

    context = {

        'form': form

    }
    return render(request, 'pag/Dimfon.html', context)


def delete_up_fonc(request, id):
    dataObject = DimFoncier.objects.get(id=id)
    if request.method == 'POST':

        dataObject.delete()
        return redirect('/foncier/DimFoncier/')
    context = {

        'item': dataObject, }
    return render(request, 'pag/delete_fon.html', context)


def DFG(request):
    if request.method == 'POST':
        form = Dimfong(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/foncier/DimFoncierGouvernanc/')
    else:
        form = Dimfong()

    return render(request, 'pag/DimFoncierGouvernanc.html', {'form': form, 'dataObject': DimFoncierGouvernanc.objects.all()})


# update Gouver
def update_up_Gouve(request, id):
    dataObject = DimFoncierGouvernanc.objects.get(id=id)
    form = Dimfong(instance=dataObject)
    if request.method == 'POST':
        form = Dimfong(request.POST, instance=dataObject)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/foncier/DimFoncierGouvernanc/')

    context = {

        'form': form

    }
    return render(request, 'pag/DimFoncierGouvernanc.html', context)


def delete_up_Gouve(request, id):
    dataObject = DimFoncierGouvernanc.objects.get(id=id)
    if request.method == 'POST':

        dataObject.delete()
        return redirect('/foncier/DimFoncierGouvernanc/')
    context = {

        'item': dataObject, }
    return render(request, 'pag/delete_fon.html', context)


def DG(request):
    if request.method == 'POST':
        form = Dimfgeo(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/foncier/DimGeographie/')
    else:
        form = Dimfgeo()

    return render(request, 'pag/DimGeographie.html', {'form': form, 'dataObject': DimGeographie.objects.all()})


# update Geo
def update_geo(request, id):
    dataOge = DimGeographie.objects.get(id=id)
    form = Dimfgeo(instance=dataOge)
    if request.method == 'POST':
        form = Dimfgeo(request.POST, instance=dataOge)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/foncier/DimGeographie/')

    context = {

        'form': form,

    }
    return render(request, 'pag/DimGeographie.html', context)


def delete_geo(request, id):
    dataOge = DimGeographie.objects.get(id=id)
    if request.method == 'POST':
        dataOge.delete()
        return redirect('/foncier/DimGeographie/')
    context = {

        'item': dataOge, }
    return render(request, 'pag/delete_geo.html', context)


def FF(request):
    if request.method == 'POST':
        form = Dimff(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/FactFoncier/')
    else:
        form = Dimff()

    return render(request, 'pag/FactFoncier.html', {'form': form, 'dataObject': FactFoncier.objects.all()})


# update FAC FONCIER
def update_ff(request, id):
    dataObject = FactFoncier.objects.get(id=id)
    form = Dimff(instance=dataObject)
    if request.method == 'POST':
        form = Dimff(request.POST, instance=dataObject)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/FactFoncier/')

    context = {

        'form': form,

    }
    return render(request, 'pag/FactFoncier.html', context)


def delete_ff(request, id):
    dataObject = FactFoncier.objects.get(id=id)
    if request.method == 'POST':
        dataObject.delete()
        return redirect('/FactFoncier/')
    context = {

        'item': dataObject, }
    return render(request, 'pag/delete_geo.html', context)
