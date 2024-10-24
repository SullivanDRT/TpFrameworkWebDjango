from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import Book
from .forms import BookForms

# Create your views here.
def about(request):
    return render(request, "bonnes_lectures/about.html")

def welcome(request):
    return render(request, "bonnes_lectures/welcome.html")

def books(request):
    books = Book.objects.all()
    context = { "books" : books}
    return render(request,"bonnes_lectures/meslivres.html" , context)

def book_detail(request, book_id):
    try:
        book = get_object_or_404(Book, id=book_id)
    except Book.DoesNotExist:
        raise Http404("Le Livre n'existe pas")
    context = {'book' : book}
    return render(request, "bonnes_lectures/book_detail.html", context)

def ajouter_livre(request):
    if request.method == 'POST':
        form = BookForms(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = BookForms()
    context = {'form' : form}
    return render(request, "bonnes_lectures/ajouter_livre.html", context)


def supprimer_livre(request,book_id):
    try:
        book = get_object_or_404(Book, id=book_id)
    except Book.DoesNotExist:
        raise Http404("Le Livre n'existe pas")
    if request.method == "GET":
        book.delete()
        return redirect('books')
    context = {'book': book}
    return book_detail(request, book_id)

def modifier_livre(request, book_id):
    try:
        book = get_object_or_404(Book, id=book_id)
    except Book.DoesNotExist:
        raise Http404("Le Livre n'existe pas")
    
    if request.method == "POST":
        form = BookForms(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', book_id=book_id)
    else:
        form = BookForms(instance=book)
        context = {'form' : form, 'book': book}
        return render(request, "bonnes_lectures/modifier_livre.html", context)