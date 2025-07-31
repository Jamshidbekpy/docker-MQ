from celery import Celery
import os
from dotenv import load_dotenv

load_dotenv()

celery_app = Celery(
    "worker",
    broker=os.getenv("CELERY_BROKER_URL"),
    backend=os.getenv("CELERY_RESULT_BACKEND"),
)

from .beat_schedule import beat_schedule

celery_app.conf.beat_schedule = beat_schedule
celery_app.conf.timezone = 'Asia/Tashkent'
from app.worker.tasks import arithmetic # noqa