from rest_framework.response import Response
from rest_framework.decorators import action

# Create your views here.
from apps.drf import insert_permission_field, check_allowed
from apps.model_viewset import CustomModelViewSet
from apps.sops_task.handlers import (
    TaskHandler,
    BizHandler,
    TemplateHandler,
    PermissionHandler,
)

from apps.sops_task.models import Tasks
from apps.sops_task.serializers import TaskSerializer


class TaskViewSet(CustomModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer

    @insert_permission_field(
        id_field=lambda d: d["id"],
        data_field=lambda d: d["info"],
        actions=[],
        resource_meta=None,
    )
    def list(self, request, *args, **kwargs):
        return TaskHandler().list(request=request, view=self)

    @check_allowed()
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        params = dict(serializer.data)
        return Response(TaskHandler().create(request=request, **params))

    @check_allowed()
    def retrieve(self, request, pk=None, *args, **kwargs):
        return Response(TaskHandler().retrieve(id=pk))

    @action(methods=["GET"], detail=False)
    def sync(self, request, *args, **kwargs):
        return Response(TaskHandler().sync(request=request))


class BizViewSet(CustomModelViewSet):
    def list(self, request, *args, **kwargs):
        return Response(BizHandler().list(request=request))


class TemplateViewSet(CustomModelViewSet):
    def list(self, request, *args, **kwargs):
        bk_biz_id = request.GET.get("bk_biz_id")
        return Response(TemplateHandler().list(request=request, bk_biz_id=bk_biz_id))

    @action(methods=["GET"], detail=True)
    def params(
        self,
        request,
        pk,
        *args,
        **kwargs,
    ):
        return Response(TemplateHandler().params(request=request, template_id=pk))


class PermissionViewSet(CustomModelViewSet):
    def list(self, request, *args, **kwargs):
        action_id = request.GET.get("action_id")
        return Response(PermissionHandler().list(request=request, action_id=action_id))
