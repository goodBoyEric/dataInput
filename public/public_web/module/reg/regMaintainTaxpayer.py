# -*- coding:UTF-8 -*-
# !/usr/bin/env python3
# _author = liusong time = 2017/12/6 0006

import time
from public.public_web.base.common_function import attachment_click_function
from selenium.webdriver.common.by import By
from random import Random
from selenium.webdriver.support.select import Select
from public.public_web.base.globalVariable import *
from public.public_web.base.globalVariable import common_url
from public.public_web.base.common_function import write_file
from public.public_web.elements_inputdata.reg.RegMaintainTaxpayer.element.element_maintain_taxpayer_search import *
from public.public_web.elements_inputdata.reg.RegMaintainTaxpayer.element.element_contact_information import *
from public.public_web.elements_inputdata.reg.RegMaintainTaxpayer.element.element_modify_other_information import *


class REGMaintainTaxpayer:
    def __init__(self, driver):
        # 公共元素定位
        self.driver = driver
        self.dict_modify_other_information = {}
        self.sleep_time = self.driver.implicitly_wait(time_to_wait=10)
        self.URL_REGMaintain_taxpayer = common_url + menu_id_search_reg_main

    def maintain_taxpayer_search_screen(self, file_address, taxpayer_name='', **manage_tax_or_taxpayer_no):
        self.driver.get(url=self.URL_REGMaintain_taxpayer)
        self.driver.implicitly_wait(time_to_wait=10)
        self.driver.switch_to_frame(iframe_element)
        if taxpayer_name is None:
            raise AttributeError('function:maintain_taxpayer_search_screen, taxpayer name is None')
        if taxpayer_name != '':
            print(taxpayer_name)
            self.driver.find_element(by=By.ID, value=maintain_taxpayer_search_taxpayer_name).send_keys(taxpayer_name)
        else:
            print(taxpayer_name)
            raise AttributeError('taxpayer_name存在错误')
        self.driver.find_element(by=By.ID, value=maintain_taxpayer_search_button_search).click()
        time.sleep(2)
        maintain_taxpayer_get_tin = self.driver.find_element(by=By.CSS_SELECTOR,
                                                             value=CSS_maintain_taxpayer_get_tin).text
        print(maintain_taxpayer_get_tin)
        write_file(file_address=file_address, **{'TIN': maintain_taxpayer_get_tin})
        self.driver.find_element(by=By.CSS_SELECTOR, value=maintain_taxpayer_search_data).click()
        if len(manage_tax_or_taxpayer_no) != 1:
            raise AttributeError('manage_tax_or_taxpayer_no存在错误')
        else:
            for taxpayer_tax, taxpayer_tax_no in manage_tax_or_taxpayer_no.items():
                if taxpayer_tax == 'taxpayer':
                    taxpayer_tax_element = maintain_taxpayer_search_button_managerTaxpayer
                    if taxpayer_tax_no == 1:
                        taxpayer_tax_menu_element = maintain_taxpayer_search_button_modify_contact
                    elif taxpayer_tax_no == 2:
                        taxpayer_tax_menu_element = maintain_taxpayer_search_button_modify_others
                    elif taxpayer_tax_no == 3:
                        taxpayer_tax_menu_element = maintain_taxpayer_search_button_deregister
                    else:
                        taxpayer_tax_menu_element = maintain_taxpayer_search_button_taxpayer_transfer
                else:
                    taxpayer_tax_element = maintain_taxpayer_search_button_managerTaxType
                    if taxpayer_tax_no == 1:
                        taxpayer_tax_menu_element = maintain_taxpayer_search_button_tax_register
                    elif taxpayer_tax_no == 2:
                        taxpayer_tax_menu_element = maintain_taxpayer_search_button_tax_suspend
                    elif taxpayer_tax_no == 3:
                        taxpayer_tax_menu_element = maintain_taxpayer_search_button_tax_reactive
                    elif taxpayer_tax_no == 4:
                        taxpayer_tax_menu_element = maintain_taxpayer_search_button_tax_deregister
                    else:
                        taxpayer_tax_menu_element = maintain_taxpayer_search_button_tax_modify_vat

                self.driver.find_element(by=By.ID, value=taxpayer_tax_element).click()
                self.driver.implicitly_wait(10)
                self.driver.find_element(by=By.ID, value=taxpayer_tax_menu_element).click()

    def contact_information(self):
        time.sleep(3)
        data_list = []
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame(iframe_element)
        self.driver.switch_to_frame(iframe_reg_req_app)

        # 清除原始数据
        self.driver.find_element(by=By.ID, value=Primary_Telephone_Second).clear()
        self.driver.find_element(by=By.ID, value=Primary_Telephone_Last).clear()
        self.driver.find_element(by=By.ID, value=Other_Telephone_Second).clear()
        self.driver.find_element(by=By.ID, value=Other_Telephone_Last).clear()
        self.driver.find_element(by=By.ID, value=Email_Address).clear()
        self.driver.find_element(by=By.ID, value=Fax_Fax2Email_Second).clear()
        self.driver.find_element(by=By.ID, value=Fax_Fax2Email_Last).clear()
        self.driver.find_element(by=By.ID, value=Cellphone_Second).clear()
        for i in range(6):
            data_list.append(RandomData().itas_random_int_four)
        data_list.append(RandomData().itas_random_int_eleven)
        data_list.append(str(RandomData().itas_random_int_nine) + '@ca-css.com')
        # 填写新数据
        self.driver.find_element(by=By.ID, value=Primary_Telephone_Second).send_keys(data_list[0])
        self.driver.find_element(by=By.ID, value=Primary_Telephone_Last).send_keys(data_list[1])
        self.driver.find_element(by=By.ID, value=Other_Telephone_Second).send_keys(data_list[2])
        self.driver.find_element(by=By.ID, value=Other_Telephone_Last).send_keys(data_list[3])
        self.driver.find_element(by=By.ID, value=Email_Address).send_keys(data_list[7])
        self.driver.find_element(by=By.ID, value=Fax_Fax2Email_Second).send_keys(data_list[4])
        self.driver.find_element(by=By.ID, value=Fax_Fax2Email_Last).send_keys(data_list[5])
        self.driver.find_element(by=By.ID, value=Cellphone_Second).send_keys(data_list[6])
        print(data_list)
        # Attachment
        attachment_click_function(driver=self.driver, direct_element=Contact_Information_Attachment_CSS, *[])

        # confirm button
        self.driver.find_element(by=By.ID, value=Contact_Information_Confirm_Button).click()
        self.driver.switch_to_default_content()
        self.driver.find_element(by=By.CSS_SELECTOR, value=Contact_Information_Yes_Button).click()
        return data_list

    def modify_other_information(self):
        time.sleep(2)
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame(iframe_element)
        self.driver.switch_to_frame(iframe_reg_req_app)

        # Submission Source
        # self.dict_modify_other_information['moi_submission_source_no'] = Random().randint(a=1, b=3)
        Select(self.driver.find_element(by=By.ID, value=MOI_Submission_Source)).select_by_index(1)

        # reason
        self.dict_modify_other_information['moi_modification_reason'] = RandomData().itas_random_char_nine
        self.driver.find_element(by=By.ID, value=MOI_Modification_Reason).\
            send_keys(self.dict_modify_other_information['moi_modification_reason'])

        # 修改Magisterial District
        self.driver.find_element(by=By.ID, value=MOI_Magisterial_District).click()
        self.driver.find_element(by=By.CSS_SELECTOR, value=MOI_Magisterial_District_CSS).click()
        magisterial_district_edit_data = self.driver.find_element\
            (by=By.CSS_SELECTOR, value=MOI_Magisterial_District_Data_CSS).text
        self.dict_modify_other_information['MOI_Magisterial_District_Actual_Data'] = magisterial_district_edit_data

        # attachment
        attachment_click_function(driver=self.driver, direct_element=MOI_Attachment_CSS, *())

        print(self.dict_modify_other_information)
        # submit button
        boi_current_handle = self.driver.current_window_handle
        self.driver.find_element(by=By.ID, value=MOI_Submit_button).click()
        self.driver.switch_to_default_content()
        self.driver.find_element(by=By.CSS_SELECTOR, value=MOI_Submit_yes_button_CSS).click()
        self.driver.get_window_position(boi_current_handle)

        return self.dict_modify_other_information
