from django.http import HttpResponse, JsonResponse
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
import django_filters
from rest_framework.viewsets import ModelViewSet
from .models import Purchase, PurchaseForm
from django.views.generic import ListView, CreateView, DetailView
from django.shortcuts import render
from django.urls import reverse_lazy
from .serializes import PurchaseSerializer


# def all_purchases_json(request):
#    all_purchases = Purchase.objects.all().values("id", "user_id", "book_id", "date")
#    purchase_list = list(all_purchases)
#    return JsonResponse(purchase_list, safe=False)

# class ListPurchases(ListView):
#    model = Purchase


# class GetPurchaseId(DetailView):
#    model = Purchase


# class PurchaseCreate(CreateView):
#    form_class = PurchaseForm
#    template_name = "purchase/purchase_form.html"
#    success_url = reverse_lazy("purchases-list")

class CustomPaginator(PageNumberPagination):
    page_size_query_param = 'page_size'


class PurchaseListView(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    pagination_class = CustomPaginator
    search_fields = ['user.last_name', 'book.author', 'book.title']
    ordering_fields = ['date']
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        SearchFilter, OrderingFilter
    ]
