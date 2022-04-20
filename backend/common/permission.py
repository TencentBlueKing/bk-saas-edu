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

from iam import IAM, Request, Subject, Action, Resource


SYSTEM_ID = settings.BK_IAM_SYSTEM_ID


class Permission(object):
    def __init__(self):
        self._iam = IAM(settings.APP_CODE, settings.SECRET_KEY, bk_apigateway_url=settings.BK_IAM_APIGATEWAY_URL)

    def _make_request_without_resources(self, username, action_id):
        request = Request(
            SYSTEM_ID,
            Subject("user", username),
            Action(action_id),
            None,
            None,
        )
        return request

    def _make_request_with_resources(self, username, action_id, resources):
        request = Request(
            SYSTEM_ID,
            Subject("user", username),
            Action(action_id),
            resources,
            None,
        )
        return request

    def allowed_task_create(self, username):
        request = self._make_request_without_resources(username, "task_create")
        return self._iam.is_allowed(request)

    def allowed_task_view(self, username, task_id):
        r = Resource(SYSTEM_ID, 'task', task_id, {})
        resources = [r]
        request = self._make_request_with_resources(username, "task_view", resources)
        return self._iam.is_allowed(request)