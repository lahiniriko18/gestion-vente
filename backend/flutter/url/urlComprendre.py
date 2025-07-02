from django.urls import path
from ..views.viewsComprendre import ComprendreView

urlpatterns = [
    path('', ComprendreView.as_view()),
    path('ajouter/', ComprendreView.as_view()),
    path('modifier/<int:numComprendre>', ComprendreView.as_view()),
    path('supprimer/<int:numComprendre>', ComprendreView.as_view()),
]