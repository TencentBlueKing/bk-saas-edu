# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from apps.sops_task.views import TaskViewSet

router = routers.DefaultRouter()

router.register("tasks", TaskViewSet, basename="tasks")

urlpatterns = [url(r"^", include(router.urls))]
