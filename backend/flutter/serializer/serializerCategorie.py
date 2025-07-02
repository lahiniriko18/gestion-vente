from rest_framework import serializers
from ..models import Categorie

class CategorieSerializer(serializers.ModelSerializer):

    class Meta:
        model=Categorie
        fields=["numCategorie","nomCategorie","imageCategorie","descCategorie"]

    def validate(self, data):
        return data
    
    def create(self, validated_data):
        return Categorie.objects.create(**validated_data)