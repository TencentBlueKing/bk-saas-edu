# -*- coding: utf-8 -*-
from django.utils.deprecation import MiddlewareMixin
from corsheaders.middleware import (
    ACCESS_CONTROL_ALLOW_ORIGIN,
    ACCESS_CONTROL_ALLOW_CREDENTIALS,
)


class CustomMiddleWare(MiddlewareMixin):
    """
    为了让前端在本地好调试
    """

    def process_response(self, request, response):
        response[ACCESS_CONTROL_ALLOW_ORIGIN] = "*"
        response[ACCESS_CONTROL_ALLOW_CREDENTIALS] = "true"
        return response
