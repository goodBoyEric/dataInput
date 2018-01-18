# -*- coding:UTF-8 -*-
# !/usr/bin/env python3
# _author = liusong time = 2018/1/16
from selenium.webdriver.common.by import By
from public.public_web.base.globalVariable import *
from public.public_web.base.newRandom import *
from selenium.webdriver.support.select import Select
from public.public_web.elements_inputdata.ppr.element.element_ppr_till import *


class PPRTill:
    def __init__(self, driver):
        self.driver = driver
        self.URL_PPRTill = common_url + menu_id_search_ppr_till

    def till_search(self, till=''):
        self.driver.get(self.URL_PPRTill)
        time.sleep(2)
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame(iframe_element)
        if till != '':
            self.driver.find_element(by=By.ID, value=PPR_Till_Search_No).send_keys(till)
            self.driver.find_element(by=By.ID, value=PPR_Till_Search_button).click()
            time.sleep(2)
            self.driver.find_element(by=By.CSS_SELECTOR, value=PPR_Till_Data_Line_CSS).click()

    def till_new(self, tin):
        self.driver.find_element(by=By.ID, value=PPR_Till_New_button).click()

        # till new screen
        time.sleep(3)
        till_no = str(tin) + '000' + str(RandomData().itas_random_int_four)
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame(iframe_element)
        self.driver.switch_to_frame(iframe_reg_req_app)
        self.driver.find_element(by=By.ID, value=PPR_Till_New_No).send_keys(till_no)
        self.driver.find_element(by=By.ID, value=PPR_Till_New_Name).send_keys(tin)
        self.driver.implicitly_wait(10)
        # submit new till
        self.driver.find_element(by=By.ID, value=PPR_Till_New_Submit_button).click()
        time.sleep(2)
        return till_no

    def till_prepare(self):
        self.driver.find_element(by=By.ID, value=PPR_Till_Prepare_button).click()

        # Prepare till
        time.sleep(2)
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame(iframe_element)
        self.driver.switch_to_frame(iframe_reg_req_app)
        Select(self.driver.find_element(by=By.ID, value=PPR_Till_Prepare_Allocate_To)).\
            select_by_visible_text(PPR_Till_Prepare_Cashier)
        #
        # # Revenue Stamps&Penalty Stamps
        # for i in PPR_Till_Revenue_Stamps_List:
        #     self.driver.find_element(by=By.ID, value=i).clear()
        #     self.driver.find_element(by=By.ID, value=i).send_keys(0)
        # for j in PPR_Till_Penalty_Stamps_List:
        #     self.driver.find_element(by=By.ID, value=j).clear()
        #     self.driver.find_element(by=By.ID, value=j).send_keys(0)
        time.sleep(1)
        self.driver.find_element(by=By.ID, value=PPR_Till_Prepare_Allocate_button).click()
        time.sleep(3)

    def till_open(self):
        self.driver.find_element(by=By.ID, value=PPR_Till_Open_button).click()

        # Open till
        time.sleep(2)
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame(iframe_element)
        self.driver.switch_to_frame(iframe_reg_req_app)

        # Revenue Stamps&Penalty Stamps
        for i in PPR_Till_Revenue_Stamps_List:
            self.driver.find_element(by=By.ID, value=i).send_keys(0)
        for j in PPR_Till_Penalty_Stamps_List:
            self.driver.find_element(by=By.ID, value=j).send_keys(0)
        time.sleep(1)
        self.driver.find_element(by=By.ID, value=PPR_Till_Open_button).click()
        time.sleep(3)

    def till_close(self, capture_payment_total_amount):
        self.driver.find_element(by=By.ID, value=PPR_Office_Close_button).click()

        # Close Till
        time.sleep(2)
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame(iframe_element)
        self.driver.switch_to_frame(iframe_reg_req_app)
        self.driver.find_element(by=By.ID, value=PPR_Till_Close_Cash_Total_Amount).clear()
        self.driver.find_element(by=By.ID, value=PPR_Till_Close_Cash_Total_Amount).\
            send_keys(capture_payment_total_amount)
        self.driver.find_element(by=By.ID, value=PPR_Office_Close_button).click()
        time.sleep(3)

    def till_reconcile(self):
        self.driver.find_element(by=By.ID, value=PPR_Office_Reconcile_button).click()

        # Close Till
        time.sleep(2)
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame(iframe_element)
        self.driver.switch_to_frame(iframe_reg_req_app)
        self.driver.find_element(by=By.ID, value=PPR_Till_Reconcile_Accept_button).click()
        self.driver.find_element(by=By.ID, value=PPR_Office_Reconcile_button).click()
        time.sleep(3)
