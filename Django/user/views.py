from django.http import HttpResponse, JsonResponse
from .models import User


def all_users_json(request):
    all_users = User.objects.all().values("id", "first_name", "last_name", "age")
    user_list = list(all_users)
    return JsonResponse(user_list, safe=False)




