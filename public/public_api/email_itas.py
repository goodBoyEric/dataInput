# !/usr/bin/env python3
# coding: utf-8

import configparser
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from public.public_api.newLogger import logger
from public.public_web.base.globalVariable import systemConfig


class SendEmail(object):
    def __init__(self, data_excel, excel_result_address):
        pass

    def __new__(cls, data_excel, excel_result_address):
        if not hasattr(cls, 'emailConfig'):
            cls.emailConfig = super(SendEmail, cls).__new__(cls)
            email_config_cursor = configparser.ConfigParser()
            email_config_cursor.read(filenames=systemConfig, encoding='utf-8')
            cls.emailConfig.senderAndUsername = email_config_cursor.get('email', 'senderAndUsername')
            cls.emailConfig.receiver = email_config_cursor.get('email', 'receiver')
            cls.emailConfig.password = email_config_cursor.get('email', 'password')
            cls.emailConfig.host = email_config_cursor.get('email', 'host')
            cls.emailConfig.port = email_config_cursor.get('email', 'port')
            cls.emailConfig.excel_result_address = excel_result_address
            cls.emailConfig.dataExcel = data_excel
        return cls.emailConfig

    def send_email_function(self):
        try:
            email_multipart = MIMEMultipart('related')
            email_multipart['Subject'] = '测试结果' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

            email_attach01 = MIMEText(open(self.dataExcel, 'rb').read(), _subtype='base64', _charset='utf-8')
            email_attach01['Content-Type'] = 'application/octet-stream'
            email_attach01['Content-Disposition'] = 'attachment; filename="data.xlsx"'

            email_attach02 = MIMEText(open(self.excel_result_address, 'rb').read(), _subtype='base64', _charset='utf-8')
            email_attach02['Content-Type'] = 'application/octet-stream'
            email_attach02['Content-Disposition'] = 'attachment; filename="result.xlsx"'

            email_text = MIMEText('大家好：' + '\n' + '\n'
                                  '这是一封自动发送的邮件，邮件内容是本次接口测试的结果，'
                                  '请查看，如有问题请与我联系。')

            email_multipart.attach(email_attach01)
            email_multipart.attach(email_attach02)
            email_multipart.attach(email_text)

            send_function = smtplib.SMTP()
            send_function.connect(host=self.host, port=self.port)
            send_function.login(user=self.senderAndUsername, password=self.password)
            send_function.sendmail(from_addr=self.senderAndUsername,
                                   to_addrs=self.receiver, msg=email_multipart.as_string())
            send_function.quit()
        except Exception as err:
            logger.exception(err, exc_info=True)
        else:
            logger.debug('email初始化完成')


# sendInit = SendEmail('E:\\dataInput\\data_excel\\result.xlsx')
# sendInit.sendEmailFunction()
