# -*- coding: utf-8 -*-
# @FileName: http_util.py
# @Description: Http请求工具类
# @Author : jaceding
# @Time : 2019/12/8

import requests


def url_open(url, encoding='utf-8') -> str:
    """
    获取目标网站整个网页的HTML
    :param url: 目标网站
    :param encoding: 字符编码 默认为utf-8
    :return: 网页HTML
    """
    headers = {
        'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) '
                      'AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50 ',
    }
    req = requests.get(url, headers=headers, verify=False, timeout=10)
    req.encoding = encoding
    return req.text


def get_redirect_url(url) -> str:
    """
    获取重定向后的URL
    :param url: 重定向前的URL
    :return: 重定向后的URL
    """
    headers = {
        'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) '
                      'AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50 ',
    }
    req = requests.get(url, headers=headers, verify=False, timeout=10)
    return req.url
