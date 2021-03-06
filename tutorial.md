# 实战项目指南

# 开发环境配置(供参考)：

- ide：PyCharm 2020.2.3 (Professional Edition)

- Python：3.6.8

- Node：v14.17.6

- MySQL: 5.7

- git: 2.32.0.windows.2

# 开发准备

## 拉取项目

进入GitHub的实战项目界面，复制项目git地址

![](src/tutorial/2022-05-27-10-22-34-image.png)

打开命令行终端拉取项目下来，

```
git clone git@github.com:TencentBlueKing/bk-saas-edu.git
```

![](src/tutorial/2022-05-31-11-05-12-image.png)

执行完成后即可拉取项目到本地

![](src/tutorial/2022-05-27-10-22-45-image.png) 

## 使用 Pycharm 打开项目，配置项目目录

![](src/tutorial/2022-05-27-10-26-15-image.png)

进入项目设置

![](src/tutorial/2022-05-27-10-25-22-image.png)

配置项目结构

![](src/tutorial/2022-05-27-10-29-14-image.png)

![](src/tutorial/2022-05-27-10-29-55-image.png)

![](src/tutorial/2022-05-27-10-31-47-image.png)

![](src/tutorial/2022-05-27-10-33-10-image.png)
## 创建 Python 虚拟环境

继续打开项目设置，找到并点击Python Interpreter

![](src/tutorial/2022-05-27-10-35-22-image.png)

![](src/tutorial/2022-05-27-10-36-58-image.png)

![](src/tutorial/2022-05-27-10-38-02-image.png)

![](src/tutorial/2022-05-27-10-38-41-image.png)

![](src/tutorial/2022-05-27-10-44-02-image.png)

![](src/tutorial/2022-05-27-10-38-41-image.png)

点击OK即可基于 Python3.6 创建一个虚拟环境


## 下载依赖

点击Pycharm左下角的terminal，打开命令行终端
![](src/tutorial/2022-05-27-10-47-18-image.png)

![](src/tutorial/2022-05-27-10-54-15-image.png)

进入后端目录`cd backend`

![](src/tutorial/2022-05-27-10-55-03-image.png)

- 下载bkapi-bk-sops

打开开发者中心 https://bkpaas.paas-edu.bktencent.com/ ，点击进入API文档

![](src/tutorial/2022-05-27-11-08-07-image.png)

点击 bk-sops

![](src/tutorial/2022-05-27-11-08-51-image.png)

如下图所示点击下载压缩包

![](src/tutorial/2022-05-27-11-09-24-image.png)

在terminal中输入

```
pip install <包所在的路径>/bkapi-bk-sops-1.0.2.tar.gz
```

在terminal中输入`pip list | grep bkapi-bk-sops` 检查是否添加成功添加 bkapi-bk-sops 依赖

![](src/tutorial/2022-05-27-11-17-43-image.png)

在命令行输入`pip install -r requirements.txt`，按回车执行完成后即可

![](src/tutorial/2022-05-27-16-03-47-image.png)

注意：如果在本教程之前已经完成了依赖安装，请确保 `bkapi-client-core>=1.1.6` ，否则后续调用 ESB API 可能会失败

# 创建SaaS应用

## gitee--创建仓库

打开 https://gitee.com/ ，（需注册）登录后新建仓库

![](src/tutorial/2022-05-27-11-26-07-image.png)

![](src/tutorial/2022-05-30-17-41-47-image.png)

创建完毕后复制仓库的 git 地址

![](src/tutorial/2022-05-30-17-41-20-image.png)

## 链接gitee仓库

回到 Pycharm 的 terminal 终端，清空远程仓库地址并添加 gitee 仓库地址为远程仓库

```git
git remote remove origin
git remote add origin <项目仓库地址>
```

确定是否修改成功：`git remote -v`

![](src/tutorial/2022-05-27-11-41-20-image.png)

## 推送到gitee仓库

在命令行中输入 `git push origin master`

![](src/tutorial/2022-05-30-17-42-18-image.png)

刷新下gitee的项目界面，会发现已经成功把本地的仓库推送到gitee的仓库中了

![](src/tutorial/2022-05-27-11-46-28-image.png)

## 开发者中心-创建蓝鲸SaaS应用

进入开发者中心 https://bkpaas.paas-edu.bktencent.com/ ，点击创建应用

![](src/tutorial/2022-05-27-16-07-23-image.png)

输入应用信息与仓库信息

![](src/tutorial/2022-05-31-09-49-56-image.png)

![](src/tutorial/2022-05-31-09-51-34-image.png)

蓝鲸SaaS项目就创建成功啦！

![](src/tutorial/2022-05-27-16-12-35-image.png)

### 创建新模块--用于部署前端服务

进入项目页面，点击新增模块

![](src/tutorial/2022-05-30-15-43-42-image.png)

![](src/tutorial/2022-05-31-09-52-48-image.png)

![](src/tutorial/2022-05-31-09-54-07-image.png)

成功创建`frontend`模块

![](src/tutorial/2022-05-31-09-55-13-image.png)

### 设置前端模块为主模块

![](src/tutorial/2022-05-31-10-15-22-image.png)



# 本地启动

## 准备工作

### 获取蓝鲸SaaS应用ID和TOKEN

  打开开发者中心 https://bkpaas.paas-edu.bktencent.com/ ， 进入创建的蓝鲸应用
  
  ![](src/tutorial/2022-05-27-14-24-14-image.png)
  
  点击`基本设置`->`基本信息`
  
  ![](src/tutorial/2022-05-27-14-24-48-image.png)
  
  如图所示，`bk_app_code` 为应用ID，而`bk_app_secret`为应用鉴权TOKEN，这两个变量在之后的环境变量配置会用到。

### 创建数据库
  
  打开命令行终端，输入下列指令进入MySQL：
  
  ```
  mysql -u root -p
  ```
  
  ![](src/tutorial/2022-05-27-14-28-29-image.png)
  
  以应用ID为数据库名创建数据库，以上面的测试项目为例，应用ID为`saas-prac-guide`，则创建数据库语句为
  
  ```
  CREATE DATABASE `saas-prac-guide` default charset utf8 COLLATE utf8_general_ci;
  ```
  
  ![](src/tutorial/2022-05-27-14-32-08-image.png)
  
  创建数据库成功

### 配置数据库
  打开Pycharm，在`bk-saas-edu/backend/`中新建`local_settings.py`
  
  在该文件中输入数据库配置：
  
  ```
  DATABASES = {
      "default": {
          "ENGINE": "django.db.backends.mysql",
          "NAME": APP_CODE,  # noqa
          "USER": "root",
          "PASSWORD": "",
          "HOST": "localhost",
          "PORT": "3306",
      },
  }
  ```
  
  `USER`和`PASSWORD`中分别输入本地MySQL的用户名和密码，`NAME`中输入应用ID`bk_app_code`的内容
  
  ![](src/tutorial/2022-05-27-15-48-38-image.png)

### 修改iam迁移文件
  
  打开`backend/support-files/iam/0001_bk_saas_edu_20220321-1505.json`
  
  按`ctrl+r`搜索替换`bk-saas-edu-v3`和`bk-saas-edu`为自己的 appcode
  
  ![](src/tutorial/2022-05-27-16-15-33-image.png)
  
  修改项目信息介绍，修改成自己项目的信息即可，至少需要修改`name`, `name_en`, `clients`的内容
  
  ![](src/tutorial/2022-05-27-16-16-03-image.png)

### 数据库迁移
  ![](src/tutorial/2022-05-27-14-41-13-image.png)
  
  如图进入配置页面，点击添加Python
  
  ![](src/tutorial/2022-05-27-14-42-13-image.png)
  配置信息
  
  ![](src/tutorial/2022-05-31-11-10-48-image.png)
  
  所需的环境变量如下
  
  ```
  PYTHONUNBUFFERED=1
  BK_PAAS2_INNER_URL=http://paas-edu.bktencent.com:80
  BK_PAAS2_URL=https://paas-edu.bktencent.com/
  DJANGO_SETTINGS_MODULE=settings
  BKPAAS_MAJOR_VERSION=3
  NODE_ENV=development
  BK_COMPONENT_API_URL=https://bkapi.paas-edu.bktencent.com
  BK_LOGIN_URL=http://paas-edu.bktencent.com:80/login/
  PIP_EXTRA_INDEX_URL=http://bkrepo.paas-edu.bktencent.com/pypi/bkpaas/pypi/simple
  BK_API_URL_TMPL=http://bkapi.paas-edu.bktencent.com/api/{api_name}
  BKAPP_CORS_ENABLED=off
  BKAPP_CSRF_COOKIE_DOMAIN=paas-edu.bktencent.com
  BKPAAS_APP_ID=<bk_app_code的内容>
  BKPAAS_APP_SECRET=<bk_app_secret的内容>
  ```
  
  ![](src/tutorial/2022-06-02-13-33-58-image.png)
  

  点击运行
  
  ![](src/tutorial/2022-05-27-15-50-13-image.png)
  
  ![](src/tutorial/2022-05-27-15-50-28-image.png)
  
  

## 本地运行后端

### 修改本地host  

修改`C:/Windows/System32/drivers/etc/hosts`，添加

```
127.0.0.1 local.paas-edu.bktencent.com
```

### Django配置

![](src/tutorial/2022-05-27-16-26-51-image.png)

![](src/tutorial/2022-05-31-11-14-33-image.png)

配置环境变量内容与上面一样

### 本地运行Django
  
  ![](src/tutorial/2022-05-27-16-28-45-image.png)
  
  ![](src/tutorial/2022-05-30-11-04-02-image.png)
  
  
### 运行celery

- 配置并运行 celery worker
  
  ```
  python manage.py celery worker --pool=solo -l info
  ```

  ![](src/tutorial/2022-06-02-12-30-58-image.png)

  ![](src/tutorial/2022-06-02-13-31-58-image.png)
  

  
- 配置并运行 celery beat

  ```
  python manage.py celery beat -l info
  ```

  ![](src/tutorial/2022-06-02-12-31-58-image.png)

  ![](src/tutorial/2022-05-31-12-38-58-image.png)
  


若重新运行celery beat报错的话，请删除`backend/celerybeat.pid`后，重新运行celery beat


### 访问后端服务

  点击链接或访问`http://local.paas-edu.bktencent.com:5000/`可打开如下页面：
  
  ![](src/tutorial/2022-05-27-16-29-46-image.png)

## 本地运行前端
  ```
  cd frontend
  npm install
  ```
  
  若想重新安装，请将`frontend`目录下的`package-lock.json`, `node_modules/`, `lib/client/.webpack_cache/` 删除后，重新执行上述命令

### 配置环境变量
  修改 `frontend/package.json`，
  
  - 填写`BKPAAS_APP_ID` 和 `APP_CODE`，内容为创建的应用`bk_app_code`
  
  - 填写`BKPAAS_APP_SECRET`，内容为应用`bk_app_secret`
  
  ![](src/tutorial/2022-05-31-11-15-00-image.png)

### 本地启动前端服务
  
  ```
  npm run dev
  ```
  
  ![](src/tutorial/2022-05-30-14-35-09-image.png)
  
  点击链接或访问`http://local.paas-edu.bktencent.com:8000/`可打开如下页面：
  
  ![](src/tutorial/2022-05-30-14-37-19-image.png)
  
  若想调用本地接口需要在本地把后端服务也启动起来，启动后通过操作前端界面即可调用后端接口。
  
  **注意：新建部署功能需要蓝鲸权限中心授权，请联系蓝鲸平台管理员进行权限审批**
  
# 本地开发配置

## 加入用户组（必选）

![](src/tutorial/2022-06-02-11-30-58-image.png)

选择业务需要先获取业务权限，我们需要申请加入到权限中心 **课堂练习专用** 的用户组

### 申请权限

打开权限中心：`https://bkiam.paas-edu.bktencent.com/apply-join-user-group?limit=10&current=1`

![](src/tutorial/2022-06-02-11-28-58-image.png)


**申请后，请联系蓝鲸平台管理员进行权限审批**

申请成功后即可获取到业务列表：

![](src/tutorial/2022-06-02-11-29-58-image.png)

## 申请云 API 权限（必选）

打开开发者中心->`云 API 管理`->`云 API 权限`，选择`网关API`-`bk-sops`，批量申请申请下列API权限：
- get_template_list ---	查询业务下的模板列表
- get_template_info --- 查询业务下的单个模板详情
- create_task --- 通过业务流程模板创建任务
- start_task --- 开始执行任务
- get_task_status --- 查询任务执行状态

![](src/tutorial/2022-06-02-10-44-58-image.png)

![](src/tutorial/2022-06-02-10-45-58-image.png)

![](src/tutorial/2022-06-02-10-46-58-image.png)
  
  **申请后，请联系蓝鲸平台管理员进行权限审批**

## 跳过权限中心的权限校验(可选)

后端服务内置了权限中心校验包括获取项目流程模板、创建任务、启动任务、查看任务的权限，若需要跳过权限校验，则可配置环境变量`BK_IAM_SKIP`为`True`

修改`backend/local_settings.py`，增加`BK_IAM_SKIP=True`

![](src/tutorial/2022-06-02-13-32-58-image.png)


## 本地前后端联调（必选）

若需要调用本地的后端服务，则需要修改前端的配置：修改`frontend/lib/client/build/dev.env.js`中的`API_URL`，原设置为调用预发布环境的后端服务，本地联调需要改为本地的后端服务地址，如`//local.paas-edu.bktencent.com:5000/`

![](src/tutorial/2022-06-01-12-59-58-image.png)


# 部署SaaS

## 配置app_desc.yaml

修改根目录下的`app_desc.yaml`，修改`bk_app_code`配置

![](src/tutorial/2022-05-31-09-57-44-image.png)

## 仓库分支管理

- master分支---用于发布生产环境

- dev分支---开发分支，不做内容限制

- stag分支---用于发布预发布环境

## 创建stag和dev分支

- 打开git项目仓库，进入分支管理页面

![](src/tutorial/2022-05-30-15-27-30-image.png)

![](src/tutorial/2022-05-30-15-27-57-image.png)

新建分支，分别创建stag和dev分支

![](src/tutorial/2022-05-30-15-28-09-image.png)

## 推送配置修改到个人仓库的开发分支

把 `backend/support-files/iam/0001_bk_saas_edu_20220321-1505.json`和`app_desc.yaml`的修改推送到自己的git仓库里

- 创建并切换到dev分支

```
git checkout -b dev
```

- 保存修改

```
git add app_desc.yaml
cd backend
git add support-files/iam/0001_bk_saas_edu_20220321-1505.json
git commit -m "feat(deploy): 修改iam项目配置和app_desc配置"
```

![](src/tutorial/2022-05-31-10-03-19-image.png)

- 推送修改

```
git push origin dev
```

![](src/tutorial/2022-05-30-14-59-12-image.png)

## 部署前进行相关配置

### - 开启增强服务

进入开发者中心`增强服务`->`数据存储`，点击启用`RabbitMQ`

![](src/tutorial/2022-06-02-16-33-58-image.png)

### - 配置网关环境变量--后端服务

进入开发者中心项目概览，切换模块至`default`模块

![](src/tutorial/2022-05-31-10-17-50-image.png)

进入环境配置界面，增加环境变量 `BK_APIGW_NAME=bk-sops`， 生效范围选择 **所有环境**

![](src/tutorial/2022-06-02-14-33-58-image.png)

### - 配置权限校验豁免环境变量--后端服务

若**线上部署**需要跳过权限中心的权限校验，则进入开发者中心的环境配置界面，增加环境变量 `BK_IAM_SKIP=True`， 生效范围选择 **所有环境**

![](src/tutorial/2022-06-06-16-33-58-image.png)

### - 配置前端环境变量调用后端服务--前端服务

切换至frontend模块

![](src/tutorial/2022-05-31-10-18-21-image.png)

进入环境配置页面，增加环境变量 `API_URL=//apps.paas-edu.bktencent.com/stag--default--<你的app_code>/`， 生效范围选择 **预发布环境**

![](src/tutorial/2022-06-01-10-19-58-image.png)

增加环境变量 `API_URL=//apps.paas-edu.bktencent.com/prod--default--<你的app_code>/`， 生效范围选择 **生产环境**

![](src/tutorial/2022-06-02-15-33-58-image.png)


**请注意以上提到的开发者中心配置的环境变量，在配置后需要重新部署才能生效**

## 部署预发布环境

### - 合入代码到stag分支

新建Pull Request

  ![](src/tutorial/2022-05-30-15-30-38-image.png)

  ![](src/tutorial/2022-05-31-10-06-04-image.png)

合入代码

  ![](src/tutorial/2022-05-31-10-29-55-image.png)


  ![](src/tutorial/2022-05-31-10-10-03-image.png)



### - 部署预发布环境--后端服务

进入开发者中心项目概览，切换模块至`default`模块

![](src/tutorial/2022-05-31-10-17-50-image.png)

进入部署界面，点击部署

![](src/tutorial/2022-05-31-10-37-09-image.png)

![](src/tutorial/2022-05-31-10-19-10-image.png)



### - 部署预发布环境--前端服务

- 点击部署

![](src/tutorial/2022-05-31-10-25-52-image.png)

![](src/tutorial/2022-05-31-10-24-48-image.png)

## 部署生产环境

### - 提交Pull Request到master

![](src/tutorial/2022-05-30-21-01-10-image.png)

![](src/tutorial/2022-05-31-10-22-24-image.png)

### - 补充项目信息

进入开发者中心项目部署界面，点击“生产环境”

![](src/tutorial/2022-05-30-15-52-54-image.png)

- 填写缺少的信息

![](src/tutorial/2022-05-30-15-53-34-image.png)

### - 部署生产环境--后端服务

切换至`default`模块，点击生产环境，分支选择`master`，

![](src/tutorial/2022-05-31-10-18-06-image.png)

![](src/tutorial2022-05-31-10-24-28-image.png)

![](src/tutorial/2022-05-31-10-26-40-image.png)

### - 部署生产环境--前端服务

- 点击部署

![](src/tutorial/2022-05-31-10-30-10-image.png)

![](src/tutorial/2022-05-31-10-29-35-image.png)

### - 访问应用

![](src/tutorial/2022-05-31-10-34-00-image.png)

![](src/tutorial/2022-05-31-10-30-36-image.png)

