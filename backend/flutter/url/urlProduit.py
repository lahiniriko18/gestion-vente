from django.urls import path
from ..views.viewsProduit import ProduitView,ProduitDetailView,ProduitCommandeView

urlpatterns = [
    path('', ProduitView.as_view()),
    path('<str:numProduit>', ProduitDetailView.as_view()),
    path('ajouter/', ProduitView.as_view()),
    path('modifier/<int:numProduit>', ProduitView.as_view()),
    path('supprimer/<int:numProduit>', ProduitView.as_view()),
    path('produit-commande/', ProduitCommandeView.as_view()),
    path('verifier-produit/', ProduitDetailView.as_view()),
]