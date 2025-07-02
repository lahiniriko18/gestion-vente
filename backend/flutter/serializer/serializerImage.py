from rest_framework import serializers
from ..models import Image,Produit

class ImageSerializer(serializers.ModelSerializer):
    numProduit = serializers.PrimaryKeyRelatedField(
        queryset=Produit.objects.all(),
        error_messages={
            'does_not_exist': "Ce produit spécifié n'existe pas !",
            'incorrect_type': "Le format de l'ID de ce produit est invalide !",
        }
    )

    class Meta:
        model=Image
        fields=["numImage","numProduit","nomImage"]
    
    def validate(self, data):
        return data
    
    def create(self, validated_data):
        return Image.objects.create(**validated_data)