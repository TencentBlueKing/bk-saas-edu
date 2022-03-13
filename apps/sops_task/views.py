from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import action

# Create your views here.
from apps.drf import insert_permission_field, check_allowed
from apps.model_viewset import CustomModelViewSet
from apps.sops_task.handlers import TaskHandler

from apps.sops_task.models import Tasks
from apps.sops_task.serializers import TaskSerializer


class TaskViewSet(CustomModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer

    @insert_permission_field()
    def list(self, request, *args, **kwargs):
        return TaskHandler().list(request=request, view=self)

    @check_allowed()
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        params = dict(serializer.data)
        return Response(TaskHandler().create(request=request, **params))

    @action(methods=["get"], detail=False)
    def bizs(self, request, *args, **kwargs):
        return Response(TaskHandler().bizs(request=request))

    @action(methods=["get"], detail=False)
    def sops_templates(self, request, *args, **kwargs):
        bk_biz_id = request.GET.get("bk_biz_id")
        return Response(TaskHandler().sops_templates(bk_biz_id=bk_biz_id))
