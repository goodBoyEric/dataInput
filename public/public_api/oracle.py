# coding:utf-8
# !/usr/bin/python3
import cx_Oracle
from public.public_api.newLogger import logger


class Oracle(object):
    def __init__(self, **list_first_data):
        logger.debug("类：Oracle，接收数据list first data：%s" % str(list_first_data))
        self.password = None
        if not isinstance(list_first_data, dict):
            raise ValueError('%s do not a dict.' % list_first_data)
        try:
            dns = cx_Oracle.makedsn(list_first_data['url'], list_first_data['port'], list_first_data['oracle_name'])
            self.oracle_connection = cx_Oracle.Connection(list_first_data['username'], list_first_data['password'], dns)
            self.oracle_cursor = cx_Oracle.Cursor(self.oracle_connection)
        except Exception as err:
            logger.error('Oracle():%s' % err)
        else:
            logger.debug('类：Oracle，完成初始化')

    @property
    def first_login_function(self):
        return self.password

    @first_login_function.setter
    def first_login_function(self, username):
        sql_password = """select t.password from APEX_USER_LOGIN t where t.login_name = '%s'""" % username
        response_data = self.oracle_cursor.execute(sql_password)
        self.password = response_data.fetchone()[0]
        logger.debug('用户登录password:%s' % self.password)

    def oracle_cursor_function(self):
        return self.oracle_cursor

    def oracle_sql_execute_function(self, sql, response=3):
        """
        :param sql:
        :param response: 1为返回单行数据
                          2为返回所有数据
                          3为执行语句，无返回值
        :return:
        """
        oracle_sql_response = None
        if response not in [1, 2, 3]:
            raise ValueError('response 输入错误')
        self.oracle_cursor.execute(sql)
        if response == 1:
            oracle_sql_response = self.oracle_cursor.fetchone()
        elif response == 2:
            oracle_sql_response = self.oracle_cursor.fetchall()
        elif response == 3:
            self.oracle_connection.commit()
            oracle_sql_response = True
        else:
            logger.error('')
        return oracle_sql_response

# 57 oracle
# database = {
#     'url': '192.168.169.77',
#     'port': '1521',
#     'oracle_name': 'itas',
#     'username': 'itas',
#     'password': 'Itas_2017'
#             }
# 60 oracle
# database = {
#             'url': '192.168.169.77',
#             'port': '1521',
#             'oracle_name': 'itas',
#             'username': 'intgadm',
#             'password': 'intgadm'
#             }
# aa = Oracle(**database)
# # aa.first_login_function = 'tacoff01'
# bb = aa.first_login_function
# print(bb)
# sql =  "update tppr02_till_base a set a.till_status= 'RECONCILE' " \
#                                  "where a.till_status  not in ('RECONCILE','DISCARD')"
# sql = """
# select t.cppr01_office_sys_guid,t.cppr01_office_status from tppr01_pay_office_business t
# """
# bb = aa.oracle_sql_execute_function(sql=sql,response=2)
# print(type(bb[1]))
