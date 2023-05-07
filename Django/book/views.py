from django.http import HttpResponse, JsonResponse
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Book, BookForm
from django.views.generic import ListView, CreateView, DetailView
from django.shortcuts import render
from django.urls import reverse_lazy
from rest_framework.viewsets import ModelViewSet
from .serializers import BookSerializer
import django_filters


# def all_books_json(request):
#    all_books = Book.objects.all().values("id", "title", "author", "year", "price")
#    book_list = list(all_books)
#    return JsonResponse(book_list, safe=False)


# class ListBooks(ListView):
#    model = Book


#class GetBookId(DetailView):
#    model = Book


# class BookCreate(CreateView):
#    form_class = BookForm
#    template_name = "book/book_form.html"
#    success_url = reverse_lazy("books-list")

class CustomPaginator(PageNumberPagination):
    page_size_query_param = 'page_size'


class BookListView(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = CustomPaginator
    search_fields = ['title', 'author']
    ordering_fields = ['price']
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        SearchFilter, OrderingFilter
    ]


