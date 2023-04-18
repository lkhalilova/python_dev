from django.urls import path
from .views import all_books_json


urlpatterns = [
    path("", all_books_json, name="all_books_json"),
]