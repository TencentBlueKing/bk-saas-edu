from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _


class TaskSerializer(serializers.Serializer):
    bk_biz_id = serializers.IntegerField(label=_("业务id"))
    template_id = serializers.IntegerField(label=_("标准运维模板id"))
    name = serializers.CharField(label=_("任务名称"), max_length=10, min_length=3)
    timing_config = serializers.CharField(
        label=_("定时配置"),
        max_length=20,
        allow_blank=True,
        allow_null=True,
        required=False,
    )
    app_name = serializers.CharField(
        label=_("应用名称"),
        max_length=50,
        allow_blank=True,
        allow_null=True,
        required=False,
    )

    def validate(self, attrs):
        ret = super(TaskSerializer, self).validate(attrs)
        return ret
