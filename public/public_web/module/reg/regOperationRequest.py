# -*- coding:UTF-8 -*-
# !/usr/bin/env python3
# _author = liusong time = 2017/12/27

import time
from public.public_web.base.globalVariable import *
from selenium.webdriver.common.by import By
from public.public_web.elements_inputdata.reg.regOperationRequest.element.element_search import *


class REGOperationRequest:
    def __init__(self, driver):
        self.driver = driver
        self.sleep_time = self.driver.implicitly_wait(time_to_wait=10)
        self.URL_REGOperationRequest = common_url + menu_id_search_reg_operation

    def search(self, tin, status):
        or_request_status_index_css_update = ''
        self.driver.implicitly_wait(time_to_wait=10)
        self.driver.get(self.URL_REGOperationRequest)
        self.driver.switch_to_frame(iframe_element)
        # 输入TIN
        self.driver.find_element(by=By.ID, value=OR_Search_TIN).send_keys(tin)
        # 输入相关状态
        self.driver.find_element(by=By.ID, value=OR_Request_Status).click()
        if status == 'submit':
            or_request_status_index_css_update = OR_Request_Status_index_CSS + '5)'
        elif status == 'approve':
            or_request_status_index_css_update = OR_Request_Status_index_CSS + '7)'
        else:
            print('search function: status err')
        self.driver.find_element(by=By.CSS_SELECTOR, value=or_request_status_index_css_update).click()
        self.driver.find_element(by=By.ID, value=OR_Search_button).click()
        time.sleep(2)
        self.driver.find_element(by=By.CSS_SELECTOR, value=OR_Table_Data_CSS).click()

    def process_button(self):
        self.driver.find_element(by=By.ID, value=OR_Process_button).click()

    def approve(self, tin):
        self.search(tin, status='submit')
        self.process_button()
        self.driver.implicitly_wait(time_to_wait=10)
        time.sleep(5)
        # 修改iframe
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame(iframe_element)
        self.driver.switch_to_frame(iframe_reg_req_app)
        self.driver.find_element(by=By.ID, value=OR_Approve_button).click()
        self.driver.implicitly_wait(time_to_wait=10)
        self.driver.switch_to_default_content()
        self.driver.find_element(by=By.CSS_SELECTOR, value=OR_Yes_button_CSS).click()

    def complete(self, tin):
        self.search(tin, status='approve')
        self.process_button()
        self.driver.implicitly_wait(time_to_wait=10)
        time.sleep(3)
        # 修改iframe
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame(iframe_element)
        self.driver.switch_to_frame(iframe_reg_req_app)
        self.driver.find_element(by=By.ID, value=OR_Complete_button).click()
