# notion配合vercel实时更新webhook

## 使用方法

1. 进入https://www.notion.so/profile -> Integrations 

2. 创建Integrations，type选择Internal

3. 进入该Integrations的详情页，配置webhook

4. 在你的服务器上创建一个docker容器，将vercel的webhook url作为环境变量传入

```shell
docker run -p 8000:8000 -e VERCEL_WEBHOOK_URL=<your vercel webhook url> alnda/notion-update-hook:0.0.1-amd64
```

5. 用notion的webhook功能，将验证通知发送到服务请求的`/update`路径

6. 查看容器日志，获取notion的verification_token

该信息具体在docker对应服务终端的`INFO - Your verify token:`附近

7. 将该信息填入notion表单中，在notion内验证成功后，当notion页面内发生更新时，即可自动更新vercel对应部署的项目