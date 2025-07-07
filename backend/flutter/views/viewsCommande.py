from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions
from ..serializer.serializerCommande import CommandeSerializer
from ..serializer.serializerComprendre import ComprendreSerializer
from ..models import Commande

class CommandeView(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        commandes = Commande.objects.all().order_by('-numCommande')
        serializer = CommandeSerializer(commandes, many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        donnee = request.data
        donneProduits = donnee.get('produits', [])
        donneCommande = {
            "reference":donnee.get('reference'),
            "numClient":donnee.get('numClient')
        }
        serializer = CommandeSerializer(data=donneCommande)
        if serializer.is_valid():
            commande = serializer.save()
            for dp in donneProduits:
                donneComprendre = {
                    "numCommande":commande.numCommande,
                    "numProduit":dp['numProduit'],
                    "quantiteCommande": dp['quantiteCommande']
                }
                serializerComprendre = ComprendreSerializer(data = donneComprendre)
                if serializerComprendre.is_valid():
                    comprendre = serializerComprendre.save()
            return Response(CommandeSerializer(commande, context={'request':request}).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, numCommande):
        commande =  Commande.objects.filter(pk=numCommande).first()
        if commande:
            serializer = CommandeSerializer(commande, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(CommandeSerializer(commande, context={'request':request}).data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"erreur":"Commande introuvable !"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, numCommande):
        commande =  Commande.objects.filter(pk=numCommande).first()
        if commande:
            commande.delete()
            return Response({"message":"Suppression avec succès !"}, status=status.HTTP_200_OK)
        return Response({"erreur":"Commande introuvable !"}, status=status.HTTP_404_NOT_FOUND)


class CommandeDetailView(APIView):
    def get(self, request):
        commandes = Commande.objects.order_by('-numCommande')[:2]
        if commandes:
            return Response(CommandeSerializer(commandes, many=True, context={'request':request}).data, status=status.HTTP_200_OK)
        return Response([], status=status.HTTP_200_OK)