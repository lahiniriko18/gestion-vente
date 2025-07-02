from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializer.serializerComprendre import ComprendreSerializer
from ..models import Comprendre

class ComprendreView(APIView):
    def get(self, request):
        comprendres = Comprendre.objects.all().order_by('-numComprendre')
        serializer = ComprendreSerializer(comprendres, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ComprendreSerializer(data=request.data)
        if serializer.is_valid():
            comprendre = serializer.save()
            return Response(ComprendreSerializer(comprendre).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, numComprendre):
        comprendre =  Comprendre.objects.filter(pk=numComprendre).first()
        if comprendre:
            serializer = ComprendreSerializer(comprendre, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(ComprendreSerializer(comprendre).data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"erreur":"Comprendre introuvable !"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, numComprendre):
        comprendre =  Comprendre.objects.filter(pk=numComprendre).first()
        if comprendre:
            comprendre.delete()
            return Response({"message":"Suppression avec succès !"}, status=status.HTTP_200_OK)
        return Response({"erreur":"Comprendre introuvable !"}, status=status.HTTP_404_NOT_FOUND)