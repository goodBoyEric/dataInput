# -*- coding:UTF-8 -*-
# !/usr/bin/env python3
# _author=liusong time= 2017/9/4 0004

import re
from public.public_api.newLogger import logger
import unittest.test

class ResponseRegular(object):
    def __init__(self):
        self.regularExp = list()
        # self.regular_response = None
        self.regular_expression = list()
        self.regular_response_list = list()

    def data_find(self):
        for i in self.regularExp:
            regular_response = re.findall(i, self.text)
            self.regular_response_list.append(regular_response)
        return self.regular_response_list

    @property
    def response_data_function(self):
        return self.text

    @response_data_function.setter
    def response_data_function(self, text):
        self.text = text

    @property
    def regular_exp_function(self):
        return self.regular_expression

    @regular_exp_function.setter
    def regular_exp_function(self, *regular_exp):
        self.regular_expression = regular_exp


class AssertRegular(ResponseRegular):

    def __init__(self, http_response, *assert_data):
        logger.debug('class:AssertRegular,httpResponse:%s ,assertData:%s' % (http_response, assert_data))
        super(AssertRegular, self).__init__()
        try:
            if not isinstance(assert_data, tuple):
                raise ValueError('Assert Regular class ,assertData 存在问题')
            self.code = http_response.status_code
            self.text = http_response.text
            self.header = http_response.headers
            self.regularExp = assert_data
        except Exception as err:
            logger.error('__init__:%s' % err)

    def assert_result(self):
        """
        :return: 返回断言结果的字典及测试用例结果
        """
        pass_or_fai_dict, regular_response_dict = {}, {}

        # 判断断言选项是不是为空，为空认为此测试用例为准备类测试用例
        if self.regularExp == ():
            pass_or_fai_dict = {}
            pass_or_fail_result = ''
        else:
            for i in self.regularExp:
                regular_response = re.findall(i, self.text)

                # 判断返回状态代码是否正确
                if self.code == 200:
                    if regular_response != list():
                        pass_or_fail = 'Pass'
                    else:
                        pass_or_fail = 'Fail'
                else:
                    pass_or_fail = 'Fail'
                pass_or_fai_dict[i] = pass_or_fail

            # 通过判断所有断言结果来判定此用例结果是否正确
            if list(pass_or_fai_dict.values()).count('Fail') > 0:
                pass_or_fail_result = 'Fail'
            else:
                pass_or_fail_result = 'Pass'
        return pass_or_fai_dict, pass_or_fail_result


def get_data_by_regular(http_response, **regular_exp):
    """
    :param http_response:http协议响应（包括响应头与响应正文）
    :param regular_exp: 正则提示的相关数据
    :return: 返回一个引用名称与正则结果字典
    """
    regular_result_dict = dict()
    if regular_exp != dict():
        for exp, regular in regular_exp.items():
            regular_result = re.findall(regular, http_response.text)
            regular_result_dict[exp] = regular_result[0]
        del http_response, regular_exp
    return regular_result_dict


def replace_data(row_data):
    """
    :param row_data: 输入具体行数据
    :return: 对于2, 3, 4, 5, 8这几行数据进行eval操作,若为空返回相应数据类型
    """
    try:
        if isinstance(row_data, list):
            replace_list = [2, 3, 4, 5, 8]
            for i in replace_list:
                if row_data[i] != '':
                    row_data[i] = eval(row_data[i])
                elif row_data[i] == '' and (i == 2):
                    row_data[i] = list()
                elif row_data[i] == '' and (i == 5):
                    row_data[i] = tuple()
                elif row_data[i] == '' and (i == 3 or i == 4 or i == 8):
                    row_data[i] = dict()
                else:
                    raise ValueError('恢复数据类型存在错误')
        else:
            raise ValueError('row data存在错误')
    except Exception as err:
        logger.error('函数：replace data，存在错误：%s' % err)
    else:
        logger.debug('函数：replace data，完成操作')
    return row_data
# regularExp = ['rowcount:([0-9]{3,})','rac01ncialYer":([0-9]){1,},']
# header = {'cookie':'JSESSIONID=9689EF263B2DAF75064D0D4B074599CE'}
# createSession = requests.Session()
# responseData = createSession.post('http://219.239.83.21:8081/ITAS/rac/journal/search/listdata.do',
#                    data={"":"","axgrid_listcols":"crac01IssueDate,crac01VoucherNo,crac01Description,totalAmount,"
#                                                  "crac01Status,crac01OperationOffice","axgridid":"gridview","crac01Status":"",
#                          "crac01VoucherNo":"","gridview_pageSize":"10","gridview_sort":"","gridview_startIndex":"0",
#                          "issueDateFrom":"01-04-2017","issueDateTo":"31-03-2018"},headers = header)
# print(responseData.text)
# aa = AssertRegulaer(responseData , *regularExp)
# bb , cc , dd = aa.assertResult
# print(bb ,cc , dd)
