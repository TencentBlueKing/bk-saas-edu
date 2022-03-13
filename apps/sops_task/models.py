from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.sops_task.constants import DEFAULT_CREATED_BY, TaskStatus


class Tasks(models.Model):
    task_id = models.IntegerField(_("标准运维任务ID"), db_index=True)
    bk_biz_id = models.IntegerField(_("业务id"), db_index=True)
    template_id = models.IntegerField(_("标准运维模板id"), db_index=True)
    task_name = models.CharField(_("任务名"), max_length=50)
    status = models.CharField(_("任务状态"), max_length=20, default=TaskStatus.CREATED)
    created_by = models.CharField(_("创建者"), max_length=32, default=DEFAULT_CREATED_BY)
    created_at = models.DateTimeField(_("创建时间"), auto_now_add=True, db_index=True)
    params = models.JSONField(_("标准运维全局参数"), null=True, blank=True)
    task_url = models.CharField(_("task链接地址"), max_length=128, null=True, blank=True)

    class Meta:
        verbose_name = "标准运维任务列表"
        verbose_name_plural = verbose_name
