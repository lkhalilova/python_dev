from django.urls import path
from rest_framework.routers import SimpleRouter

# from .views import ListUsers, GetUserId, UserCreate
from .views import UserListView

urlpatterns = [
#    path("", ListUsers.as_view(), name="users-list"),
#    path("detail/<int:pk>", GetUserId.as_view(), name="user-id"),
#    path("create", UserCreate.as_view(), name="user-create")
]


router = SimpleRouter()
router.register("", UserListView)

urlpatterns += router.urls