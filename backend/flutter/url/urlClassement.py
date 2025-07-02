from django.urls import path
from ..views.viewsClassement import ClassementView

urlpatterns = [
    path('', ClassementView.as_view()),
    path('ajouter/', ClassementView.as_view()),
    path('modifier/<int:numClassement>', ClassementView.as_view()),
    path('supprimer/<int:numClassement>', ClassementView.as_view()),
]