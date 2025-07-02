from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions
from django.db.models import Count
from ..serializer.serializerProduit import ProduitSerializer
from ..models import Produit

class ProduitView(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        produits = Produit.objects.all().order_by('-numProduit')
        serializer = ProduitSerializer(produits, many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ProduitSerializer(data=request.data)
        if serializer.is_valid():
            produit = serializer.save()
            produit.gererQrCode()
            return Response(ProduitSerializer(produit, context={'request':request}).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, numProduit):
        produit = Produit.objects.filter(pk=numProduit).first()
        if produit:
            serializer = ProduitSerializer(produit, data=request.data, context={'request':request})
            if serializer.is_valid():
                serializer.save()
                return Response(ProduitSerializer(produit, context={'request':request}).data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"erreur":"Produit introuvable !"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, numProduit):
        produit =  Produit.objects.filter(pk=numProduit).first()
        if produit:
            produit.delete()
            return Response({"message":"Suppression avec succès !"}, status=status.HTTP_200_OK)
        return Response({"erreur":"Produit introuvable !"}, status=status.HTTP_404_NOT_FOUND)


class ProduitDetailView(APIView):
    def get(self, request, numProduit):
        if numProduit.isdigit():
            produit = Produit.objects.filter(pk=int(numProduit)).first()
            if produit:
                return Response(ProduitSerializer(produit, context={'request':request}).data, status=status.HTTP_200_OK)
            return Response({"erreur":"Produit introuvable !"}, status=status.HTTP_404_NOT_FOUND)
        return Response({"erreur":"Produit introuvable !"}, status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request):
        data=request.data
        quantite = data.get('quantite')
        numProduit = data.get('numProduit')
        verif = Produit.objects.filter(numProduit=numProduit, quantite__gte=quantite).exists()
        return Response({"valeur":verif}, status=status.HTTP_200_OK)

class ProduitCommandeView(APIView):
    def get(self, request):
        produit = Produit.objects.annotate(totalCommandes=Count('comprendres')).order_by('-totalCommandes').first()
        if produit:
            return Response(ProduitSerializer(produit, context={'request':request}).data, status=status.HTTP_200_OK)
        return Response({"erreur":"Aucun produit commandé"}, status=status.HTTP_404_NOT_FOUND)
            