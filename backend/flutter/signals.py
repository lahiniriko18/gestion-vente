from django.db.models.signals import post_delete,pre_save,post_save
from django.dispatch import receiver
from .models import Categorie,Produit,Comprendre

@receiver(post_delete, sender=Categorie)
def auto_delete_image_on_delete(sender, instance, **kwargs):
    if instance.imageCategorie:
        instance.imageCategorie.delete(save=False)

@receiver(post_delete, sender=Produit)
def auto_delete_image_on_delete(sender, instance, **kwargs):
    if instance.qrCode:
        instance.qrCode.delete(save=False)

@receiver(pre_save, sender=Categorie)
def auto_delete_image_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        ancienImage = Categorie.objects.get(pk=instance.pk).imageCategorie
    except Categorie.DoesNotExist:
        return False

    nouveauImage = instance.imageCategorie
    if ancienImage and ancienImage != nouveauImage:
        ancienImage.delete(save=False)

@receiver(post_save, sender=Comprendre)
def update_produit_quantite(sender, instance, created, **kwargs):
    if created:
        print(instance.quantiteCommande)
        produit = instance.numProduit
        if produit.quantite >= instance.quantiteCommande:
            produit.quantite -= instance.quantiteCommande
            produit.save()
        else:
            raise ValueError("Quantité demanée supérieure au stock disponible!")