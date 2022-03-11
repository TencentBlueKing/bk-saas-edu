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
from config import RUN_VER
from config.default import FRONTEND_BACKEND_SEPARATION

if RUN_VER == "open":
    from blueapps.patch.settings_open_saas import *  # noqa
else:
    from blueapps.patch.settings_paas_services import *  # noqa

# 预发布环境
RUN_MODE = "STAGING"

# 只对预发布环境日志级别进行配置，可以在这里修改
# from blueapps.conf.log import set_log_level # noqa
# LOG_LEVEL = "ERROR"
# LOGGING = set_log_level(locals())

# 预发布环境数据库可以在这里配置

# 前后端开发模式下支持跨域配置
if FRONTEND_BACKEND_SEPARATION:
    INSTALLED_APPS += ("corsheaders",)
    # 该跨域中间件需要放在前面
    MIDDLEWARE = ("corsheaders.middleware.CorsMiddleware",) + MIDDLEWARE
    CORS_ORIGIN_ALLOW_ALL = True
    CORS_ALLOW_CREDENTIALS = True

# DATABASES.update(
#     {
#         'default': {
#             'ENGINE': 'django.db.backends.mysql',
#             'NAME': '',  # 数据库名
#             'USER': '',  # 数据库用户
#             'PASSWORD': '',  # 数据库密码
#             'HOST': '',  # 数据库主机
#             'PORT': '3306',  # 数据库端口
#         },
#     }
# )

