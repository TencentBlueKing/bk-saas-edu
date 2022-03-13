# -*- coding: utf-8 -*-

# 默认创建者
DEFAULT_CREATED_BY = "admin"
# 默认任务状态
DEFAULT_TASK_STATUS = "created"

# todo mock掉标准运维接口调用
SOPS_TASK_STATUS_RESULT = {
    "result": True,
    "data": {
        "retry": 0,
        "name": "<class 'pipeline.core.pipeline.Pipeline'>",
        "finish_time": "",
        "skip": False,
        "start_time": "2018-04-26 16:08:34 +0800",
        "children": {
            "62d4784e20483f1585149ce90ed954c9": {
                "retry": 0,
                "name": "<class 'pipeline.core.flow.event.EmptyStartEvent'>",
                "finish_time": "2018-04-26 16:08:34 +0800",
                "skip": False,
                "start_time": "2018-04-26 16:08:34 +0800",
                "children": {},
                "state": "FINISHED",
                "version": "7447cc2801b630f497768493c02fb488",
                "id": "62d4784e20483f1585149ce90ed954c9",
                "loop": 1,
            },
            "e8b128dff46637368b9b1bd921abc14e": {
                "retry": 0,
                "name": "<class 'pipeline.core.flow.activity.ServiceActivity'>",
                "finish_time": "2018-04-26 16:08:46 +0800",
                "skip": False,
                "start_time": "2018-04-26 16:08:34 +0800",
                "children": {},
                "state": "FAILED",
                "version": "914d35fe7d143c2186e6d3532870b37d",
                "id": "e8b128dff46637368b9b1bd921abc14e",
                "loop": 1,
            },
        },
        "state": "FAILED",
        "version": "",
        "id": "5a1622f9f43e3429acb604e18dbd100a",
        "loop": 1,
    },
}

DEFAULT_CC_BIZ_START = 0
DEFAULT_CC_BIZ_LIMIT = 99999999
DEFAULT_CC_BIZ_SORT = ""

DEFAULT_TEMPLATE_LIST = {
    "result": True,
    "data": [
        {
            "category": "Other",
            "edit_time": "2018-04-23 17:30:48 +0800",
            "create_time": "2018-04-23 17:26:40 +0800",
            "name": "快速执行脚本",
            "bk_biz_id": "2",
            "creator": "admin",
            "bk_biz_name": "蓝鲸",
            "id": 32,
            "editor": "admin",
        },
        {
            "category": "Other",
            "edit_time": "2018-04-19 12:04:42 +0800",
            "create_time": "2018-04-19 12:04:42 +0800",
            "name": "new201804191218",
            "bk_biz_id": "2",
            "creator": "admin",
            "bk_biz_name": "蓝鲸",
            "id": 31,
            "editor": None,
        },
        {
            "category": "Other",
            "edit_time": "2018-04-18 17:09:39 +0800",
            "create_time": "2018-04-16 21:43:15 +0800",
            "name": "new20180416213944",
            "bk_biz_id": "2",
            "creator": "admin",
            "bk_biz_name": "蓝鲸",
            "id": 30,
            "editor": "admin",
        },
    ],
}

GET_TEMPLATE_INFO_RESULT = {
    "result": True,
    "data": {
        "category": "Other",
        "edit_time": "2018-04-27 16:24:24 +0800",
        "create_time": "2018-04-16 21:43:15 +0800",
        "name": "new20180416213944",
        "bk_biz_id": "2",
        "creator": "admin",
        "pipeline_tree": {
            "activities": {
                "631b6576cc5dfbdcaa4f510ce88a7e67": {
                    "outgoing": "44ab36ebf4cf119edaf2d20401da87e4",
                    "incoming": "fb2f3a8b533ca5c67e2440b4164f7632",
                    "name": "节点_1",
                    "error_ignorable": False,
                    "component": {
                        "code": "job_fast_execute_script",
                        "data": {
                            "account": {"hook": False, "value": "root"},
                            "ip_list": {"hook": False, "value": "127.0.0.1"},
                            "script_timeout": {
                                "hook": True,
                                "value": "${script_timeout}",
                            },
                            "content": {"hook": False, "value": "${content}"},
                            "script_param": {"hook": False, "value": "${params}"},
                            "script_type": {"hook": True, "value": "${script_type}"},
                        },
                    },
                    "optional": False,
                    "type": "ServiceActivity",
                    "id": "631b6576cc5dfbdcaa4f510ce88a7e67",
                    "loop": None,
                }
            },
            "end_event": {
                "type": "EmptyEndEvent",
                "outgoing": "",
                "incoming": "44ab36ebf4cf119edaf2d20401da87e4",
                "id": "60c81e383d048d8a3c574d3436e1b82c",
                "name": "",
            },
            "outputs": [],
            "flows": {
                "fb2f3a8b533ca5c67e2440b4164f7632": {
                    "is_default": False,
                    "source": "48afea1016ab70ee37179fa0eb1e1a14",
                    "id": "fb2f3a8b533ca5c67e2440b4164f7632",
                    "target": "631b6576cc5dfbdcaa4f510ce88a7e67",
                },
                "44ab36ebf4cf119edaf2d20401da87e4": {
                    "is_default": False,
                    "source": "631b6576cc5dfbdcaa4f510ce88a7e67",
                    "id": "44ab36ebf4cf119edaf2d20401da87e4",
                    "target": "60c81e383d048d8a3c574d3436e1b82c",
                },
            },
            "start_event": {
                "type": "EmptyStartEvent",
                "outgoing": "fb2f3a8b533ca5c67e2440b4164f7632",
                "incoming": "",
                "id": "48afea1016ab70ee37179fa0eb1e1a14",
                "name": "",
            },
            "constants": {
                "${script_type}": {
                    "source_tag": "job_fast_execute_script.script_type",
                    "source_info": {
                        "631b6576cc5dfbdcaa4f510ce88a7e67": ["script_type"]
                    },
                    "name": "脚本类型",
                    "index": 0,
                    "custom_type": "radio",
                    "value": "4",
                    "show_type": "show",
                    "source_type": "component_inputs",
                    "key": "${script_type}",
                    "validation": "^.*$",
                    "desc": "",
                },
                "${content}": {
                    "source_tag": "",
                    "source_info": {},
                    "name": "内容",
                    "index": 2,
                    "custom_type": "textarea",
                    "value": "",
                    "show_type": "show",
                    "source_type": "custom",
                    "key": "${content}",
                    "desc": "",
                },
                "${script_timeout}": {
                    "source_tag": "job_fast_execute_script.script_timeout",
                    "source_info": {
                        "631b6576cc5dfbdcaa4f510ce88a7e67": ["script_timeout"]
                    },
                    "name": "超时时间",
                    "index": 1,
                    "custom_type": "input",
                    "value": "",
                    "show_type": "show",
                    "source_type": "component_inputs",
                    "key": "${script_timeout}",
                    "validation": "^.*$",
                    "desc": "",
                },
                "${params}": {
                    "source_tag": "",
                    "source_info": {},
                    "name": "参数",
                    "index": 3,
                    "custom_type": "input",
                    "value": "",
                    "show_type": "show",
                    "source_type": "custom",
                    "key": "${params}",
                    "desc": "",
                },
            },
            "gateways": {},
        },
        "bk_biz_name": "蓝鲸",
        "id": 30,
        "editor": "admin",
    },
}

CREATE_TASK_RESULT = {
    "result": True,
    "data": {
        "task_id": 10,
        "task_url": "http://bk_sops_host/taskflow/execute/3/?instance_id=15364",
        "pipeline_tree": {
            "activities": {
                "node9b5ae13799d63e179f0ce3088b62": {
                    "outgoing": "line27bc7b4ccbcf37ddb9d1f6572a04",
                    "incoming": "line490caa49d2a03e64829693281032",
                    "name": "timing",
                    "error_ignorable": False,
                    "component": {
                        "code": "sleep_timer",
                        "data": {"bk_timing": {"hook": False, "value": "2"}},
                    },
                    "stage_name": "步骤1",
                    "can_retry": True,
                    "isSkipped": True,
                    "type": "ServiceActivity",
                    "optional": False,
                    "id": "node9b5ae13799d63e179f0ce3088b62",
                    "loop": None,
                },
                "node880ded556c6c3c269be3cedc64b6": {
                    "outgoing": "line490caa49d2a03e64829693281032",
                    "incoming": "lineb83161d6e0593ad68d9ec73a961b",
                    "name": "暂停",
                    "error_ignorable": False,
                    "component": {"code": "pause_node", "data": {}},
                    "stage_name": "步骤1",
                    "can_retry": True,
                    "isSkipped": True,
                    "type": "ServiceActivity",
                    "optional": True,
                    "id": "node880ded556c6c3c269be3cedc64b6",
                    "loop": None,
                },
            },
            "end_event": {
                "type": "EmptyEndEvent",
                "outgoing": "",
                "incoming": "line27bc7b4ccbcf37ddb9d1f6572a04",
                "id": "node5c48f37aa9f0351e8b43ab6a2295",
                "name": "",
            },
            "outputs": [],
            "flows": {
                "line490caa49d2a03e64829693281032": {
                    "is_default": False,
                    "source": "node880ded556c6c3c269be3cedc64b6",
                    "id": "line490caa49d2a03e64829693281032",
                    "target": "node9b5ae13799d63e179f0ce3088b62",
                },
                "lineb83161d6e0593ad68d9ec73a961b": {
                    "is_default": False,
                    "source": "noded383bc1d7387391f889c6bab18b8",
                    "id": "lineb83161d6e0593ad68d9ec73a961b",
                    "target": "node880ded556c6c3c269be3cedc64b6",
                },
                "line27bc7b4ccbcf37ddb9d1f6572a04": {
                    "is_default": False,
                    "source": "node9b5ae13799d63e179f0ce3088b62",
                    "id": "line27bc7b4ccbcf37ddb9d1f6572a04",
                    "target": "node5c48f37aa9f0351e8b43ab6a2295",
                },
            },
            "gateways": {},
            "line": [
                {
                    "source": {
                        "id": "node9b5ae13799d63e179f0ce3088b62",
                        "arrow": "Right",
                    },
                    "target": {
                        "id": "node5c48f37aa9f0351e8b43ab6a2295",
                        "arrow": "Left",
                    },
                    "id": "line27bc7b4ccbcf37ddb9d1f6572a04",
                },
                {
                    "source": {
                        "id": "node880ded556c6c3c269be3cedc64b6",
                        "arrow": "Right",
                    },
                    "target": {
                        "id": "node9b5ae13799d63e179f0ce3088b62",
                        "arrow": "Left",
                    },
                    "id": "line490caa49d2a03e64829693281032",
                },
                {
                    "source": {
                        "id": "noded383bc1d7387391f889c6bab18b8",
                        "arrow": "Right",
                    },
                    "id": "lineb83161d6e0593ad68d9ec73a961b",
                    "target": {
                        "id": "node880ded556c6c3c269be3cedc64b6",
                        "arrow": "Left",
                    },
                },
            ],
            "start_event": {
                "type": "EmptyStartEvent",
                "outgoing": "lineb83161d6e0593ad68d9ec73a961b",
                "incoming": "",
                "id": "noded383bc1d7387391f889c6bab18b8",
                "name": "",
            },
            "id": "node7ef6970d06ad3bc092594cb5ec5f",
            "constants": {},
            "location": [
                {
                    "stage_name": "步骤1",
                    "name": "暂停",
                    "y": 135,
                    "x": 300,
                    "type": "tasknode",
                    "id": "node880ded556c6c3c269be3cedc64b6",
                },
                {
                    "y": 150,
                    "x": 1000,
                    "type": "endpoint",
                    "id": "node5c48f37aa9f0351e8b43ab6a2295",
                },
                {
                    "stage_name": "步骤1",
                    "name": "timing",
                    "y": 135,
                    "x": 595,
                    "type": "tasknode",
                    "id": "node9b5ae13799d63e179f0ce3088b62",
                },
                {
                    "y": 150,
                    "x": 80,
                    "type": "startpoint",
                    "id": "noded383bc1d7387391f889c6bab18b8",
                },
            ],
        },
    },
}

START_TASK_RESULT = {"result": True, "data": {}}
