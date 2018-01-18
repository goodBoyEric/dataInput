# -*- coding:UTF-8 -*-
# !/usr/bin/env python3
# _author = liusong time = 2018/1/8
import time
from public.public_web.base.globalVariable import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from public.public_web.base.common_function import attachment_click_function
from public.public_web.elements_inputdata.ret.retReturn.element import *
from public.public_web.base.common_function import is_element_exist


class RETReturn:
    def __init__(self, driver):
        self.driver = driver
        self.URL_RETReturn = common_url + menu_id_search_ret_return

    def return_search_screen(self, tin, i=1, return_status=''):
        time.sleep(1)
        self.driver.get(self.URL_RETReturn)
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame(iframe_element)
        self.driver.find_element(by=By.ID, value=Return_TIN).send_keys(tin)
        if return_status != '':
            select_return_status = self.driver.find_element(by=By.ID, value=Return_Status)
            Select(select_return_status).select_by_value(return_status)
        self.driver.find_element(by=By.ID, value=Return_Search_button).click()
        return_search_table_line = Return_Search_Table + str(i) + ')'
        print(return_search_table_line)
        time.sleep(2)
        self.driver.find_element(by=By.CSS_SELECTOR, value=return_search_table_line).click()
        self.driver.find_element(by=By.ID, value=Return_Process_button).click()

    def return_process_screen(self):
        time.sleep(2)
        return_search_screen = self.driver.current_window_handle
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame(iframe_element)
        attachment_click_function(self.driver, direct_element=Return_CheckBox_CSS, *())
        self.driver.find_element(by=By.ID, value=Return_Submit).click()
        time.sleep(2)
        self.driver.switch_to_window(return_search_screen)

    def get_return_id(self, tin):
        self.return_search_screen(tin=tin, return_status='RCV')
        time.sleep(1)
        return_id = self.driver.find_element(by=By.CSS_SELECTOR, value=Return_Search_Table_Return_ID).text
        if return_id is None:
            raise Exception('function:get_return_id ---  return id is none.')
        print(return_id)
        return return_id

    def capture_vat_return(self):
        time.sleep(2)
        self.driver.switch_to_default_content()
        return_search_process_yes_button_is_exist = is_element_exist(
            driver=self.driver, by='css', element=Return_Search_Process_Yes_button_CSS)
        print(return_search_process_yes_button_is_exist)
        if return_search_process_yes_button_is_exist is True:
            self.driver.find_element(by=By.CSS_SELECTOR, value=Return_Search_Process_Yes_button_CSS).click()

        # VAT DECLARED AND VAT CLAIMED
        time.sleep(2)
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame(iframe_element)
        self.driver.find_element(by=By.CSS_SELECTOR, value=Return_VAT_Declared).click()
        time.sleep(2)
        self.driver.find_element(by=By.ID, value=Return_VAT_Trading_15).send_keys(1000)
        self.driver.find_element(by=By.ID, value=Return_VAT_Trading_Total).send_keys(150)
        self.driver.find_element(by=By.ID, value=Return_VAT_Trading_15_Total).send_keys(1000)
        self.driver.find_element(by=By.ID, value=Return_VAT_Trading_Total_ALL).send_keys(150)
        time.sleep(0.5)
        self.driver.find_element(by=By.ID, value=Return_VAT_Submit_button).click()
        time.sleep(3)
