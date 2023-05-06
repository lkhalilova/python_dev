from django.urls import path
#from .views import ListBooks, GetBookId, BookCreate
from rest_framework.routers import SimpleRouter
from .views import BookListView


urlpatterns = [
#    path("", ListBooks.as_view(), name="books-list"),
#    path("detail/<int:pk>", GetBookId.as_view(), name="book-id"),
#    path("create", BookCreate.as_view(), name="book-create"),

]

router = SimpleRouter()
router.register("", BookListView)

urlpatterns += router.urls

