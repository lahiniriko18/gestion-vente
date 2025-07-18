from rest_framework import serializers
from ..models import Commande,Client
from ..serializer.serializerProduit import ProduitSerializer
from ..serializer.serializerClient import ClientSerializer

class CommandeSerializer(serializers.ModelSerializer):

    numClient = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(),
        error_messages={
            'does_not_exist': "Ce client spécifié n'existe pas !",
            'incorrect_type': "Le format de l'ID du client est invalide !",
        }
    )
    client = ClientSerializer(source='numClient', read_only = True)
    produits = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model=Commande
        fields=[
            "numCommande",
            "numClient",
            "dateCommande",
            "reference",
            "client",
            "produits"
        ]
    
    def get_produits(self, obj):
        comprendres=obj.comprendres.all()
        request = self.context.get('request')
        produits = []
        for comprendre in comprendres:
            d={
                "produit":ProduitSerializer(comprendre.numProduit, context={'request':request}).data,
                "quantiteCommande":comprendre.quantiteCommande
            }
            produits.append(d)
        return produits
    
    def validate(self, data):
        return data
    
    def create(self, validated_data):
        return Commande.objects.create(**validated_data)