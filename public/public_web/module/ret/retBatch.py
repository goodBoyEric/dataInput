# -*- coding:UTF-8 -*-
# !/usr/bin/env python3
# _author = liusong time = 2018/1/9
from public.public_web.base.globalVariable import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from public.public_web.elements_inputdata.ret.retBatch.element import *


class RETBatch():
    def __init__(self, driver):
        self.driver = driver
        self.URL_RETBatch = common_url + menu_id_search_ret_batch

    def batch_search_screen(self, return_id, batch_status_value=''):
        self.driver.get(self.URL_RETBatch)
        self.driver.switch_to_frame(iframe_element)
        self.driver.find_element(by=By.ID, value=Batch_Return_ID).send_keys(return_id)
        if batch_status_value != '':
            select_batch_status = self.driver.find_element(by=By.ID, value=Batch_Status)
            Select(select_batch_status).deselect_by_value(batch_status_value)
        self.driver.find_element(by=By.ID, value=Batch_Search_button).click()
        time.sleep(2)
        self.driver.find_element(by=By.CSS_SELECTOR, value=Batch_Search_Table_Line_CSS).click()
        self.driver.find_element(by=By.ID, value=Batch_Process_button).click()

    def batch_send_batch(self):
        batch_send_screen = self.driver.current_window_handle
        time.sleep(1)
        self.driver.find_element(by=By.ID, value=Batch_Send_Details_button).click()
        time.sleep(1)
        self.driver.switch_to_frame(iframe_reg_req_app)
        batch_all_return = len(self.driver.find_elements(by=By.CSS_SELECTOR, value=Batch_Return_All))
        print(batch_all_return)
        self.driver.find_element(by=By.ID, value=Batch_Send_Print_button).click()
        time.sleep(2)
        self.driver.switch_to_window(batch_send_screen)
        time.sleep(2)
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame(iframe_element)
        self.driver.switch_to_frame(iframe_reg_req_app)
        self.driver.find_element(by=By.ID, value=Batch_Number_Return).send_keys(batch_all_return)
        self.driver.find_element(by=By.ID, value=Batch_Send_Send_button).click()
        return batch_all_return

    def batch_accept(self, number_of_return):
        time.sleep(1)
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame(iframe_element)
        self.driver.find_element(by=By.ID, value=Batch_Number_Return).send_keys(number_of_return)
        self.driver.find_element(by=By.ID, value=Batch_Accept_button).click()

    def batch_allocate(self):
        time.sleep(1)
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame(iframe_element)
        self.driver.find_element(by=By.ID, value=Batch_First_Capture).click()
        self.driver.find_element(by=By.CSS_SELECTOR, value=First_Capture_Name_CSS).click()
        time.sleep(0.5)
        self.driver.find_element(by=By.ID, value=Batch_Allocate_button).click()
