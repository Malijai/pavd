from django.urls import include, path
from .views import article_new, article_edit, article_list


urlpatterns = [
    path('article/new/', article_new, name='article_new'),
    path('article/<int:pk>/edit/', article_edit, name='article_edit'),
    path('', article_list, name='article_list'),
]
