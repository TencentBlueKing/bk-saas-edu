# -*- coding: utf-8 -*-

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response


class ResponseMixin(object):
    def finalize_response(self, request, response, *args, **kwargs):
        if isinstance(response, Response):
            response.data = {
                "result": True,
                "data": response.data,
                "code": 0,
                "messages": "OK",
            }
        return super(ResponseMixin, self).finalize_response(
            request, response, *args, **kwargs
        )


# 注意书写顺序
class CustomModelViewSet(ResponseMixin, ModelViewSet):
    pass
