from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializer.serializerClient import ClientSerializer
from ..models import Client

class ClientView(APIView):
    def get(self, request):
        clients = Client.objects.all().order_by('-numClient')
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        print(request.data)
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            client = serializer.save()
            return Response(ClientSerializer(client).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, numClient):
        client =  Client.objects.filter(pk=numClient).first()
        if client:
            serializer = ClientSerializer(client, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(ClientSerializer(client).data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"erreur":"Client introuvable !"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, numClient):
        client =  Client.objects.filter(pk=numClient).first()
        if client:
            client.delete()
            return Response({"message":"Suppression avec succès !"}, status=status.HTTP_200_OK)
        return Response({"erreur":"Client introuvable !"}, status=status.HTTP_404_NOT_FOUND)