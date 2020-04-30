# -*- coding: utf-8 -*-
# @FileName: mysql_util.py
# @Description: 数据库工具类
# @Author : jaceding
# @Time : 2019/12/8
import os

import pymysql
from pymysql import ProgrammingError

from utils.log_util import logger


class MysqlDb(object):

    def __init__(self):
        mysql_ip = os.environ.get('MYSQL_IP')
        db_name = os.environ.get('MYSQL_DB_NAME')
        port = int(os.environ.get('MYSQL_PORT'))
        user = os.environ.get('MYSQL_USER')
        pass_word = os.environ.get('MYSQL_PASSWORD')

        if mysql_ip is None:
            mysql_ip = '127.0.0.1'
        if db_name is None:
            db_name = 'clsq_spider'
        if port is None:
            port = 3306
        if user is None:
            user = 'root'

        logger.info('mysql建立连接')
        logger.info("mysql_ip # " + mysql_ip)
        logger.info("db_name # " + db_name)
        logger.info("port # " + str(port))
        logger.info("user # " + user)
        logger.info("pass_word # " + pass_word)

        self.conn = pymysql.connect(mysql_ip, user, pass_word, db_name, port, autocommit=True)
        logger.info('mysql连接成功')
        self.cursor = self.conn.cursor()

    def save(self, item):
        """
        保存信息至数据库
        :param item: 实体信息
        :return: 是否保存成功 True or False
        """
        sql = "INSERT INTO clsq(descr, url_view, url) VALUES (%s, %s, %s)"
        logger.info('save--> %s' % sql)
        save_success = True
        try:
            # 执行sql语句
            self.cursor.execute(sql, (item['describe'], item['url_view'], item['url_down']))
            logger.info('插入成功 %s ' % str(item))
        except Exception as e:
            save_success = False
            logger.error('插入失败 %s ' % str(item))
        return save_success

    def release(self):
        """
        释放连接
        """
        logger.info('关闭mysql连接')
        self.conn.close()

    def ensure_table(self):
        """
        确保表存在，判断表是否存在,如果不存在则创建表
        """
        try:
            sql = "SELECT * FROM clsq limit 1; "
            self.cursor.execute(sql)
        except ProgrammingError:
            sql = "CREATE TABLE `clsq` (" \
                  "  `id` int(11) NOT NULL AUTO_INCREMENT," \
                  "  `descr` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL," \
                  "  `url_view` varchar(255) DEFAULT NULL," \
                  "  `url` varchar(255) DEFAULT NULL," \
                  "  PRIMARY KEY (`id`)\n" \
                  ") ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;"
            self.cursor.execute(sql)


db = MysqlDb()
save_item = db.save
