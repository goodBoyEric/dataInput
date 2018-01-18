# -*- coding:UTF-8 -*-
# !/usr/bin/env python3
# _author = liusong time = 2018/1/17
from selenium.webdriver.common.by import By
from public.public_web.base.globalVariable import *
from public.public_web.elements_inputdata.ppr.element.element_ppr_capture_payment import *


class PPRCapturePayment:
    def __init__(self, driver):
        self.driver = driver
        self.URLPPR_capture_payment = common_url + menu_id_search_ppr_payment

    def capture_payment(self, tin):
        self.driver.get(self.URLPPR_capture_payment)
        capture_payment_handle = self.driver.current_window_handle
        time.sleep(3)
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame(iframe_element)
        self.driver.find_element(by=By.ID, value=PPR_Capture_Search_Options).click()
        time.sleep(1)
        self.driver.find_element(by=By.ID, value=PPR_Capture_Search_TIN_Value).send_keys(tin)
        self.driver.find_element(by=By.ID, value=PPR_Capture_Search_button).click()
        time.sleep(1)
        self.driver.find_element(by=By.CSS_SELECTOR, value=PPR_Capture_All_Liability_CheckBox_CSS).click()
        capture_payment_total_amount = self.driver.find_element(
            by=By.ID, value=PPR_Capture_Total_Amount).get_attribute('value')
        self.driver.find_element(by=By.ID, value=PPR_Capture_Receive_Amount).send_keys(capture_payment_total_amount)
        self.driver.find_element(by=By.ID, value=PPR_Capture_Submit_button).click()
        time.sleep(3)
        self.driver.switch_to_window(capture_payment_handle)
        return capture_payment_total_amount

