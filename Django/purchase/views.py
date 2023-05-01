from django.http import HttpResponse, JsonResponse
from .models import Purchase, PurchaseForm
from django.views.generic import ListView, CreateView, DetailView
from django.shortcuts import render
from django.urls import reverse_lazy


# def all_purchases_json(request):
#    all_purchases = Purchase.objects.all().values("id", "user_id", "book_id", "date")
#    purchase_list = list(all_purchases)
#    return JsonResponse(purchase_list, safe=False)

class ListPurchases(ListView):
    model = Purchase


class GetPurchaseId(DetailView):
    model = Purchase


class PurchaseCreate(CreateView):
    form_class = PurchaseForm
    template_name = "purchase/purchase_form.html"
    success_url = reverse_lazy("purchases-list")

