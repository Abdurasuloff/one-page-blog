from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('article/<int:id>/detail/', views.article_detail, name="article_detail"),
    path('article/<int:id>/update/', views.article_update, name="article_update"),
    path('article/<int:id>/delete/', views.article_delete, name="article_delete"),
    path('article/create/', views.article_create, name="article_create"),
]