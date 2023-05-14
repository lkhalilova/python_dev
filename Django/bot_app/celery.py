from celery import Celery
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bot_app.settings")

app = Celery("bot_app")

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat.schedule = {
    "amount_updater": {
        "task": "user.tasks.user_amount",
        "schedule": 60,
        "args": (),
        "kwargs": {},

    }
}