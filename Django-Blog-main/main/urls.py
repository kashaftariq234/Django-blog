from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("article/<int:id>", views.article, name="article"),
    path("author/<int:id>", views.author, name="author"),
    path("article", views.add_article, name="add_article"),
    path("article/edit/<int:id>", views.edit_article, name="edit_article"),
    path("author", views.add_author, name="add_author"),
    path("author/edit/<int:id>", views.edit_author, name="edit_author"),
]
