from django.urls import include, path
from .views import article_new, article_edit, article_list, bilan_irr, cherche_article, recherche


urlpatterns = [
    path('article/new/', article_new, name='article_new'),
    path('article/<int:pk>/edit/', article_edit, name='article_edit'),
    path('', article_list, name='article_list'),
    path('irr/<int:volet>/', bilan_irr, name='bilan_irr'),
    path('verif/<int:doc>/<int:volet>/', cherche_article, name='cherche_article'),
    path('recherche/', recherche, name='recherche'),

]
