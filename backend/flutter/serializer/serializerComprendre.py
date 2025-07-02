from rest_framework import serializers
from ..models import Comprendre,Commande,Produit

class ComprendreSerializer(serializers.ModelSerializer):
    numCommande = serializers.PrimaryKeyRelatedField(
        queryset=Commande.objects.all(),
        error_messages={
            'does_not_exist': "Ce commande spécifié n'existe pas !",
            'incorrect_type': "Le format de l'ID du commande est invalide !",
        }
    )
    numProduit = serializers.PrimaryKeyRelatedField(
        queryset=Produit.objects.all(),
        error_messages={
            'does_not_exist': "Ce produit spécifié n'existe pas !",
            'incorrect_type': "Le format de l'ID du produit est invalide !",
        }
    )

    class Meta:
        model=Comprendre
        fields=[
            "numComprendre",
            "numCommande",
            "numProduit",
            "quantiteCommande",
        ]
    
    def validate(self, data):
        produit=data.get("numProduit")
        if data.get("quantiteCommande",0)>produit.quantite:
            raise serializers.ValidationError({"erreur":"Quantité du produit commandé insuffisant !"})
        return data
    
    def create(self, validated_data):
        produit=validated_data.get("numProduit")
        produit.quantite-=validated_data.get("quantiteCommande",0)
        produit.save()
        return Comprendre.objects.create(**validated_data)