from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("about/", views.about, name="about"),
    path("welcome/", views.welcome, name="welcome"),
    path("books/", views.books, name="books"),
    path("bookDetail/<int:book_id>/", views.book_detail, name="book_detail"),
    path("ajouterLivre/", views.ajouter_livre, name="ajouter_livre"),
    path("books/supprimerLivre/<int:book_id>/", views.supprimer_livre, name="supprimer_livre"),
    path("books/modifierLivre/<int:book_id>/", views.modifier_livre, name="modifier_livre"),
]