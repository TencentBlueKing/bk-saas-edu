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

from apps.sops_task.models import Tasks

from iam import IAM, Request, Subject, Action, Resource
from iam.apply.models import ActionWithoutResources, ActionWithResources, Application, RelatedResourceType, ResourceInstance, ResourceNode
from common.constants import ActionEnum, ResourceTypeEnum

import sys
import logging
iam_logger = logging.getLogger("iam")
iam_logger.setLevel(logging.DEBUG)

debug_hanler = logging.StreamHandler(sys.stdout)
debug_hanler.setFormatter(logging.Formatter('%(levelname)s [%(asctime)s] [IAM] %(message)s'))
iam_logger.addHandler(debug_hanler)


class Permission(object):
    def __init__(self):
        self._iam = IAM(settings.APP_CODE, settings.SECRET_KEY, bk_apigateway_url=settings.BK_IAM_APIGATEWAY_URL)

    def _make_request_without_resources(self, username, action_id):
        request = Request(
            settings.BK_IAM_SYSTEM_ID,
            Subject("user", username),
            Action(action_id),
            None,
            None,
        )
        return request

    def _make_request_with_resources(self, username, action_id, resources):
        request = Request(
            settings.BK_IAM_SYSTEM_ID,
            Subject("user", username),
            Action(action_id),
            resources,
            None,
        )
        return request

    def allowed_task_create(self, username):
        request = self._make_request_without_resources(username, ActionEnum.TASK_CREATE.value)
        return self._iam.is_allowed(request)

    def allowed_task_view(self, username, task_id):
        r = Resource(settings.BK_IAM_SYSTEM_ID, ResourceTypeEnum.TASK.value, task_id, {})
        resources = [r]
        request = self._make_request_with_resources(username, ActionEnum.TASK_VIEW.value, resources)
        return self._iam.is_allowed(request)

    def batch_allowed_task_view(self, username, task_ids):
        resources_list = []
        for task_id in task_ids:
            r = Resource(settings.BK_IAM_SYSTEM_ID, ResourceTypeEnum.TASK.value, task_id, {})
            resources = [r]
            resources_list.append(resources)

        # 注意这里resources字段空
        request = Request(
            settings.BK_IAM_SYSTEM_ID,
            Subject("user", username),
            Action(ActionEnum.TASK_VIEW.value),
            [],
            None
        )

        # call batch_is_allowed
        return self._iam.batch_is_allowed(request, resources_list)

    def make_action_application(self, action_id):
        action = ActionWithoutResources(action_id)
        actions = [action]
        application = Application(settings.BK_IAM_SYSTEM_ID, actions)
        return application

    def make_task_application(self, task_id):
        task_name = f"task:{task_id}"
        try:
            task_name = Tasks.objects.get(id=task_id).task_name
        except Exception:
            pass

        instance = ResourceInstance([ResourceNode(ResourceTypeEnum.TASK.value, task_id, task_name)])
        related_resource_type = RelatedResourceType(settings.BK_IAM_SYSTEM_ID, ResourceTypeEnum.TASK.value, [instance])

        action = ActionWithResources(ActionEnum.TASK_VIEW.value, [related_resource_type])

        actions = [action]

        application = Application(settings.BK_IAM_SYSTEM_ID, actions)
        return application

    def generate_apply_url(self, application, bk_username=""):
        """
        处理无权限 - 跳转申请列表
        """
        ok, message, url = self._iam.get_apply_url(application, bk_username=bk_username)
        iam_logger.info("generate apply url for %s, got %s, %s, %s", application, ok, message, url)
        print("generate apply url for %s, got %s, %s, %s" % (application, ok, message, url))
        if not ok:
            return settings.BK_IAM_DEFAULT_APPLY_URL
        return url