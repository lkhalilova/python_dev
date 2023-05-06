from django.urls import path
from .views import ListPurchases, GetPurchaseId, PurchaseCreate


urlpatterns = [
    path("", ListPurchases.as_view(), name="purchases-list"),
    path("detail/<int:pk>", GetPurchaseId.as_view(), name="purchase-id"),
    path("create", PurchaseCreate.as_view(), name="purchase-create")
]


