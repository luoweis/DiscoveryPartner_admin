# DiscoveryPartner_admin
Discovery Partner admin
项目名称： 发现技术工作人员
人以类聚、物以群分

## 数据库
```bash

docker run -d \
    --name discovery_admin_mysql \
    -e MYSQL_ROOT_PASSWORD=luoweis123456 \
    -e MYSQL_DATABASE=DiscoveryPartnerAdmin \
    --publish 13306:3306 \
    mysql:5.7 \
    --character-set-server=utf8mb4 \
    --collation-server=utf8mb4_unicode_ci
```