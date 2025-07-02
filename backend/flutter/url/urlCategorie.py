from django.urls import path
from ..views.viewsCategorie import CategorieView

urlpatterns = [
    path('', CategorieView.as_view()),
    path('ajouter/', CategorieView.as_view()),
    path('modifier/<int:numCategorie>', CategorieView.as_view()),
    path('supprimer/<int:numCategorie>', CategorieView.as_view()),
]