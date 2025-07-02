from rest_framework import serializers
from ..models import Classement

class ClassementSerializer(serializers.ModelSerializer):

    class Meta:
        model=Classement
        fields=["numClassement","nomClassement","quantiteMin","quantiteMax","descClassement"]
    def validate(self, data):
        if data['quantiteMin'] > data['quantiteMax']:
            raise serializers.ValidationError(
                {"erreur":"La quantité minimale doit inférieure au quantité maximale!"}
            )
        return data
    
    def create(self, validated_data):
        return Classement.objects.create(**validated_data)