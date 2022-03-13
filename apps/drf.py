# -*- coding: utf-8 -*-
import logging
from functools import wraps

from django.conf import settings
from django.http import JsonResponse, Http404
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import exceptions
from django.utils.translation import ugettext as _

logger = logging.getLogger("root")


class DataPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_query_param = "page"
    page_size_query_param = "pagesize"
    max_page_size = 1000

    def get_paginated_response(self, data):
        return Response({"total": self.page.paginator.count, "list": data})


def custom_exception_handler(exc, context):
    """
    自定义错误处理方式
    """
    # 专门处理 404 异常，直接返回前端，前端处理
    if isinstance(exc, Http404):
        return JsonResponse(_error("404", str(exc)))

    # 特殊处理 rest_framework ValidationError
    if isinstance(exc, exceptions.ValidationError):
        message = str(exc)
        return JsonResponse(_error("{}".format(exc.status_code), message))

    # 处理 rest_framework 的异常
    if isinstance(exc, exceptions.APIException):
        return JsonResponse(_error("{}".format(exc.status_code), exc.detail))

    # 处理 Data APP 自定义异常
    if isinstance(exc, BaseException):
        _msg = _("【APP 自定义异常】{message}, code={code}, args={args}").format(
            message=exc.message,
            code=exc.code,
            args=exc.args,
            data=exc.data,
            errors=exc.errors,
        )
        logger.exception(_msg)
        return JsonResponse(_error(exc.code, exc.message, exc.data, exc.errors))

    # 判断是否在debug模式中,
    # 在这里判断是防止阻止了用户原本主动抛出的异常
    if settings.DEBUG:
        return None

    # 非预期异常
    logger.exception(getattr(exc, "message", exc))
    return JsonResponse(_error("500", _("系统错误，请联系管理员")))


def _error(code=None, message="", data=None, errors=None):
    message = f"{message}（{code}）"
    if errors:
        message += f"（detail => {errors}）"
    return {
        "result": False,
        "code": code,
        "data": data,
        "message": message,
        "errors": errors,
    }


def insert_permission_field():
    # todo 返回所需权限字段
    """
    数据返回后，插入权限相关字段
    """

    def wrapper(view_func):
        @wraps(view_func)
        def wrapped_view(*args, **kwargs):
            response = view_func(*args, **kwargs)
            return response

        return wrapped_view

    return wrapper


def check_allowed():
    # todo 确定是否具有权限
    def wrapper(view_func):
        @wraps(view_func)
        def wrapped_view(*args, **kwargs):
            response = view_func(*args, **kwargs)
            return response

        return wrapped_view

    return wrapper
