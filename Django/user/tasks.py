from celery import shared_task
from user.models import User


@shared_task
def user_task():
    print("You can't get here if it is not your turn")


@shared_task
def purchase_count(user_id):
    queried_user = User.objects.get(id=user_id)
    purchases_amount = queried_user.purchases.count()
    return f"This user has made {purchases_amount} purchases"


@shared_task
def user_amount():
    return f"Users amount: {User.objects.all.count()}"

