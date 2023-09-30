from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Produit,Pays,Ville
def home(request):
    produits=Produit.objects.all()
    pays=Pays.objects.all()
    villes=Ville.objects.all()
    context={
        'produits':produits,
        "pays":pays,
        "villes":villes
    }

    return render(request,'htmx/home.html',context)


def add(request):
    if request.method == "POST":
        designation=request.POST.get('designation')
        prix=request.POST.get('prix')
        quantite=request.POST.get('quantite')
        produit=Produit.objects.create(
            designation=designation,
            prix=prix,
            quantite=quantite
        )
        produit.save()
        return render(request,'htmx/component/new.html',{'produit':produit})


def delete(request,pk):
    produit=get_object_or_404(Produit,id=pk)
    produit.delete()
    return HttpResponse('')



def filtre(request):
    id=request.POST.get('pays')
    pays=Pays.objects.get(pk=id)
    print('pays',pays)
    villes=Ville.objects.filter(pays=pays)
    print('villes',villes)
    return render(request,"htmx/component/filtre.html",{"villes":villes})



