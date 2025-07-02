from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializer.serializerClassement import ClassementSerializer
from ..models import Classement

class ClassementView(APIView):
    def get(self, request):
        classements = Classement.objects.all().order_by('-numClassement')
        serializer = ClassementSerializer(classements, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ClassementSerializer(data=request.data)
        if serializer.is_valid():
            classement = serializer.save()
            return Response(ClassementSerializer(classement).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, numClassement):
        classement =  Classement.objects.filter(pk=numClassement).first()
        if classement:
            serializer = ClassementSerializer(classement, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(ClassementSerializer(classement).data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"erreur":"Classement introuvable !"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, numClassement):
        classement =  Classement.objects.filter(pk=numClassement).first()
        if classement:
            classement.delete()
            return Response({"message":"Suppression avec succès !"}, status=status.HTTP_200_OK)
        return Response({"erreur":"Classement introuvable !"}, status=status.HTTP_404_NOT_FOUND)