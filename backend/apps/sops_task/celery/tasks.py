from blueapps.core.celery import celery_app
from apps.sops_task.handlers import TaskHandler


@celery_app.task
def update_sops_task_status():
    TaskHandler().sync()
