# clsq_spider
该爬虫程序会爬取当天的所有视频链接并存入MySQL数据库
## docker-compose 部署
```yml
version: '3'
services:
  clsq_spider:
    image: lovewen/clsq_spider:latest
    container_name: clsq_spider
    environment:
      TZ: Asia/Shanghai
      MYSQL_IP: 127.0.0.1
      MYSQL_DB_NAME: mydb
      MYSQL_PORT: 3306
      MYSQL_USER: root
      MYSQL_PASSWORD: 123456
    volumes:
      - ./logs:/usr/log
      - ./htm:/usr/htm
```
建议配合linux定时任务每天晚上23:58分执行一次
```shell
58 23 * * * cd /usr/clsq_spider && docker-compose up -d
```