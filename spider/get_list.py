# -*- coding: utf-8 -*-
# @FileName: getlist.py
# @Description: 获取昨天的所有链接
# @Author : jaceding
# @Time : 2019/12/8

import time
import random
from utils.http_util import url_open
from utils.log_util import logger
from lxml import etree


def get_list(url='/thread0806.php?fid=22&search=&page=',
             domain='http://cl.epek.icu', num=1) -> set:
    """
    获取今天的所有链接
    :param domain: 域名 方便提取出连接后进行拼接
    :param num: 第几页
    :param url: 默认值 http://cl.epek.icu/thread0806.php?fid=22&search=&page=
    :return:
    """
    if not url.__contains__(domain):
        url = domain + url
    item_list = set()
    target_url = url + str(num)
    logger.info('get_list-->: ' + target_url)
    target_html = url_open(target_url, encoding='gbk')
    selector = etree.HTML(target_html)
    items = selector.xpath('.//table[@id="ajaxtable"]//tr[@class="tr3 t_one tac"]')
    for item in items:
        item_date = item.xpath('.//div[@class="f12"]/span[@class="s3"]/text()')
        if len(item_date) <= 0 or '' == item_date[0].strip():
            continue
        if item_date[0].strip().find('今天') >= 0:
            item_link = item.xpath('.//td[@class="tal"]/h3/a/@href')
            item_list.add(domain + '/' + item_link[0].strip())
        else:
            logger.info('第%d页：size-->: %d' % (num, len(item_list)))
            return item_list
    logger.info('第%d页：size-->: %d' % (num, len(item_list)))
    if len(item_list) == 0:
        return item_list
    sleep_time = random.randint(20, 40)
    logger.info('get_list --> thread sleep %ds' % sleep_time)
    time.sleep(sleep_time)
    num += 1
    item_list_ex = get_list(url, domain, num)
    item_list = item_list | item_list_ex
    logger.info('总数-->: %d' % len(item_list))
    return item_list
