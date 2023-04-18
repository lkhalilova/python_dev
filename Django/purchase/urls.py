from django.urls import path
from .views import all_purchases_json


urlpatterns = [
    path("", all_purchases_json, name="all_purchases_json"),
]