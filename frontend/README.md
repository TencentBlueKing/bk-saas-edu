# SaaS开发课程项目

## 前端启动方式

### 本地开发模式（需要先启动后端）
1. 本地配置 hosts （127.0.0.1       local.paas-edu.bktencent.com）
2. 执行 npm install
3. 执行 npm run dev
4. 浏览器打开 local.paas-edu.bktencent.com:8000

### 本地开发配置注意项
1. 配置 frontend/package.json：betterScripts.dev.env 中的 BKPAAS_APP_ID 和 BKPAAS_APP_SECRET。这个从 lesscode 生成源码的时候会自动生成
2. 如果前后端都是本地开发，需要手动配置 proxy。配置文件在 frontend/lib/client/build/webpack.dev.conf.js，配置项为 webpackConfig.proxy。如果不需要代理，可以注释掉这个配置
3. 接口请求url配置：配置文件在 frontend/lib/client/build/dev.env.js，配置项为 API_URL。dev模式下，如果需要调试本地后端请求，可以改成 'http://local.paas-edu.bktencent.com:5000/'，如果请求线上接口，可以使用 'http://apps.paas-edu.bktencent.com/stag--bk-saas-edu-v3/'

### 线上部署模式
执行 npm run online
