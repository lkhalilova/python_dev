from django.http import HttpResponse, JsonResponse
from .models import Purchase


def all_purchases_json(request):
    all_purchases = Purchase.objects.all().values("id", "user_id", "book_id", "date")
    purchase_list = list(all_purchases)
    return JsonResponse(purchase_list, safe=False)

