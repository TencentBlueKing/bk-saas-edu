# 接口文档

**重要说明：请认真阅读以下规范，功能实现且符合规范的接口将酌情加分**

## 接口规范

### 1. 接口请求规范

- GET 请求，请使用 **查询字符串** 进行传参，如 `http://test.bk.com/sets/?bk_biz_id=2`

- POST 请求，请使用 **JSON** 格式进行传参，以下是使用 jquery 发起 post ajax 请求的例子

  ```js
  $.ajax({
      type: "post",
      url: site_url + 'release/',
      data: JSON.stringify({
          bk_biz_id: 2
      }),
      contentType: "application/json",
      dataType: "json",
      success: function(result) {}
  })
  ```

- 必须严格按照接口文档规定的请求方法 (GET/POST) 进行接口请求

### 2. 接口返回规范

- 必须使用 **JSON** 格式返回数据
- 接口返回状态码必须为 **200**
- 返回格式，包括数据类型、数据结构等，必须与接口文档保持一致

## [API-01] 获取业务列表

- 请求方法及URL

```
GET api/v1/bizs/
```

- 请求参数示例

  无

- 返回结果示例

```json
{
    "result": true,
    "code": 0,
    "data": [
        {
            "bk_biz_id": 12,
            "bk_biz_name": "蓝鲸"
        }
        ...
    ],
    "message": "OK"
}
```

- 返回结果参数说明

| 字段    | 类型   | 描述                              |
| ------- | ------ | --------------------------------- |
| result  | bool   | 返回结果，true为成功，false为失败 |
| code    | int    | 返回码，0表示成功，其他值表示失败 |
| message | string | 错误信息                          |
| data    | list   | 结果                              |

data

| 字段        | 类型   | 描述     |
| ----------- | ------ | -------- |
| bk_biz_id   | int    | 业务ID   |
| bk_biz_name | string | 业务名称 |

## [API-02] 获取标准运维模板列表

- 请求方法及URL

```
GET api/v1/templates/
```

- 请求参数示例

```json
?bk_biz_id=2
```

- 请求参数说明

| 字段      | 类型 | 必选 | 描述   |
| :-------- | ---- | ---- | ------ |
| bk_biz_id | int  | 是   | 业务id |


- 返回结果示例

```json
{
    "result": true,
    "code": 0,
    "data": [
        {
           "template_id": 1,
           "template_name": "考试认证-部署模板"
        }
        ...
    ],
    "message": "OK"
}
```

- 返回结果参数说明

| 字段    | 类型   | 描述                              |
| ------- | ------ | --------------------------------- |
| result  | bool   | 返回结果，true为成功，false为失败 |
| code    | int    | 返回码，0表示成功，其他值表示失败 |
| message | string | 错误信息                          |
| data    | list   | 结果                              |

data

| 字段        | 类型   | 描述     |
| ----------- | ------ | -------- |
| bk_biz_id   | int    | 业务ID   |
| bk_biz_name | string | 业务名称 |

## [API-03] 获取任务执行历史列表(支持分页)

- 请求方法及URL

```
GET api/v1/tasks/
```

- 请求参数示例

```json
?size=10&page=1
```

- 请求参数说明

| 字段 | 类型 | 必选 | 描述         |
| :--- | ---- | ---- | ------------ |
| size | int  | 非   | 每一页的数目 |
| page | int  | 非   | 当前页码     |


- 返回结果示例

```json
{
    "result": true,
    "data": {
        "count": 8,
        "info": [
            {
                "id": 1,
                "task_name": "test_no1",
                "task_id": 44,
                "task_url": "xxxxx/o/bk_sops/taskflow/execute/1/?instance_id=44",
                "bk_biz_id": 2,
                "template_id": 20,
                "created_by": "admin",
                "created_at": "2021-03-09 11:22:07",
                "status": "FINISHED",
                "permission":{"view_task": true}
            },
          	...
        ]
    },
    "code": 0,
    "message": "ok",
    "errors": null
}
```

- 返回结果参数说明

| 字段    | 类型   | 描述                              |
| ------- | ------ | --------------------------------- |
| result  | bool   | 返回结果，true为成功，false为失败 |
| code    | int    | 返回码，0表示成功，其他值表示失败 |
| message | string | 错误信息                          |
| data    | list   | 结果                              |

data

| 字段  | 类型  | 描述         |
| ----- | ----- | ------------ |
| count | int   | 总记录数     |
| info  | array | 执行记录数据 |

## [API-04] 获取当前模板所需参数

- 请求方法及URL

```
GET api/v1/templates/20/params/
```

- 返回结果示例

```json
{
    "result": true,
    "data": [{
      "${app_code}": {
            "custom_type": "input",
            "desc": "",
            "form_schema": {
                "attrs": {
                    "hookable": true,
                    "name": "输入框",
                    "validation": []
                },
                "type": "input"
            },
            "index": 1,
            "key": "${app_code}",
            "name": "应用code",
            "show_type": "show",
            "source_info": {},
            "source_tag": "input.input",
            "source_type": "custom",
            "validation": "^.+$",
            "value": "",
            "version": "legacy"
        },
      "${deploy_time}": {
        "custom_type": "int",
        "desc": "部署定时时间",
        "form_schema": {
          "attrs": {
            "hookable": true,
            "name": "整数",
            "validation": [
              {
                "type": "required"
              }
            ]
          },
          "type": "int"
        },
        "index": 0,
        "is_meta": false,
        "key": "${deploy_time}",
        "name": "部署定时时间",
        "show_type": "show",
        "source_info": {},
        "source_tag": "int.int",
        "source_type": "custom",
        "validation": "",
        "value": 0,
        "version": "legacy"
      }
    ],
    "code": 0,
    "message": "ok",
    "errors": null
}
```

- 返回结果参数说明

| 字段    | 类型   | 描述                              |
| ------- | ------ | --------------------------------- |
| result  | bool   | 返回结果，true为成功，false为失败 |
| code    | int    | 返回码，0表示成功，其他值表示失败 |
| message | string | 错误信息                          |
| data    | list   | 结果                              |

## [API-05] 新建任务

> 注，每套模板的新建任务时，除了   task_name, bk_biz_id, template_id 这三个参数之外可能不同。

- 请求方法及URL

```
POST api/v1/tasks/
```

- 请求参数示例

```json
{
    "task_name": "test",
    "bk_biz_id": 2,
    "template_id": 20,
  	"params":{
      "app_code": "test_app",
      "deploy_time": 5
    }
}
```

- 请求参数说明

| 字段        | 类型   | 必选 | 描述                   |
| :---------- | ------ | ---- | ---------------------- |
| task_name   | string | 是   | 任务名称               |
| bk_biz_id   | int    | 是   | 业务id                 |
| template_id | int    | 是   | 模版id                 |
| params      | dict   | 是   | 当前模版所需的参数字典 |


- 返回结果示例

```json
 {
    "result": true,
    "data": {
        "task_name": "test",
      	"params":{
          "app_code": "test_app",
          "deploy_time": 5
    		},
         "bk_biz_id": 2,
    		 "template_id": 20,
    },
    "code": 0,
    "message": "创建成功",
    "errors": null
}
```

- 返回结果参数说明

| 字段    | 类型   | 描述                              |
| ------- | ------ | --------------------------------- |
| result  | bool   | 返回结果，true为成功，false为失败 |
| code    | int    | 返回码，0表示成功，其他值表示失败 |
| message | string | 错误信息                          |
| data    | dict   | 结果                              |

data

| 字段        | 类型   | 必选 | 描述                   |
| :---------- | ------ | ---- | ---------------------- |
| task_name   | string | 是   | 任务名称               |
| bk_biz_id   | int    | 是   | 业务id                 |
| template_id | int    | 是   | 模版id                 |
| params      | dict   | 是   | 当前模版所需的参数字典 |

## [API-06] 手动刷新任务状态

- 请求方法及URL

```
GET api/v1/tasks/sync/
```

- 请求参数示例

  无

- 返回结果示例

```json
{
    "result": true,
    "code": 0,
    "data": [],
    "message": "OK"
}
```

- 返回结果参数说明

| 字段    | 类型   | 描述                              |
| ------- | ------ | --------------------------------- |
| result  | bool   | 返回结果，true为成功，false为失败 |
| code    | int    | 返回码，0表示成功，其他值表示失败 |
| message | string | 错误信息                          |
| data    | list   | 结果                              |

## [API-07] 查询是否有某个操作的权限

- 请求方法及URL

```
GET api/v1/permissions/
```

- 请求参数示例

```json
?action_id=create_ticket
```

- 返回结果示例

有权限:

```json
{
    "result": true,
    "code": 0,
    "data": {},
    "message": "OK"
} 
```

无权限:

```json
{
    "result": false,
    "code": 9900403,
    "data": {
      "url":"xxxxxxx"
    },
    "message": "NO PERMISSIONS"
} 
```

- 返回结果参数说明

| 字段    | 类型   | 描述                              |
| ------- | ------ | --------------------------------- |
| result  | bool   | 返回结果，true为成功，false为失败 |
| code    | int    | 返回码，0表示成功，其他值表示失败 |
| message | string | 错误信息                          |
| data    | dict   | 结果                              |

data

| 字段 | 类型   | 必选 | 描述          |
| :--- | ------ | ---- | ------------- |
| url  | string | 是   | 无权限申请url |

## 


## [API-08] 查询task详情

- 请求方法及URL
```
GET api/v1/tasks/1/
```

- 请求参数示例

无

- 返回结果示例
```json
{
    "result": true,
    "data": {
        "id": 3,
        "task_id": 10,
        "bk_biz_id": 2,
        "template_id": 1,
        "task_name": "测试任务",
        "status": "FAILED",
        "created_by": "admin",
        "params": {},
        "task_url": "http://bk_sops_host/taskflow/execute/3/?instance_id=15364"
    },
    "code": 0,
    "messages": "OK"
}
```

- 返回结果参数说明

| 字段    | 类型   | 描述                              |
| ------- | ------ | --------------------------------- |
| result  | bool   | 返回结果，true为成功，false为失败 |
| code    | int    | 返回码，0表示成功，其他值表示失败 |
| message | string | 错误信息                          |
| data    | dict   | 结果                              |

