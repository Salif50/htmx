from django.db import models



class Produit(models.Model):
    designation=models.CharField(max_length=128)
    prix=models.IntegerField()
    quantite=models.IntegerField()


class Pays(models.Model):
    nom=models.CharField(max_length=128)


class Ville(models.Model):
    nom=models.CharField(max_length=128)
    pays=models.ForeignKey(Pays,on_delete=models.CASCADE)