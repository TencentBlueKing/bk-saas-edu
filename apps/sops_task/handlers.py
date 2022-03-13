# -*- coding: utf-8 -*-
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from blueking.component.shortcuts import get_client_by_request

from apps.drf import DataPageNumberPagination
from apps.sops_task.constants import (
    SOPS_TASK_STATUS_RESULT,
    DEFAULT_CC_BIZ_START,
    DEFAULT_CC_BIZ_LIMIT,
    DEFAULT_CC_BIZ_SORT,
    DEFAULT_TEMPLATE_LIST,
    GET_TEMPLATE_INFO_RESULT,
    CREATE_TASK_RESULT,
    START_TASK_RESULT,
)
from apps.sops_task.models import Tasks


class TaskHandler(object):
    def list(self, request, view):
        pg = DataPageNumberPagination()
        page_sops_tasks = pg.paginate_queryset(
            queryset=Tasks.objects.all().order_by("-created_at", "created_by"),
            request=request,
            view=view,
        )
        if not page_sops_tasks:
            return Response([])
        task_result_dict = self._get_task_status(
            [task.sops_task_id for task in page_sops_tasks]
        )
        res = pg.get_paginated_response(
            [
                self._generate_task_status(task, task_result_dict)
                for task in page_sops_tasks
            ]
        )
        self.update_task_status_result(task_result_dict)
        return res

    def create(
        self, request, bk_biz_id, template_id, name, timing_config=None, app_name=None
    ):
        user_name = request.user.username
        create_task_result = self.call_create_task(name=name)
        self.call_start_task(create_task_result["data"]["task_id"])
        task = Tasks.objects.create(
            sops_task_id=create_task_result["data"]["task_id"],
            bk_biz_id=bk_biz_id,
            template_id=template_id,
            name=name,
            created_by=user_name,
            timing_config=timing_config,
            app_name=app_name,
            task_url=create_task_result["data"]["task_url"],
        )
        return task.id

    def bizs(self, request):
        client = get_client_by_request(request)
        kwargs = {
            "fields": ["bk_biz_id", "bk_biz_name"],
            "page": {
                "start": DEFAULT_CC_BIZ_START,
                "limit": DEFAULT_CC_BIZ_LIMIT,
                "sort": DEFAULT_CC_BIZ_SORT,
            },
        }
        result = client.cc.search_business(kwargs)
        return result["data"]

    def sops_templates(self, bk_biz_id):
        if not bk_biz_id:
            raise ValidationError("need to supply bk_biz_id in param")
        return self.call_get_template_list(bk_biz_id=bk_biz_id)

    @classmethod
    def update_task_status_result(cls, task_status_result: dict):
        query_set = Tasks.objects.filter(sops_task_id__in=task_status_result.keys())
        for obj in query_set:
            query_set.status = task_status_result.get(obj.sops_task_id)
        Tasks.objects.bulk_update(query_set, fields=["status"])

    @classmethod
    def _generate_task_status(cls, task, task_result_dict):
        task_dict = model_to_dict(task)
        task_dict["status"] = task_result_dict.get(task.sops_task_id)
        return task_dict

    @classmethod
    def _get_task_status(cls, sops_tasks_ids):
        result = {}
        for sops_task_id in sops_tasks_ids:
            sops_task_result = cls.call_sops_task_status(sops_task_id)
            if not sops_task_result["data"]:
                continue
            result.update({sops_task_id: sops_task_result["data"]["state"]})
        return result

    @classmethod
    def call_sops_task_status(cls, sops_task_id):
        # todo mock修改掉get_task_status接口调用
        return SOPS_TASK_STATUS_RESULT

    @classmethod
    def call_get_template_list(cls, bk_biz_id):
        # todo mock掉获取标准运维模板列表接口调用
        return DEFAULT_TEMPLATE_LIST

    @classmethod
    def call_get_template_info(cls, template_id):
        # todo mock掉获取模板详情接口调用
        return GET_TEMPLATE_INFO_RESULT

    @classmethod
    def call_create_task(cls, name, constants: dict = None):
        # todo mock掉创建任务接口
        return CREATE_TASK_RESULT

    @classmethod
    def call_start_task(cls, task_id):
        # todo mock掉开始任务接口
        return START_TASK_RESULT
