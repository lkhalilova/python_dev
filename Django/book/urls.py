from django.urls import path
from .views import ListBooks, GetBookId, BookCreate


urlpatterns = [
    path("", ListBooks.as_view(), name="books-list"),
    path("detail/<int:id>", GetBookId.as_view(), name="book-id"),
    path("create", BookCreate.as_view(), name="book-create")
]
