# coding:utf-8
# !/usr/bin/evn python3

import configparser
import requests.sessions

from public.public_api.newLogger import logger
from public.public_api.oracle import Oracle
from public.public_web.base.globalVariable import systemConfig


class Config(object):
    def __init__(self):
        pass

    def __new__(cls, config_file_address=systemConfig):
        try:
            if not hasattr(cls, 'config'):
                # 创建属性&在属性下命名数值
                cls.config = super(Config, cls).__new__(cls)
                open_config = configparser.ConfigParser()
                open_config.read(config_file_address)

                # 通过config获取数据
                cls.config.login_mode = open_config.get('loginMode', 'loginMode')
                cls.config.cookie = open_config.get('cookie', 'cookie')
                cls.config.environment = open_config.get('environment', 'environment')

                # 通过判断配置中的环境变量来读取使用环境
                cls.config.database = (open_config.get(cls.config.environment, 'database')).split(",")
                cls.config.url = open_config.get(cls.config.environment, 'URL')
                cls.config.userneme = open_config.get(cls.config.environment, 'userneme')
        except Exception as err:
            logger.error('出现错误%s' % err)
        else:
            logger.debug('类：Config，完成初始化')
        return cls.config

    def data_base_function(self):
        return self.database

    def url_function(self):
        return self.url


class PostData(Config):
    def __init__(self):
        super(PostData, self).__init__()
        # 创建session
        self.itas_session = requests.Session()
        try:
            if self.login_mode == 'login':
                # 连接数据查询登录用户的密码&组装首次登录post data
                connect_oracle = Oracle(*self.database)
                connect_oracle.first_login_function = self.userneme
                password = connect_oracle.first_login_function
                first_login_data = {'username': self.userneme, 'password': password, 'language': ''}

                # 创建session
                aa = self.itas_session.post(url=(self.url + "/ITAS/login"), data=first_login_data)
                print(aa.text)
                # 可以对此次传输的cookie进行存放，此方法与cookie方式类似
                self.JSESSIONID = self.itas_session.cookies.get('JSESSIONID')

            # cookie方式，直接将cookie添加到headers
            elif self.login_mode == 'cookie':
                logger.debug('cookie 登录方式')
            else:
                raise ValueError('login Mode方式设置错误')
        except Exception as err:
            logger.error('初始化出现错误：%s' % err)
        else:
            logger.debug('类：PostData，完成初始化')

    def create_jsession_id(self):
        return self.JSESSIONID

    def create_session(self):
        return self.itas_session

    def post_data_function(self, http_mode, url_path, data, post_header):
        # 组装登录所用
        all_url = self.url + url_path
        update_headers = dict()
        post_data_variable = None
        try:
            if not isinstance(data, dict):
                post_data = eval(data)
            else:
                post_data = data
            # 按照不同的测试Mode进行数据发送
            if self.login_mode == 'cookie':
                update_headers = {'cookie': 'JSESSIONID=' + self.cookie}
                update_headers.update(post_header)
            elif self.login_mode == 'login':
                update_headers = {'cookie': 'JSESSIONID=' + self.JSESSIONID}
                update_headers.update(post_header)
            else:
                logger.error('函数：post_data_function  login mode：%s存在错误' % self.login_mode)
            print(all_url, post_data, update_headers)
            # logger.debug(all_url, str(post_data), str(update_headers))

            if http_mode == 'Post':
                post_data_variable = self.itas_session.post(url=all_url, data=post_data, headers=update_headers)
            elif http_mode == 'Get':
                post_data_variable = self.itas_session.get(url=all_url, data=post_data, headers=update_headers)
            else:
                post_data_variable = None
                raise ValueError('http_mode')
            print(post_data_variable.text)
            logger.debug(post_data_variable.text)
        except Exception as err:
            logger.error(' 出现错误%s' % err)
        else:
            logger.debug('方法：postDataFunction，完成初始化。')
        return post_data_variable

# aa = PostData()
# data = {"": "", "axgrid_listcols": "crac01IssueDate,crac01VoucherNo,crac01Description,totalAmount,"
#                             "crac01Status,crac01OperationOffice", "axgridid": "gridview", "crac01Status": "",
#  "crac01VoucherNo": "", "gridview_pageSize": "10", "gridview_sort": "", "gridview_startIndex": "0",
#  "issueDateFrom": "01-04-2017", "issueDateTo": "31-03-2018"}
# headers = {}
# bb = aa.postDataFunction(httpMode = 'Post' ,
#                          URL_path = r'/ITAS/rac/journal/search/listdata.do',data=data , postHeader= headers)
# print(bb.text)
# print(bb.status_code)
