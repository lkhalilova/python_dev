from django.urls import path
from rest_framework.routers import SimpleRouter

# from .views import ListPurchases, GetPurchaseId, PurchaseCreate
from .views import PurchaseListView


urlpatterns = [
#    path("", ListPurchases.as_view(), name="purchases-list"),
#    path("detail/<int:pk>", GetPurchaseId.as_view(), name="purchase-id"),
#    path("create", PurchaseCreate.as_view(), name="purchase-create")
]

router = SimpleRouter()
router.register("", PurchaseListView)

urlpatterns += router.urls


