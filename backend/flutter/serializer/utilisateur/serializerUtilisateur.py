from rest_framework import serializers
from django.contrib.auth import get_user_model

Utilisateur = get_user_model()
import re
class UtilisateurSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only= True)
    
    class Meta:
        model=Utilisateur
        fields=[
            'id', 
            'username', 
            'email', 
            'password', 
            'contact', 
            'adresse', 
            'image', 
            'first_name', 
            'last_name'
        ]
    def validate_contact(self, value):
        contactFiltrer=value.replace(" ","")
        pattern=r'^(?:\+261|0)(20|32|33|34|37|38)\d{7}$'
        if not re.match(pattern, contactFiltrer):
            raise serializers.ValidationError({"erreur":"Contact invalide !"})
        if re.match(r'^\+261',contactFiltrer):
            return f"+261 {contactFiltrer[4:6]} {contactFiltrer[6:8]} {contactFiltrer[8:11]} {contactFiltrer[11:13]}"
        return f"{contactFiltrer[0:3]} {contactFiltrer[3:5]} {contactFiltrer[5:8]} {contactFiltrer[8:10]}"

    def validate(self, data):
        return data
    
class InscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        utilisateur = Utilisateur.objects.create_user(**validated_data)
        return utilisateur

class ModifierUtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields=[
            'contact', 
            'adresse', 
            'image', 
            'first_name', 
            'last_name'
        ]

    def validate_contact(self, value):
        contactFiltrer=value.replace(" ","")
        pattern=r'^(?:\+261|0)(20|32|33|34|37|38)\d{7}$'
        if not re.match(pattern, contactFiltrer):
            raise serializers.ValidationError({"erreur":"Contact invalide !"})
        if re.match(r'^\+261',contactFiltrer):
            return f"+261 {contactFiltrer[4:6]} {contactFiltrer[6:8]} {contactFiltrer[8:11]} {contactFiltrer[11:13]}"
        return f"{contactFiltrer[0:3]} {contactFiltrer[3:5]} {contactFiltrer[5:8]} {contactFiltrer[8:10]}"

    def validate(self, data):
        return data