
本文档用于将蓝鲸 Python 开发框架构建为镜像。


### 构建镜像

1. 将目录下的 `Dockerfile` `start_web.sh` 文件放到 Python 开发框架的根目录（跟 requirements.txt 文件同级的目录下）

2. 构建镜像
```
docker build . -f Dockerfile -t bkframe:v1.0
```

3. 上传镜像
```
docker tag [ImageId]  ccr.ccs.tencentyun.com/ /[namespace]/[ImageName]:[镜像版本号
docker push ccr.ccs.tencentyun.com/[namespace]/[ImageName]:[镜像版本号]
```

### 参考

1. 腾讯云免费镜像仓库： https://console.cloud.tencent.com/tke2/registry/

2. 使用 Arm 架构的机器如何构建 x86 平台镜像

Docker 支持通过 buildx 工具来构建跨平台的镜像，详情请查阅 [官方文档]([https://docs.docker.com/desktop/multi-arch/#multi-arch-support-on-docker-desktop)。

```
docker buildx create --use
docker buildx inspect --bootstrap
# 在这里我们必须在构建阶段同时做推送动作，因为多平台构建仅会保存在构建缓存中
docker buildx build --platform linux/amd64,linux/arm64 -t ${你的镜像 tag} --push .
```
