from django.urls import path
from ..views.viewsImage import ImageView

urlpatterns = [
    path('', ImageView.as_view()),
    path('ajouter/', ImageView.as_view()),
    path('modifier/<int:numImage>', ImageView.as_view()),
    path('supprimer/<int:numImage>', ImageView.as_view()),
]