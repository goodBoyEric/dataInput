# -*- coding:UTF-8 -*-
# !/usr/bin/env python3
# _author = liusong time = 2018/1/16
from selenium.webdriver.common.by import By
from public.public_api.oracle import Oracle
from public.public_web.base.globalVariable import *
from public.public_web.elements_inputdata.ppr.element.element_ppr_till import *


class PPROffice:
    def __init__(self, driver, **oracle_data):
        self.driver = driver
        self.URL_PPROffice = common_url + menu_id_search_ppr_office
        self.oracle = Oracle(**oracle_data)

    def open_office(self, current_time):
        time.sleep(2)
        self.driver.get(self.URL_PPROffice)
        time.sleep(2)
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame(iframe_element)
        # 获取office状态
        office_current_status = self.driver.find_element(
            by=By.ID, value=PPR_Office_Status).get_attribute('defvalue')
        # 获取office时间
        office_current_time = self.driver.find_element(
            by=By.ID, value=PPR_Office_Business_Date).get_attribute('value')
        print(office_current_status)
        if office_current_status == 'CL':
            print(office_current_time)
            self.driver.find_element(by=By.ID, value=PPR_Office_Open_button).click()
        elif office_current_status == 'OP' and office_current_time != current_time:
            # till 状态更新
            update_till_status = """update tppr02_till_base a set a.till_status= 'RECONCILE'
                                where a.till_status  not in ('RECONCILE','DISCARD') """
            self.oracle.oracle_sql_execute_function(sql=update_till_status)
            self.driver.find_element(by=By.ID, value=PPR_Office_Close_button).click()
            time.sleep(2)
            self.driver.find_element(by=By.ID, value=PPR_Office_Open_button).click()
