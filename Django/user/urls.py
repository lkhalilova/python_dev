from django.urls import path
from .views import ListUsers, GetUserId, UserCreate


urlpatterns = [
    path("", ListUsers.as_view(), name="users-list"),
    path("detail/<int:pk>", GetUserId.as_view(), name="user-id"),
    path("create", UserCreate.as_view(), name="user-create")
]