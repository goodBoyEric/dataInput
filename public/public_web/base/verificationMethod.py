# -*- coding:UTF-8 -*-
# !/usr/bin/env python3
# _author = liusong time = 2017/11/1 0001

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from public.public_web.base.globalVariable import iframe_element, iframe_reg_req_app
from public.public_web.elements_inputdata.reg.RegMaintainTaxpayer.element.element_contact_information import *
from public.public_web.elements_inputdata.tac.element.element_tac_transaction import *


class SearchPublicFunction(object):
    def __init__(self, driver):
        self.driver = driver

    def search_verification(self, url, col_or_selector, iframe='mainFrame', **kwargs):
        # 转到需要验证界面
        self.driver.implicitly_wait(time_to_wait=10)
        self.driver.get(url=url)

        # 判断col输入是数字还是定位方式
        if type(col_or_selector) is int:
            col_selector = '#gridview>tbody>tr:nth-child(1)>td:nth-child(' + str(col_or_selector) + ')'
        else:
            col_selector = col_or_selector

        # 跳转iframe至主
        self.driver.implicitly_wait(10)
        self.driver.switch_to_frame(iframe)
        for i, j in kwargs.items():
            if i == 'ID':
                by = By.ID
            elif i == 'XPATH':
                by = By.XPATH
            elif i == 'CSS':
                by = By.CSS_SELECTOR
            else:
                raise AttributeError('search_verification err')
            for x, y in j.items():
                self.driver.find_element(by=by, value=x).send_keys(y)

        self.driver.implicitly_wait(time_to_wait=10)
        self.driver.find_element(by=By.ID, value='btnSearch').click()
        time.sleep(2)
        self.driver.implicitly_wait(time_to_wait=10)
        # js = """document.getElementById('gridview').value='aaa ';
        # """
        # col_data = self.driver.execute_script(script=js
        col_data = self.driver.find_element(by=By.CSS_SELECTOR, value=col_selector).text
        return col_data


def contact_information_verification(driver):
    time.sleep(3)
    verify_data_list = []
    driver.switch_to_default_content()
    driver.switch_to_frame(iframe_element)
    driver.switch_to_frame(iframe_reg_req_app)

    # 获取数据
    a = driver.find_element(by=By.ID, value=Primary_Telephone_Second).text
    print('Primary_Telephone_Second:%s' % a)
    verify_data_list.append(int(driver.find_element
                                (by=By.ID, value=Primary_Telephone_Second).get_attribute(name='value')))
    verify_data_list.append(int(driver.find_element
                                (by=By.ID, value=Primary_Telephone_Last).get_attribute(name='value')))
    verify_data_list.append(int(driver.find_element
                                (by=By.ID, value=Other_Telephone_Second).get_attribute(name='value')))
    verify_data_list.append(int(driver.find_element
                                (by=By.ID, value=Other_Telephone_Last).get_attribute(name='value')))
    verify_data_list.append(int(driver.find_element
                                (by=By.ID, value=Fax_Fax2Email_Second).get_attribute(name='value')))
    verify_data_list.append(int(driver.find_element
                                (by=By.ID, value=Fax_Fax2Email_Last).get_attribute(name='value')))
    verify_data_list.append(int(driver.find_element
                                (by=By.ID, value=Cellphone_Second).get_attribute(name='value')))
    verify_data_list.append(driver.find_element(by=By.ID, value=Email_Address).get_attribute(name='value'))

    return verify_data_list


def return_post_verification(driver, url, tin, tax_type, year=2018):
    """
   VAT:1
   ITX:2
   """
    driver.get(url)
    time.sleep(2)
    driver.switch_to_default_content()
    driver.switch_to_frame(iframe_element)
    # tin&tax type&year
    driver.find_element(by=By.ID,value=TTransaction_TIN).send_keys(tin)
    driver.find_element(by=By.ID,value=TTransaction_TaxYear).send_keys(year)
    select_taxtype = driver.find_element(by=By.ID,value=TTransaction_TaxType)
    Select(select_taxtype).select_by_value(str(tax_type))
    # search button
    time.sleep(1)
    driver.find_element(by=By.ID, value=TTransaction_Search_button).click()
    time.sleep(2)
    assessment_amount = float(driver.find_element(by=By.CSS_SELECTOR, value=TTransaction_Table_Data).text)
    print(assessment_amount)
    return assessment_amount
