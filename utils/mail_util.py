# -*- coding: utf-8 -*-
# @FileName: mail_util.py
# @Description: 邮件工具类
# @Author : jaceding
# @Time : 2019/12/8
import os
import smtplib
from email.mime.text import MIMEText
from utils.log_util import logger


def send_info(total_num, success_num, start_time, end_time):
    """
    发送邮件通知
    :param total_num: 总数
    :param success_num: 成功数
    :param start_time: 开始时间
    :param end_time: 结束时间
    """
    receiver = os.environ.get('MAIL_ACCOUNT')
    content = '<h1>clsq_spider</h1>'
    content += '<br/>'
    content += '<h4>total:' + str(total_num) + '</h4>'
    content += '<h4>success:' + str(success_num) + '</h4>'
    content += '<h4>task start in :' + str(start_time) + '</h4>'
    content += '<h4>task end in :' + str(end_time) + '</h4>'
    subject = 'clsq_spider task info'
    send(receiver, content, subject)


def send(receiver, content, subject) -> bool:
    """
    :param receiver: 接收人邮箱
    :param content: 邮件内容
    :param subject: 邮件主题
    """
    success = True
    mailserver = 'smtp.qq.com'  # QQ邮箱服务器地址S

    sender = os.environ.get('MAIL_ACCOUNT')  # 发件人邮箱用户名
    password = os.environ.get('MAIL_PASSWORD')  # 发件人邮箱密码（授权码）

    mail = MIMEText(content, 'html', 'utf-8')
    mail['Subject'] = subject
    mail['From'] = sender  # 发送者
    mail['To'] = receiver  # 接收者

    try:
        smtp = smtplib.SMTP_SSL(mailserver, port=465)  # QQ邮箱的服务器和端口号
        smtp.login(sender, password)  # 登录邮箱

        # 参数分别是发送者，接收者，第三个是把上面的发送邮件的内容变成字符串
        smtp.sendmail(sender, receiver, mail.as_string())
        smtp.quit()  # 发送完毕后退出smtp
    except Exception as e:
        logger.error(str(e))
        success = False

    return success
