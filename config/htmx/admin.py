from django.contrib import admin

from .models import Produit,Pays,Ville

admin.site.register(Produit)
admin.site.register(Pays)
admin.site.register(Ville)