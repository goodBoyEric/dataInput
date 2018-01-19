# coding:utf-8
# !/usr/bin/python3

import os
import time
from selenium.webdriver import Chrome
# from selenium.webdriver.common.by import By


def get_public_path_function():
    try:
        get_public_path = os.getcwd()
        # print(type(getPublicPath))
        data_position = get_public_path.find('dataInput')
        get_public_path = get_public_path[0:data_position + 10]
    # getPublicPath.
        return get_public_path
    except OSError as err:
        print('getPublicPathFunction', err)

public_path = get_public_path_function()
# print(publicPath)

# config文件
systemConfig = public_path + '\\config\\systemConfig.conf'
# print(systemConfig)

# data_excel文件
excel_publicPath = public_path + '\\data_excel\\data.xlsx'
# print(excel_publicPath)

# 临时文件地址
temporaryFile = public_path + '\\temporaryFile\\tem.txt'
temporaryFile_web_01 = public_path + '\\temporaryFile\\tem_web_01.txt'
temporaryFile_web_02 = public_path + '\\temporaryFile\\tem_web_02.txt'
temporaryFile_web_03 = public_path + '\\temporaryFile\\tem_web_03.txt'
temporaryFile_web_04 = public_path + '\\temporaryFile\\tem_web_04.txt'
temporaryFile_web_05 = public_path + '\\temporaryFile\\tem_web_05.txt'


# log存放地址
logFile = public_path + '\\log\\log.txt'

# Excel存放地址
excel_result_address = public_path + '\\data_excel\\result.xlsx'
# print(excel_result_address)

# Local Time
Local_Time = time.strftime('%d-%m-%Y', time.localtime())

# 浏览器驱动
browser_driver = Chrome()
# browser_driver.find_element().is_displayed()

# iframe
iframe_element = 'mainFrame'
iframe_reg_req_app = '_ax_frm_frame_'
iframe_element_vat_details = 'topPopModalCommonFrame'

# reg url
menu_id_search_reg_req = '89199741-1cfb-477f-9fe9-2b52e34940a8'
menu_id_search_reg_main = '099f73a3-4898-4d48-a3ba-fa5f854fe58f'
menu_id_search_reg_operation = '32293007-90f6-40e0-971b-8f18e9b445b9'

# ret url
menu_id_search_ret_return = '8ba2131b-93a4-4d56-82b2-41d95fc4b87d'
menu_id_search_ret_batch = '847cf223-6b62-4bb8-982c-b331e4b9f2e4'

# tac url
menu_id_search_tac_transaction = '2b0ca8ba-2820-43d8-b94b-7217e29ebaf7'
menu_id_search_tac_journal = '9ffadd3b-f1a8-4947-9086-5a6dfb0d75e8'
menu_id_search_tac_payment_extension = '07a9ca1d-7137-4ff4-ac79-4bbf2221b96c'
menu_id_search_tac_running_balance = 'ce37c350-dc42-4d4f-85c2-113da35984a9'
menu_id_search_tac_taxpayer_statement = '1fc7da33-af13-45fc-9b03-dc1809e47c9a'
menu_id_search_tac_tax_refund = 'f2985e9f-5f89-4258-9285-6f4b17c05ea0'
menu_id_search_tac_nontax_refund = '553d6ac5-0128-4d70-8ab7-70fa417cb0bb'
menu_id_search_tac_tourist_refund = '3ad6d897-3974-48e2-812c-027fec38bc53'
menu_id_search_tac_clearance_certificates = '7d5606ab-c1e6-46a9-983c-9eb8c43d4390'

# ppr
menu_id_search_ppr_office = 'ca6c94ab-4bcd-4f0e-bc9e-5e78081b12fa'
menu_id_search_ppr_till = '620ac4cf-0984-454a-a678-c7719221938e'
menu_id_search_ppr_payment = '0f817e0f-b9c5-42a6-977b-f9a05cb94af6'

# 57系统测试地址
url = 'http://192.168.168.57:8080/ITAS/login'
common_url = 'http://192.168.168.57:8080/ITAS/apexIndex?targetMenuId='
username = 'tacoff01'
password = '12345a*'
database = {
    'url': '192.168.169.77',
    'port': '1521',
    'oracle_name': 'itas',
    'username': 'itas',
    'password': 'Itas_2017'
            }

# 60系统测试地址
# url = 'http://192.168.168.60:8080/ITAS/login'
# common_url = 'http://192.168.168.60:8080/ITAS/apexIndex?targetMenuId='
# username = 'tacoff01'
# password = '12345a*'
# database = {
#             'url': '192.168.169.77',
#             'port': '1521',
#             'oracle_name': 'itas',
#             'username': 'intgadm',
#             'password': 'intgadm'
#             }
