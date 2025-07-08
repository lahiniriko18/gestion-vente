from django.db import models
from django.contrib.auth.models import AbstractUser
import qrcode
from io import BytesIO
from django.core.files import File
from django.conf import settings
from django.utils import timezone

class Classement(models.Model):
    numClassement = models.AutoField(primary_key=True)
    nomClassement = models.CharField(max_length=20)
    quantiteMin = models.FloatField()
    quantiteMax = models.FloatField(null=True)
    descClassement = models.TextField(null=True)

    class Meta:
        db_table = 'classement'
        verbose_name = 'Classement'
        verbose_name_plural = 'Classements'
    
    def __str__(self):
        return self.nomClassement


class Categorie(models.Model):
    numCategorie = models.AutoField(primary_key=True)
    nomCategorie = models.CharField(max_length=50)
    imageCategorie = models.ImageField(upload_to='images/produits/categories/',null=True)
    descCategorie = models.TextField(null=True)

    class Meta:
        db_table = 'categorie'
        verbose_name = 'Categorie'
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.nomCategorie
    
class Produit(models.Model):
    numProduit = models.AutoField(primary_key=True)
    numClassement = models.ForeignKey(
        Classement, 
        related_name='produits', 
        on_delete=models.SET_NULL, 
        db_column='numClassement',
        null=True
    )
    numCategorie = models.ForeignKey(
        Categorie, 
        related_name='produits', 
        on_delete=models.CASCADE, 
        db_column='numCategorie',
        null=True
    )
    libelleProduit = models.CharField(max_length=20)
    quantite = models.FloatField(default=0)
    prixUnitaire = models.FloatField(null=True)
    uniteMesure = models.CharField(10, null=True)
    description = models.TextField(null=True)
    qrCode = models.ImageField(upload_to='images/produits/qrcode/', null=True, blank=True)

    class Meta:
        db_table = 'produit'
        verbose_name = 'Produit'
        verbose_name_plural = 'Produits'
    
    def __str__(self):
        return self.libelleProduit
    
    def gererQrCode(self):
        url = self.numProduit
        qr = qrcode.make(url)
        buffer = BytesIO()
        qr.save(buffer, format='PNG')
        file_name = f"qr_code_produit_{self.numProduit}.png"
        self.qrCode.save(file_name, File(buffer), save=False)
        self.save()


class Image(models.Model):
    numImage = models.AutoField(primary_key=True)
    numProduit = models.ForeignKey(
        Produit, 
        related_name='images',
        on_delete=models.CASCADE,
        db_column='numProduit'
    )
    nomImage = models.ImageField(upload_to='images/produits/images/',null=True)

    class Meta:
        db_table = 'image'
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
    
    def __str__(self):
        return self.nomImage


class Client(models.Model):
    numClient = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=20)
    contact = models.CharField(max_length=17, null=True)
    adresse = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = 'client'
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
    
    def __str__(self):
        return self.nom


class Commande(models.Model):
    numCommande = models.AutoField(primary_key=True)
    numClient = models.ForeignKey(
        Client, 
        related_name='commandes', 
        on_delete=models.SET_NULL, 
        db_column='numClient',
        null=True
    )
    dateCommande = models.DateTimeField(default=timezone.now)
    reference = models.CharField(max_length=30, null=True)

    class Meta:
        db_table = 'commande'
        verbose_name = 'Commande'
        verbose_name_plural = 'Commandes'
    
    def __str__(self):
        return f"Commande numéro {self.numCommande} par le client {self.numClient}"

    def save(self, *args, **kwargs):
        if not self.reference:
            super().save(*args, **kwargs)
            self.reference = f"Commande-{self.numCommande}"
            self.save()
        else:
            super().save(*args, **kwargs)


class Comprendre(models.Model):
    numComprendre = models.AutoField(primary_key=True)
    numCommande = models.ForeignKey(
        Commande, 
        related_name='comprendres', 
        on_delete=models.CASCADE,
        db_column='numCommande',
        null=True
    )
    numProduit = models.ForeignKey(
        Produit, 
        related_name='comprendres', 
        on_delete=models.CASCADE, 
        db_column='numProduit'
    )
    quantiteCommande = models.FloatField(default=0)

    class Meta:
        db_table = 'comprendre'
        verbose_name = 'Comprendre'
        verbose_name_plural = 'Comprendres'
    
    def __str__(self):
        return f"Commande du produi {self.numProduit}"
    

class Utilisateur(AbstractUser):
    contact = models.CharField(max_length=17, null=True)
    image = models.ImageField(upload_to='images/utilisateurs/', null=True)
    adresse = models.CharField(max_length=100, null=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)

    def clean(self):
        return super().clean()
    class Meta:
        db_table='utilisateur'

    def __str__(self):
        return self.username