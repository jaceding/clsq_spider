# clsq_spider
该爬虫程序会爬取某神秘网站当天的所有视频链接并存入数据库。
## 功能配置介绍
1. 数据存入数据库（必选）  
目前仅支持MySQL数据库，相关配置如下：

    配置名称 | 含义 |  默认值  
    -|-|-
    MYSQL_IP | ip地址 | 127.0.0.1 |
    MYSQL_DB_NAME | 名称 | mydb |
    MYSQL_PORT | 端口 | 3306 |
    MYSQL_USER | 用户名 | root |
    MYSQL_PASSWORD | 密码 | 无 |

2. 邮件通知（非必填）  
邮件是自己给自己发送，通知内容主要包含：爬取总数、成功数、开始时间、结束时间，目前仅支持QQ邮箱，相关配置如下：  
注意：邮件授权码非密码，如有疑惑请自行百度：QQ邮箱授权码

    配置名称 | 含义 |  默认值  
    -|-|-
    MAIL_ACCOUNT | 邮箱账号 | 无 |
    MAIL_PASSWORD | 邮箱授权码 | 无 |

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
      MAIL_ACCOUNT: 987654321@qq.com
      MAIL_PASSWORD: 123456
    volumes:
      - ./logs:/usr/log
      - ./htm:/usr/htm
```
建议配合Linux定时任务每天晚上23:58分执行一次
```shell
58 23 * * * cd /usr/clsq_spider && docker-compose up -d
```