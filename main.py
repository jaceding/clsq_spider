# -*- coding: utf-8 -*-
# @FileName: main.py
# @Description: 主程序
# @Author : jaceding
# @Time : 2019/12/8

import time
import random
import base64
from spider.get_list import get_list
from spider.get_item import get_item
from utils.mysql_util import db
from utils.mail_util import send_info
from utils.http_util import get_redirect_url
from utils.log_util import logger


def start(domain):
    """
    主方法
    :param domain: 域名
    """
    start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    total_num = 0
    success_num = 0
    try:
        # 确保表结构存在
        db.ensure_table()
        link_list = get_list(domain=domain)
        total_num = len(link_list)
        for index, link in enumerate(link_list):
            try:
                item = get_item(link)
                if item is None:
                    continue
                else:
                    if item['url_down'] is not None and item['url_down'].strip() != '':
                        success_num += 1
                    db.save(item)
            except Exception as e:
                logger.error(str(e))
            finally:
                logger.info('main --> %.2f%%' % ((index + 1) / total_num))
                if (index + 1) != total_num:
                    sleep_time = random.randint(20, 40)
                    logger.info('main --> thread sleep %ds' % sleep_time)
                    time.sleep(sleep_time)
    except Exception as e:
        logger.error(str(e))
    finally:
        # 释放连接
        db.release()

    end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    send_info(total_num, success_num, start_time, end_time)


if __name__ == '__main__':
    logger.info('### start ###')
    url = 'aHR0cDovL2NjLm84ZC53aW4='
    url2 = get_redirect_url(base64.b64decode(url).decode('utf-8')).replace('https', 'http')
    logger.info('url2 # ' + url2)
    url3 = get_redirect_url(url2 + "/new.php").replace('https', 'http')
    logger.info('url3 # ' + url3)
    start(domain=url3)
    logger.info('### end ###')

