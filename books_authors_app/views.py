from django.shortcuts import render, redirect
from .models import Book, Author

# Create your views here.

def index(request):
    context = {"book_list": Book.objects.all()}
    return render(request, "book.html", context)


def process_books(request):
    if request.method == "POST":
        title = request.POST["title"]
        desc = request.POST["desc"]

        Book.objects.create(title=title, desc=desc)
    return redirect ('/')

def book_detail(request, val):
    pass
    context = {"current_book": Book.objects.get(id=val),
               "author_list": Author.objects.all()
    }
    return render(request, "book_detail.html", context)

def add_author(request):
    if request.method == "POST":
        this_book = Book.objects.get(id=request.POST["book_id"])
        this_author = Author.objects.get(id=request.POST["new_author"])
        this_book.authors.add(this_author)
    return redirect ('/')
    
        
def authors(request):
    context = {"author_list": Author.objects.all()}
    return render(request, "author.html", context)    

def process_authors(request):
    if request.method == "POST":
        first = request.POST["first_name"]
        last = request.POST["last_name"]
        notes = request.POST["notes"]

        Author.objects.create(first_name=first, last_name= last, notes = notes)
    return redirect ('/authors')

def author_detail(request, val):
    pass
    context = {"current_author": Author.objects.get(id=val),
               "book_list": Book.objects.all()
    }
    return render(request, "author_detail.html", context)

def add_book(request):
    if request.method == "POST":
        this_book = Book.objects.get(id=request.POST["new_book"])
        this_author = Author.objects.get(id=request.POST["author_id"])
        this_author.books.add(this_book)
    return redirect ('/authors')
