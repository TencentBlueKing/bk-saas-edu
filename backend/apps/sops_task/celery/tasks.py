from apps.sops_task.handlers import TaskHandler


def update_sops_task_status():
    TaskHandler().sync()
