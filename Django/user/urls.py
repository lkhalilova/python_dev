from django.urls import path
from .views import all_users_json


urlpatterns = [
    path("", all_users_json, name="all_users_json"),
]