# -*- coding: utf-8 -*-
# @FileName: http_util.py
# @Description: 日志工具类
# @Author : jaceding
# @Time : 2020/04/15

import logging
import logging.handlers
import os
import time
import platform
from utils.md5_util import encode


# 根据操作系统 -> 设置文件路径
sys = platform.system()
if sys == 'Windows':
    logs_dir = 'logs'
    htm_dir = 'htm'
elif sys == 'Linux':
    logs_dir = '/usr/log'
    htm_dir = '/usr/htm'
# 日志级别
level = logging.DEBUG
# 设置输出格式
formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')


class Logs(object):

    def __init__(self):
        self.logger = logging.getLogger()

        # 创建文件目录
        if os.path.exists(logs_dir) and os.path.isdir(logs_dir):
            pass
        else:
            os.mkdir(logs_dir)

        # 修改log保存位置
        logfilename = '%s.log' % time.strftime('%Y-%m-%d', time.localtime())
        logfilepath = os.path.join(logs_dir, logfilename)

        # 文件句柄
        rotatingFileHandler = logging.handlers.RotatingFileHandler(filename=logfilepath,
                                                                   maxBytes=1024 * 1024 * 50,
                                                                   backupCount=5,
                                                                   encoding='utf-8')
        rotatingFileHandler.setFormatter(formatter)

        # 控制台句柄
        console = logging.StreamHandler()
        # console.setLevel(logging.INFO)
        console.setFormatter(formatter)

        # 添加内容到日志句柄中
        self.logger.addHandler(rotatingFileHandler)
        self.logger.addHandler(console)
        self.logger.setLevel(level)

    def info(self, message):
        self.logger.info(message)

    def debug(self, message):
        self.logger.debug(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def htm(self, message, url):
        name = encode(url)
        file = htm_dir + os.sep + name + '.html'
        f = open(file, "w+")
        f.write(message)
        f.close()


logger = Logs()
logger.info("log file: " + logs_dir)
logger.info("html file: " + htm_dir)
