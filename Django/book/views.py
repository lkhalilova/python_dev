from django.http import HttpResponse, JsonResponse
from .models import Book, BookForm
from django.views.generic import ListView, CreateView, DetailView
from django.shortcuts import render
from django.urls import reverse_lazy


# def all_books_json(request):
#    all_books = Book.objects.all().values("id", "title", "author", "year", "price")
#    book_list = list(all_books)
#    return JsonResponse(book_list, safe=False)


class ListBooks(ListView):
    model = Book


class GetBookId(DetailView):
    model = Book


class BookCreate(CreateView):
    form_class = BookForm
    template_name = "book/book_form.html"
    success_url = reverse_lazy("books-list")


