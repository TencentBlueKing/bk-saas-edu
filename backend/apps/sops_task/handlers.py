# -*- coding: utf-8 -*-
import functools
import json
import logging

from bkapi.bk_sops.shortcuts import get_client_by_request as get_sops_client_by_request
from bkapi_component.open.shortcuts import (
    get_client_by_request as get_esb_client_by_request,
)
from django.forms.models import model_to_dict
from rest_framework.exceptions import ValidationError

from apps.drf import DataPageNumberPagination
from apps.sops_task.constants import TaskStatus
from apps.exceptions import ApiResultError
from apps.sops_task.models import Tasks

logger = logging.getLogger("root")


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
            request,
            bk_biz_id=bk_biz_id,
            template_id=template_id,
            task_name=task_name,
            params=params,
        )
        SopsHandler.call_start_task(
            request, bk_biz_id=bk_biz_id, task_id=create_task_result["data"]["task_id"]
        )
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
            sops_task_result = SopsHandler.call_sops_task_status(
                request, sops_task_id=task.task_id, bk_biz_id=task.bk_biz_id
            )
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


class BizHandler(object):
    def list(self, request):
        result = CCHandler.call_search_business(request)
        return [
            {"bk_biz_id": info["bk_biz_id"], "bk_biz_name": info["bk_biz_name"]}
            for info in result["data"]["info"]
        ]


class TemplateHandler(object):
    def list(self, request, bk_biz_id):
        if not bk_biz_id:
            raise ValidationError("need to supply bk_biz_id in param")
        result = SopsHandler.call_get_template_list(request, bk_biz_id=bk_biz_id)[
            "data"
        ]
        return [
            {"template_id": obj["id"], "template_name": obj["name"]} for obj in result
        ]

    def params(self, request, template_id, bk_biz_id):
        if not bk_biz_id:
            raise ValidationError("need to supply bk_biz_id in param")
        result = SopsHandler.call_get_template_info(
            request, bk_biz_id=bk_biz_id, template_id=template_id
        )["data"]
        return result["pipeline_tree"]["constants"]


def client_log(func):
    @functools.wraps(func)
    def wrapper(request, *args, **kwargs):
        logger.info("client request: args: {}, kwargs: {}".format(args, kwargs))
        result = func(request, *args, **kwargs)
        logger.info("client response: {}".format(json.dumps(result)))
        if not result.get("result"):
            raise ApiResultError(message=result.get("message"))
        return result

    return wrapper


class PermissionHandler(object):
    def __init__(self, action_id, resource_type, resource_id):
        self.action_id = action_id
        self.resource_type = resource_type
        self.resource_id = resource_id

    def has_permission(self, request):
        # todo mock 权限中心是否有权限逻辑
        return True

    def get_apply_url(self, request):
        # todo mock 权限中心获取apply_data及 url
        return ""


class SopsHandler(object):
    @staticmethod
    @client_log
    def call_sops_task_status(request, bk_biz_id, sops_task_id):
        client = get_sops_client_by_request(request)
        return client.api.get_task_status(
            path_params={
                "task_id": sops_task_id,
                "bk_biz_id": bk_biz_id,
            }
        )

    @staticmethod
    @client_log
    def call_get_template_list(request, bk_biz_id):
        client = get_sops_client_by_request(request)
        return client.api.get_template_list(
            path_params={
                "bk_biz_id": bk_biz_id,
            }
        )

    @staticmethod
    @client_log
    def call_get_template_info(request, bk_biz_id, template_id):
        client = get_sops_client_by_request(request)
        return client.api.get_template_info(
            path_params={
                "bk_biz_id": bk_biz_id,
                "template_id": template_id,
            }
        )

    @staticmethod
    @client_log
    def call_create_task(
        request, bk_biz_id, template_id, task_name, params: dict = None
    ):
        params = {
            "constants": {
                key if key.startswith("$") else f"${{{key}}}": value
                for key, value in (params or {}).items()
            },
            "name": task_name,
        }

        client = get_sops_client_by_request(request)
        return client.api.create_task(
            json=params,
            path_params={
                "bk_biz_id": bk_biz_id,
                "template_id": template_id,
            },
        )

    @staticmethod
    @client_log
    def call_start_task(request, bk_biz_id, task_id):
        client = get_sops_client_by_request(request)
        return client.api.start_task(
            json={},
            path_params={
                "bk_biz_id": bk_biz_id,
                "task_id": task_id,
            }
        )


class CCHandler(object):
    @staticmethod
    @client_log
    def call_search_business(request):
        # 创建 ESB SDK 客户端
        client = get_esb_client_by_request(request)
        # 调用 CC 系统的 search_business 组件
        return client.cc.search_business()
