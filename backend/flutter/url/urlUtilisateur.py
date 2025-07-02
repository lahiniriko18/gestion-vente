from django.urls import path
from ..views.viewsUtilisateur import InscriptionView,ChangeMdpView,ConnexionView,DeconnexionView,ProfileView,ModifierProfileView
from rest_framework_simplejwt.views import (
    TokenRefreshView
)

urlpatterns = [
    path('inscription/', InscriptionView.as_view()),
    path('connexion/', ConnexionView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('deconnexion/', DeconnexionView.as_view()),
    path('profile/', ProfileView.as_view()),
    path('modifier-profile/', ModifierProfileView.as_view()),
    path('modifier-mdp/', ChangeMdpView.as_view()),
    
]