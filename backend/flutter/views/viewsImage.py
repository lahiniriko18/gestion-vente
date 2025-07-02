from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializer.serializerImage import ImageSerializer
from ..models import Image

class ImageView(APIView):
    def get(self, request):
        images = Image.objects.all().order_by('-numImage')
        serializer = ImageSerializer(images, many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            image = serializer.save()
            return Response(ImageSerializer(image, context={'request':request}).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, numImage):
        image =  Image.objects.filter(pk=numImage).first()
        if image:
            serializer = ImageSerializer(image, data=request.data, context={'request':request})
            if serializer.is_valid():
                serializer.save()
                return Response(ImageSerializer(image, context={'request':request}).data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"erreur":"Image introuvable !"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, numImage):
        image =  Image.objects.filter(pk=numImage).first()
        if image:   
            image.delete()
            return Response({"message":"Suppression avec succès !"}, status=status.HTTP_200_OK)
        return Response({"erreur":"Image introuvable !"}, status=status.HTTP_404_NOT_FOUND)