from django.urls import path,include
from .url import urlUtilisateur,urlCategorie,urlClassement,urlClient,urlCommande,urlComprendre,urlImage,urlProduit

urlpatterns = [
    path('classement/', include(urlClassement)),
    path('categorie/', include(urlCategorie)),
    path('produit/', include(urlProduit)),
    path('image/', include(urlImage)),
    path('client/', include(urlClient)),
    path('commande/', include(urlCommande)),
    path('comprendre/', include(urlComprendre)),
    path('user/', include(urlUtilisateur)),
]