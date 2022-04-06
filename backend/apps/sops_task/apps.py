from multiprocessing.spawn import import_main_path
from django.apps import AppConfig
from celery.schedules import crontab

from blueapps.core.celery import celery_app


class SopsTaskConfig(AppConfig):
    name = "apps.sops_task"

    def ready(self) -> None:
        from apps.sops_task.celery.tasks import update_sops_task_status  # noqa
        celery_app.conf.beat_schedule = {
            # Executes at sunset in Melbourne
            "update_sops_task_status": {
                "task": "apps.sops_task.celery.tasks.update_sops_task_status",
                "schedule": crontab(minute=1),
            },
        }
