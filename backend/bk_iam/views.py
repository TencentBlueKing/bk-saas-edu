# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云PaaS平台社区版 (BlueKing PaaS Community
Edition) available.
Copyright (C) 2017-2021 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""
from django.conf import settings

from iam import IAM
from iam.contrib.django.dispatcher import DjangoBasicResourceApiDispatcher
from iam.resource.provider import ResourceProvider, ListResult

from apps.sops_task.models import Tasks

# reference: https://github.com/TencentBlueKing/iam-python-sdk/blob/master/docs/usage.md#3-resource-api-framework

class TaskResourceProvider(ResourceProvider):
    def list_instance(self, filter, page, **options):
        """配置权限时的下拉列表
        """
        queryset = Tasks.objects.all()
        count = queryset.count()
        results = [
            {"id": str(task.id), "display_name": task.task_name} for task in queryset[page.slice_from : page.slice_to]
        ]

        return ListResult(results=results, count=count)

    def search_instance(self, filter, page, **options):
        """配置权限时的搜索框
        """
        queryset = Tasks.objects.filter(task_name__contains=filter.keyword).all()
        count = queryset.count()
        results = [
            {"id": str(task.id), "display_name": task.task_name} for task in queryset[page.slice_from : page.slice_to]
        ]
        return ListResult(results=results, count=count)

    def fetch_instance_info(self, filter, **options):
        """申请权限时, 回调这个接口进行资源信息正确性/合法性校验
        """
        ids = []
        if filter.ids:
            ids = [int(i) for i in filter.ids]

        results = [{"id": str(task.id), "display_name": task.task_name} for task in Tasks.objects.filter(id__in=ids)]
        return ListResult(results=results)

    def list_attr(self, **options):
        """通过属性配置权限会用到, 没有属性权限管控不需要实现
        属性列表
        """
        return ListResult(results=[])

    def list_attr_value(self, filter, page, **options):
        """通过属性配置权限会用到, 没有属性权限管控不需要实现
        属性值列表
        """
        return ListResult(results=[])

    def list_instance_by_policy(self, filter, page, **options):
        """权限预览, 暂时没有用到, 可以不实现
        """
        return ListResult(results=[], count=0)


_iam = IAM(settings.APP_CODE, settings.SECRET_KEY, bk_apigateway_url=settings.BK_IAM_APIGATEWAY_URL)
dispatcher = DjangoBasicResourceApiDispatcher(_iam, settings.BK_IAM_SYSTEM_ID)
dispatcher.register("task", TaskResourceProvider())