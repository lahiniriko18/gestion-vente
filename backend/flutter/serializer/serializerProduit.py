from rest_framework import serializers
from ..models import Produit,Classement,Categorie
from .serializerCategorie import CategorieSerializer
from .serializerClassement import ClassementSerializer

class ProduitSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    numClassement = serializers.PrimaryKeyRelatedField(
        queryset=Classement.objects.all(),
        allow_null = True,
        required =False,
        error_messages={
            'does_not_exist': "Ce classement spécifié n'existe pas !",
            'incorrect_type': "Le format de l'ID du classement est invalide !",
        },
    )
    numCategorie = serializers.PrimaryKeyRelatedField(
        queryset=Categorie.objects.all(),
        error_messages={
            'does_not_exist': "Ce categorie spécifié n'existe pas !",
            'incorrect_type': "Le format de l'ID du categorie est invalide !",
        }
    )
    qrCode = serializers.ImageField(
        allow_null = True,
        required = False
    )

    class Meta:
        model=Produit
        fields=[
            "numProduit",
            "numClassement",
            "numCategorie",
            "libelleProduit",
            "quantite",
            "prixUnitaire",
            "uniteMesure",
            "description",
            "qrCode",
            "images"
        ]
    
    def get_images(self, obj):
        request = self.context.get('request')
        return [
            request.build_absolute_uri(image.nomImage.url)
            for image in obj.images.all() if image.nomImage
        ]
    def validate(self, data):
        donnee=data
        return donnee
    
    def create(self, validated_data):
        return Produit.objects.create(**validated_data)