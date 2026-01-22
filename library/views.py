from django.shortcuts import render
import datetime as dt
from .models import Book


def index(request):
    books = Book.objects.all()
    return render(
        request, "library/index.html", {"books": books, "now": dt.datetime.now()}
    )


def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, "library/book_detail.html", {"book": book, "now": dt.datetime.now()})
