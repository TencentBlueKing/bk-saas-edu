# -*- coding: utf-8 -*-
from django.forms.models import model_to_dict
from rest_framework.exceptions import ValidationError

from apps.drf import DataPageNumberPagination
from apps.sops_task.constants import (
    SOPS_TASK_STATUS_RESULT,
    DEFAULT_TEMPLATE_LIST,
    GET_TEMPLATE_INFO_RESULT,
    CREATE_TASK_RESULT,
    START_TASK_RESULT,
    TaskStatus,
    DEFAULT_CC_BIZ_RESULT,
)
from apps.sops_task.models import Tasks


class TaskHandler(object):
    def list(self, request, view):
        pg = DataPageNumberPagination()
        page_sops_tasks = pg.paginate_queryset(
            queryset=Tasks.objects.all()
            .order_by("-created_at", "created_by")
            .values(
                "id",
                "task_name",
                "task_id",
                "task_url",
                "bk_biz_id",
                "template_id",
                "created_by",
                "created_at",
                "status",
            ),
            request=request,
            view=view,
        )
        res = pg.get_paginated_response(page_sops_tasks)
        return res

    def create(self, request, bk_biz_id, template_id, task_name, params):
        user_name = request.user.username
        create_task_result = SopsHandler.call_create_task(
            task_name=task_name, params=params
        )
        SopsHandler.call_start_task(create_task_result["data"]["task_id"])
        task = Tasks.objects.create(
            task_id=create_task_result["data"]["task_id"],
            bk_biz_id=bk_biz_id,
            template_id=template_id,
            task_name=task_name,
            created_by=user_name,
            params=params,
            task_url=create_task_result["data"]["task_url"],
        )
        return {
            "id": task.id,
            "task_name": task.task_name,
            "params": task.params,
            "bk_biz_id": task.bk_biz_id,
            "template_id": task.template_id,
        }

    def retrieve(self, id):
        task = Tasks.objects.filter(pk=id).first()
        if not task:
            raise ValidationError("task: {} not exist".format(id))
        return model_to_dict(task)

    def sync(self, request):
        tasks = Tasks.objects.filter(
            status__in=[TaskStatus.CREATED, TaskStatus.RUNNING, TaskStatus.SUSPENDED]
        )
        for task in tasks:
            sops_task_result = SopsHandler.call_sops_task_status(task.task_id)
            if not sops_task_result["data"]:
                continue
            task.status = sops_task_result["data"]["state"]
            task.save()
        return []

    @classmethod
    def update_task_status_result(cls, task_status_result: dict):
        query_set = Tasks.objects.filter(sops_task_id__in=task_status_result.keys())
        for obj in query_set:
            query_set.status = task_status_result.get(obj.sops_task_id)
        Tasks.objects.bulk_update(query_set, fields=["status"])

    @classmethod
    def _get_task_status(cls, sops_tasks_ids):
        result = {}
        for sops_task_id in sops_tasks_ids:
            sops_task_result = SopsHandler.call_sops_task_status(sops_task_id)
            if not sops_task_result["data"]:
                continue
            result.update({sops_task_id: sops_task_result["data"]["state"]})
        return result


class BizHandler(object):
    def list(self, request):
        result = CCHandler.call_search_business()
        return [
            {"bk_biz_id": info["bk_biz_id"], "bk_biz_name": info["bk_biz_name"]}
            for info in result["data"]["info"]
        ]


class TemplateHandler(object):
    def list(self, request, bk_biz_id):
        if not bk_biz_id:
            raise ValidationError("need to supply bk_biz_id in param")
        result = SopsHandler.call_get_template_list(bk_biz_id=bk_biz_id)["data"]
        return [
            {"template_id": obj["id"], "template_name": obj["name"]} for obj in result
        ]

    def params(self, request, template_id):
        result = SopsHandler.call_get_template_info(template_id=template_id)["data"]
        return result["pipeline_tree"]["constants"]


class PermissionHandler(object):
    def list(self, request, action_id):
        if not action_id:
            raise ValidationError("need to supply action_id in param")
        # todo mock 权限中心调用
        return {}


class SopsHandler(object):
    # todo 待mock接口
    @staticmethod
    def call_sops_task_status(sops_task_id):
        return SOPS_TASK_STATUS_RESULT

    @staticmethod
    def call_get_template_list(bk_biz_id):
        return DEFAULT_TEMPLATE_LIST

    @staticmethod
    def call_get_template_info(template_id):
        return GET_TEMPLATE_INFO_RESULT

    @staticmethod
    def call_create_task(task_name, params: dict = None):
        return CREATE_TASK_RESULT

    @staticmethod
    def call_start_task(task_id):
        return START_TASK_RESULT


class CCHandler(object):
    @staticmethod
    def call_search_business():
        return DEFAULT_CC_BIZ_RESULT
