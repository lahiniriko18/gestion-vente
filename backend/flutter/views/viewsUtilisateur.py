from rest_framework_simplejwt.views import TokenObtainPairView
from ..serializer.utilisateur.serializerConnexion import ConnexionSerializer
from ..serializer.utilisateur.serializerUtilisateur import InscriptionSerializer,ModifierUtilisateurSerializer,UtilisateurSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken
from flutter.models import Utilisateur

class ProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        utilisateur = request.user
        serializer = UtilisateurSerializer(utilisateur)
        return Response(serializer.data)

class InscriptionView(APIView):
    def post(self, request):
        data=request.data
        serializer = InscriptionSerializer(data=data)
        if serializer.is_valid():
            utilisateur = serializer.save()
            return Response(UtilisateurSerializer(utilisateur).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ConnexionView(TokenObtainPairView):
    serializer_class = ConnexionSerializer

class DeconnexionView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Déconnexion réussie."}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"erreur": "Token invalide ou manquant"}, status=status.HTTP_400_BAD_REQUEST)

class ChangeMdpView(APIView):    
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        utilisateur = request.user
        ancienMdp = request.data.get("ancienMdp")
        nouveauMdp = request.data.get("nouveauMdp")

        if not utilisateur.check_password(ancienMdp):
            return Response({"erreur": "Ancien mot de passe incorrect"}, status=status.HTTP_400_BAD_REQUEST)

        utilisateur.set_password(nouveauMdp)
        utilisateur.save()
        return Response({"message": "Mot de passe modifié avec succès"})
    
class ModifierProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request):
        utilisateur = request.user
        serializer = ModifierUtilisateurSerializer(utilisateur, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Profil mis à jour avec succès"})
        return Response(serializer.errors, status=400)
