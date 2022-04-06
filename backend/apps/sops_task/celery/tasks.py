import os
import logging
from blueapps.core.celery import celery_app
from bkapi.bk_sops.shortcuts import get_client_by_username

from apps.sops_task.models import Tasks
from apps.sops_task.constants import TaskStatus

logger = logging.getLogger("celery")


@celery_app.task
def update_sops_task_status():
    tasks = Tasks.objects.exclude(status__in=[TaskStatus.FINISHED, TaskStatus.REVOKED])
    client = get_client_by_username(os.getenv("SOPS_TASK_STATUS_SYNC_USER", "admin"))
    logger.info("[update_sops_task_status] get %s not finish tasks", len(tasks))
    for task in tasks:
        task_status_result = client.api.get_task_status(
            path_params={
                "task_id": task.task_id,
                "bk_biz_id": task.bk_biz_id,
            }
        )
        logger.info(
            "[update_sops_task_status] get_task_status for task %s return: %s", task.task_id, task_status_result
        )
        if not task_status_result["result"]:
            continue
        task.status = task_status_result["data"]["state"]
        task.save()
