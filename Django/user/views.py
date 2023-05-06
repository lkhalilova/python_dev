from django.http import HttpResponse, JsonResponse
from .models import User
from .models import User, UserForm
from django.views.generic import ListView, CreateView, DetailView
from django.shortcuts import render
from django.urls import reverse_lazy


# def all_users_json(request):
#    all_users = User.objects.all().values("id", "first_name", "last_name", "age")
#    user_list = list(all_users)
#    return JsonResponse(user_list, safe=False)

class ListUsers(ListView):
    model = User


class GetUserId(DetailView):
    model = User


class UserCreate(CreateView):
    form_class = UserForm
    template_name = "user/user_form.html"
    success_url = reverse_lazy("users-list")




