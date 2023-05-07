import django_filters
from django.http import HttpResponse, JsonResponse
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from .models import User, UserForm
from django.views.generic import ListView, CreateView, DetailView
from django.shortcuts import render
from django.urls import reverse_lazy
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer


# def all_users_json(request):
#    all_users = User.objects.all().values("id", "first_name", "last_name", "age")
#    user_list = list(all_users)
#    return JsonResponse(user_list, safe=False)

# class ListUsers(ListView):
#    model = User


#class GetUserId(DetailView):
#    model = User


#class UserCreate(CreateView):
#    form_class = UserForm
#    template_name = "user/user_form.html"
#    success_url = reverse_lazy("users-list")

class CustomPaginator(PageNumberPagination):
    page_size_query_param = 'page_size'


class UserListView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = CustomPaginator
    search_fields = ['last_name']
    ordering_fields = ['age']
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        SearchFilter, OrderingFilter
    ]



