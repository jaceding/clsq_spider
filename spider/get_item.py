# -*- coding: utf-8 -*-
# @FileName: get_item.py
# @Description: 
# @Author : jaceding
# @Time : 2019/12/8

import time
import random
import base64
from lxml import etree
from utils.http_util import url_open
from utils.log_util import logger

describe_re = base64.b64decode('IC0g5Zyo57ar5oiQ5Lq65b2x6ZmiIHwg6I2J5qa056S+5Y2AIC0gdDY2eS5jb20='.encode('utf-8')).decode("utf-8")


def get_item(url):
    """
    解析 播放页面 并封装成视频对象
    :param url: 播放页面
    :return: 视频对象
    """
    try:
        logger.info('get_item-->: ' + url)
        target_html = url_open(url, encoding='gbk')
        selector = etree.HTML(target_html)
        a_onclick_src = selector.xpath(
            '//div[@class="tpc_content do_not_catch"]/a[@style="cursor:pointer"]/@onclick')[0]
        if a_onclick_src is None:
            logger.htm(target_html, url)
            return None
        describe = selector.xpath('//head/title/text()')[0]
        describe = str(describe).replace(describe_re, '')
        url_index_left = a_onclick_src.find("src=")
        url_view = str(a_onclick_src[url_index_left + 5:len(a_onclick_src) - 1])
        url_view = url_view.replace(' ', '').replace('#iframeload', '')
        time.sleep(random.randint(5, 10))
        url_down = get_download_url(url_view)
        item = {'describe': describe, 'url_view': url_view, 'url_down': url_down}
    except Exception as e:
        logger.error('获取详细信息失败，原因：' + str(e))
        return None
    return item


def get_download_url(url_view: str) -> str:
    """
    根据 可播放URL 解析出 可下载URL
    :param url_view: 可播放URL
    :return: 可下载URL
    """
    logger.info('get_download_url-->: ' + url_view)
    try:
        html = url_open(url_view)
        flag = 'video_url:'
        index1 = html.find(flag)
        if index1 == -1:
            index1 = html.find('video:')
            if index1 == -1:
                logger.info('----html---')
                logger.info(html)
                logger.info('----html----')
                logger.htm(message=html, url=url_view)
                return None
            index2 = html.find('.mp4', index1, index1 + 255)
            download_url = html[index1 + len('video:'):index2 + 4].strip().replace('\'', '')
        else:
            index2 = html.find(',', index1, index1 + 255)
            download_url = html[index1 + len(flag):index2].strip().replace('\'', '')

    except Exception as e:
        logger.error('获取下载链接失败，原因：' + str(e))
        return None
    # 去除function/0/
    if len(download_url) > 0 and download_url.find('function/0/') >= 0:
        download_url = download_url.replace('function/0/', '')
    return download_url.replace(' ', '')
