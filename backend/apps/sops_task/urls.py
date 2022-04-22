# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from apps.sops_task.views import (
    TaskViewSet,
    BizViewSet,
    TemplateViewSet,
    PermissionViewSet,
)

router = routers.DefaultRouter()

router.register("tasks", TaskViewSet, basename="tasks")
router.register("bizs", BizViewSet, basename="bizs")
router.register("templates", TemplateViewSet, basename="templates")
# router.register("permissions", PermissionViewSet, basename="permissions")

urlpatterns = [
    url(r"^", include(router.urls)),
    url(r"^permissions/$", PermissionViewSet.as_view({"get": "has_permission"}), name="has_permission"),
    url(r"^permissions/get_apply_url/$", PermissionViewSet.as_view({"get": "get_apply_url"}), name="get_apply_url"),
]
