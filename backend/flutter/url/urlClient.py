from django.urls import path
from ..views.viewsClient import ClientView

urlpatterns = [
    path('', ClientView.as_view()),
    path('ajouter/', ClientView.as_view()),
    path('modifier/<int:numClient>', ClientView.as_view()),
    path('supprimer/<int:numClient>', ClientView.as_view()),
]