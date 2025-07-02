from django.urls import path
from ..views.viewsCommande import CommandeView,CommandeDetailView

urlpatterns = [
    path('', CommandeView.as_view()),
    path('ajouter/', CommandeView.as_view()),
    path('modifier/<int:numCommande>', CommandeView.as_view()),
    path('supprimer/<int:numCommande>', CommandeView.as_view()),
    path('dernier-commande/', CommandeDetailView.as_view()),
]