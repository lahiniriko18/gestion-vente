from rest_framework import serializers
from ..models import Client
import re

class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model=Client
        fields=["numClient","nom","contact","adresse"]
    
    def validate_contact(self,value):
        contactFiltrer=value.replace(" ","")
        pattern=r'^(?:\+261|0)(20|32|33|34|37|38)\d{7}$'
        if not re.match(pattern, contactFiltrer):
            raise serializers.ValidationError({"erreur":"Contact invalide !"})
        if re.match(r'^\+261',contactFiltrer):
            return f"+261 {contactFiltrer[4:6]} {contactFiltrer[6:8]} {contactFiltrer[8:11]} {contactFiltrer[11:13]}"
        return f"{contactFiltrer[0:3]} {contactFiltrer[3:5]} {contactFiltrer[5:8]} {contactFiltrer[8:10]}"
        
    def validate(self, data):
        return data
    
    def create(self, validated_data):
        return Client.objects.create(**validated_data)