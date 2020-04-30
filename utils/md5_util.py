# -*- coding: utf-8 -*-
# @FileName: mail_util.py
# @Description: md5工具类
# @Author : jaceding
# @Time : 2020/04/29

import hashlib


def encode(message: str) -> str:
    """
    md5加密字符串
    :param message: 加密前的字符串
    :return: 加密后的字符串
    """
    b = message.encode(encoding='utf-8')
    str_md5 = hashlib.md5(b).hexdigest()
    return str_md5
