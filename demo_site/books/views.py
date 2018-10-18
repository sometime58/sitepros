from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Book


def index(request):
    # connecting to the database and get info from it
    all_books = Book.objects.all()

    # template directory has to be named .templates.name_of_the_app
    # template = loader.get_template('books/index.html')

    # create a context to pass in the data
    context = {
        'all_books': all_books
    }
    return render(request, 'books/index.html', context)


def detail(request, book_id):
    try:
        # make sure book can get
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        # DoesNotExist works with classes
        raise Http404('Book you are looking for does not exist')
    # return HttpResponse('<h2> Details for Book ID: ' + str(book_id) + '</h2>')
    return render(request, 'books/detail.html', {'book': book})