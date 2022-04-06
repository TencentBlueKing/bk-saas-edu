import os
import logging
from blueapps.core.celery import celery_app
from bkapi.bk_sops.shortcuts import get_client_by_username as get_sops_client_by_username
from bkapi_component.open.shortcuts import get_client_by_username

from apps.sops_task.models import Tasks
from apps.sops_task.constants import TaskStatus

logger = logging.getLogger("celery")


@celery_app.task
def update_sops_task_status():
    tasks = Tasks.objects.exclude(status__in=[TaskStatus.FINISHED, TaskStatus.REVOKED])
    client = get_sops_client_by_username(os.getenv("SOPS_TASK_STATUS_SYNC_USER", "admin"))
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
        if task_status_result["data"]["state"] == TaskStatus.FINISHED:
            notify_task_finished.delay(task_id=task.task_id, task_creator=task.created_by)
        task.status = task_status_result["data"]["state"]
        task.save()


@celery_app.task
def notify_task_finished(task_id, task_creator):
    client = get_client_by_username(os.getenv("SOPS_TASK_FINISH_NOTIFY_USER", "admin"))
    send_mail_result = client.cmsi.send_mail(
        receiver__username=task_creator, title="标准运维任务执行完成", content="您的标准运维任务(ID:{})已经执行完成".format(task_id)
    )
    logger.info("[notify_task_finished] task %s finish message send result: %s", task_id, send_mail_result)
