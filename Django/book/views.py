from django.http import HttpResponse, JsonResponse
from .models import Book


def all_books_json(request):
    all_books = Book.objects.all().values("id", "title", "author", "year", "price")
    book_list = list(all_books)
    return JsonResponse(book_list, safe=False)
