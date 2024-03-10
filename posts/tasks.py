from celery.utils.log import get_task_logger
from blog.celery import app
from django.utils import timezone
from .models import Post


__all__ = ("update_time",)


logger = get_task_logger(__name__)


@app.task
def update_time():
    logger.info("Running date updates")
    for post in Post.objects.all():
        post.date = timezone.now()
        post.save()
