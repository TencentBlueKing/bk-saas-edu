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

from django.http import JsonResponse
from django.shortcuts import render


# 开发框架中通过中间件默认是需要登录态的，如有不需要登录的，可添加装饰器login_exempt
# 装饰器引入 from blueapps.account.decorators import login_exempt
def home(request):
    """
    首页
    """
    return render(request, "home_application/index_home.html")


def dev_guide(request):
    """
    开发指引
    """
    return render(request, "home_application/dev_guide.html")


def contact(request):
    """
    联系页
    """
    return render(request, "home_application/contact.html")


def anything(request):
    result = {
        "api_name": None,  # 网关名
        "app": None,  # 请求的应用
        "username": None,  # 用户名
        "headers": {k: v for k, v in request.headers.items() if k.lower().startswith("X-Bkapi-")},  # 网关请求头
    }

    if hasattr(request, "jwt"):
        result["api_name"] = request.jwt.api_name

    if hasattr(request, "app"):
        result["app"] = request.app.bk_app_code

    if hasattr(request, "user"):
        result["username"] = request.user.username

    return JsonResponse(result)
