from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _


class TaskSerializer(serializers.Serializer):
    bk_biz_id = serializers.IntegerField(label=_("业务id"))
    template_id = serializers.IntegerField(label=_("标准运维模板id"))
    task_name = serializers.CharField(label=_("任务名称"), max_length=10, min_length=3)
    params = serializers.DictField(label=_("模板参数"))
