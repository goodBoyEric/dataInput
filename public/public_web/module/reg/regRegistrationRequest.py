# -*- coding:UTF-8 -*-
# !/usr/bin/env python3
# _author = liusong time = 2017/9/25 0025

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from public.public_web.base.globalVariable import *
from public.public_web.base.newRandom import RandomData
from public.public_web.base.common_function import attachment_click_function
from public.public_web.elements_inputdata.reg.RegRegistrationRequest.element.element_capture import *
from public.public_web.elements_inputdata.reg.RegRegistrationRequest.element.element_search import *
from public.public_web.elements_inputdata.reg.RegRegistrationRequest.element.element_approve import *
from public.public_web.elements_inputdata.reg.RegRegistrationRequest.element.element_complete import *


class REGRegistrationRequest(object):
    def __init__(self, driver):
        # 公共元素定位
        self.driver = driver
        self.sleep_time = self.driver.implicitly_wait(time_to_wait=10)
        self.URL_REGRegistrationRequest = common_url + menu_id_search_reg_req

    def registration_request_search_process(self, **search_data):
        self.driver.implicitly_wait(time_to_wait=10)
        self.driver.get(url=self.URL_REGRegistrationRequest)
        print(self.URL_REGRegistrationRequest)
        self.driver.implicitly_wait(time_to_wait=10)
        self.driver.switch_to_frame(iframe_element)
        for i, j in search_data.items():
            self.driver.find_element(by=By.ID, value=i).send_keys(j)
        self.driver.find_element(by=By.ID, value=Registration_Request_Search_Button).click()
        time.sleep(2)
        self.driver.find_element(by=By.CSS_SELECTOR, value=first_line_data).click()
        self.driver.find_element(by=By.ID, value=Registration_Request_Process_Button).click()

    def registration_request_search_new(self):
        self.driver.get(url=self.URL_REGRegistrationRequest)
        time.sleep(2)
        self.driver.switch_to_frame(iframe_element)
        self.driver.find_element(by=By.ID, value=Registration_Request_New_Button).click()

    def registration_request_search_capture(self, n):
        self.driver.implicitly_wait(time_to_wait=10)
        first_name = RandomData().itas_random_char_nine
        second_name = RandomData().itas_random_char_nine
        # print('firstname:%s' % first_name)
        # print('secondname:%s' % second_name)
        taxpayer_name = first_name + ' ' + second_name
        self.driver.implicitly_wait(time_to_wait=10)
        # *Submission Source
        select_capture_submission_source = self.driver.find_element(by=By.ID, value=Capture_Submission_Source)
        Select(select_capture_submission_source).select_by_index(3)

        # *Taxpayer Category
        if 10 < n < 20:
            taxpayer_category_no = 1
        elif 20 < n <= 30:
            taxpayer_category_no = 2
        elif 30 < n < 40:
            taxpayer_category_no = 3
        elif 40 < n <= 50:
            taxpayer_category_no = 4
        else:
            raise AttributeError("Taxpayer Category 错误")
        select_taxpayer_category = self.driver.find_element(by=By.ID, value=Taxpayer_Category)
        Select(select_taxpayer_category).select_by_index(taxpayer_category_no)

        # Taxpayer Type
        taxpayer_type_no = None
        if 10 < n <= 20:
            taxpayer_type_no = n - 10 + 1
        elif 20 < n <= 30:
            taxpayer_type_no = n - 20 + 1
        elif 30 < n <= 40:
            taxpayer_type_no = n - 30 + 1
        elif 40 < n <= 50:
            taxpayer_type_no = n - 40 + 1
        self.driver.find_element(by=By.ID, value=Taxpayer_Type_input).click()
        self.driver.find_element(by=By.CSS_SELECTOR, value=Taxpayer_Type_CSS + str(taxpayer_type_no) + ')').click()

        # Magisterial District
        self.driver.find_element(by=By.ID, value=Magisterial_District_input).click()
        self.driver.find_element(by=By.CSS_SELECTOR, value=Magisterial_District_CSS).click()

        # *Activity Sector
        select_activity_sector = self.driver.find_element(by=By.ID, value=Activity_Sector)
        Select(select_activity_sector).select_by_index(2)

        # *Source of Income
        self.driver.find_element(by=By.ID, value=Source_of_Income_input).click()
        self.driver.implicitly_wait(time_to_wait=10)
        self.driver.find_element(by=By.CSS_SELECTOR, value=Source_of_Income_CSS).click()

        # Primary Telephone&Cellphone&Email Address
        self.driver.find_element(by=By.ID, value=Primary_Telephone_first).send_keys(RandomData().itas_random_int_four)
        self.driver.find_element(by=By.ID, value=Primary_Telephone_second).send_keys(RandomData().itas_random_int_four)
        self.driver.find_element(by=By.ID, value=Cellphone).send_keys(RandomData().itas_random_int_nine)
        self.driver.find_element(by=By.ID, value=Email_Address).send_keys(str(RandomData().itas_random_int_nine) +
                                                                          '@ca-css.com')

        # Other Telephone&Fax/Fax2Email
        self.driver.find_element(by=By.ID, value=Other_Telephone_first).send_keys(RandomData().itas_random_int_four)
        self.driver.find_element(by=By.ID, value=Other_Telephone_second).send_keys(RandomData().itas_random_int_four)
        self.driver.find_element(by=By.ID, value=Fax_Fax2Email_first).send_keys(RandomData().itas_random_int_four)
        self.driver.find_element(by=By.ID, value=Fax_Fax2Email_second).send_keys(RandomData().itas_random_int_six)

        # Postal Address
        self.driver.find_element(by=By.ID, value=Postal_Address_OpenButton).click()
        select_postal_address_first = self.driver.find_element(by=By.ID, value=Postal_Address_first)
        Select(select_postal_address_first).select_by_index(1)
        self.driver.find_element(by=By.ID, value=Postal_Address_second).send_keys(RandomData().itas_random_int_six)
        self.driver.find_element(by=By.ID, value=Postal_Suburb_Area).send_keys(RandomData().itas_random_char_six)
        self.driver.find_element(by=By.ID, value=Postal_City_Town).send_keys(RandomData().itas_random_char_six)
        self.driver.find_element(by=By.CSS_SELECTOR, value=Postal_Address_SaveButton_CSS).click()

        # Residential/Business Address
        self.driver.find_element(by=By.ID, value=Residential_Business_Address_OpenButton).click()
        self.driver.find_element(by=By.ID, value=Address_Line).send_keys(RandomData().itas_random_char_nine)
        self.driver.find_element(by=By.ID, value=Residential_Suburb_Area).send_keys(RandomData().itas_random_char_nine)
        self.driver.find_element(by=By.ID, value=Residential_City_Town).send_keys(RandomData().itas_random_char_nine)
        self.driver.find_element(by=By.CSS_SELECTOR, value=Residential_Business_Address_SaveButton).click()

        # individual information
        self.driver.find_element(by=By.ID, value=First_Names).send_keys(first_name)
        self.driver.find_element(by=By.ID, value=Surname).send_keys(second_name)
        while True:
            self.driver.find_element(by=By.ID, value=Date_of_Birth).clear()
            self.driver.find_element(by=By.ID, value=Date_of_Birth).send_keys('10-10-1980')
            data_of_brith_data_js = 'return document.getElementById("' + Date_of_Birth + '").value'
            print(data_of_brith_data_js)
            data_of_brith_data = self.driver.execute_script(data_of_brith_data_js)
            print(11, data_of_brith_data)
            if data_of_brith_data == '10-10-1980':
                break
        select_id_type = self.driver.find_element(by=By.ID, value=ID_Type)
        Select(select_id_type).select_by_index(1)
        self.driver.find_element(by=By.ID, value=ID_Number).send_keys(RandomData().itas_random_int_eleven)
        # self.driver.find_element(by=By.ID, value=Gender_Male).send_keys()
        # self.driver.find_element(by=By.ID, value=Gender_Female).send_keys()
        self.driver.find_element(by=By.ID, value=Marital_Status_input).click()
        self.driver.find_element(by=By.CSS_SELECTOR, value=Marital_Status_CSS).click()

        # bank Account
        self.driver.find_element(by=By.CSS_SELECTOR, value=bank_account_tab_CSS).click()
        self.driver.find_element(by=By.ID, value=Bank_account_NewButton).click()
        self.driver.implicitly_wait(time_to_wait=10)
        select_bank_name = self.driver.find_element(by=By.ID, value=Name_of_Bank)
        Select(select_bank_name).select_by_index(2)
        select_branch_name = self.driver.find_element(by=By.ID, value=Branch_Name)
        Select(select_branch_name).select_by_index(2)
        select_type_of_account = self.driver.find_element(by=By.ID, value=Type_of_Account)
        Select(select_type_of_account).select_by_index(3)
        self.driver.find_element(by=By.ID, value=Account_Number).send_keys(RandomData().itas_random_int_nine)

        # Tax Type ITX
        self.driver.find_element(by=By.CSS_SELECTOR, value=tax_type_tab_CSS).click()
        self.driver.implicitly_wait(time_to_wait=10)
        # control_effective_date = self.driver.find_element(by=By.ID, value=Effective_Date)
        self.driver.find_element(by=By.ID, value=Effective_Date).clear()
        self.driver.implicitly_wait(time_to_wait=10)
        effective_date_js = """
        document.getElementById("registeredTaxType[0].creg06EffectiveDate").removeAttribute('readonly')"""
        self.driver.execute_script(effective_date_js)
        self.driver.implicitly_wait(time_to_wait=10)
        # print(currentDay)
        self.driver.find_element(by=By.ID, value=Effective_Date).send_keys(income_tax_effective_date)

        # Tax Type VAT
        self.driver.find_element(by=By.CSS_SELECTOR, value=VAT_Checkbox_CSS).click()
        effective_date_js_vat = """
        document.getElementById("registeredTaxType[1].creg06EffectiveDate").removeAttribute('readonly')"""
        self.driver.implicitly_wait(time_to_wait=10)
        # control_effective_date = self.driver.find_element(by=By.ID, value=Effective_Date)
        self.driver.find_element(by=By.ID, value=VAT_Effective_Date).clear()
        self.driver.implicitly_wait(time_to_wait=10)
        self.driver.execute_script(effective_date_js_vat)
        self.driver.implicitly_wait(time_to_wait=10)
        # print(currentDay)
        self.driver.find_element(by=By.ID, value=VAT_Effective_Date).send_keys(vat_tax_effective_date)
        self.driver.find_element(by=By.ID, value=VAT_Details_button).click()
        time.sleep(1)
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame(iframe_element_vat_details)
        self.driver.find_element(by=By.ID, value=VAT_Estimated_Annual_Taxable_Supplies).\
            send_keys(RandomData().itas_random_int_nine)
        self.driver.switch_to_default_content()
        time.sleep(1)
        self.driver.find_element(by=By.CSS_SELECTOR, value=VAT_Details_Screen_Yes_button).click()

        # Other Business Activity
        self.driver.switch_to_frame(iframe_element)
        self.driver.find_element(by=By.ID, value=Other_Source_of_Income_tab).click()
        self.driver.implicitly_wait(time_to_wait=10)
        self.driver.find_element(by=By.ID, value=Other_Source_of_Income_NewButton).click()
        in_activity_sector_select = self.driver.find_element(by=By.ID, value=IN_Activity_Sector)
        Select(in_activity_sector_select).select_by_index(1)
        in_source_of_income_select = self.driver.find_element(by=By.ID, value=IN_Source_of_Income)
        Select(in_source_of_income_select).select_by_index(1)
        active_inactive_select = self.driver.find_element(by=By.ID, value=Active_Inactive)
        Select(active_inactive_select).select_by_index(1)

        # attachments
        attachment_click_function(driver=self.driver,
                                  direct_element=registration_request_search_capture_attachments, *[])
        # attachment_elements = self.driver.find_elements(
        #     by=By.CSS_SELECTOR, value=registration_request_search_capture_attachments)
        # for attachment_element in attachment_elements:
        #     attachment_element_status = attachment_element.is_selected()
        #     # print(attachment_element_status)
        #     if attachment_element_status is False:
        #         attachment_element.click()

        # submit button
        self.driver.find_element(by=By.ID, value=capture_submit_button).click()
        self.driver.switch_to_default_content()
        self.driver.find_element(by=By.CSS_SELECTOR, value=capture_yes_button_CSS).click()
        print(taxpayer_name)
        time.sleep(3)
        return taxpayer_name

    def registration_request_search_approve(self):
        self.driver.implicitly_wait(time_to_wait=10)
        time.sleep(3)
        # self.driver.switch_to_frame(iframe_element)
        self.driver.switch_to_frame(iframe_reg_req_app)
        self.driver.find_element(by=By.ID, value=registration_request_approve_button).click()
        self.driver.switch_to_default_content()
        self.driver.find_element(by=By.CSS_SELECTOR, value=approve_yes_button_CSS).click()
        time.sleep(3)

    def registration_request_search_complete(self):
        current_window_handle = self.driver.current_window_handle
        self.driver.implicitly_wait(time_to_wait=10)
        time.sleep(3)
        self.driver.switch_to_frame(iframe_reg_req_app)
        self.driver.find_element(by=By.ID, value=registration_request_complete_button).click()
        time.sleep(2)
        self.driver.switch_to_window(current_window_handle)


# if __name__ == "__main__":
#     # 启动浏览器
#     system_driver = browser_driver
#     start_browser = Itasbrowser(itas_browser_driver=system_driver)
#     start_browser.login_itas(username_01=username, password_01=password)
#
#     # capture registration
#     reg_request = REGRegistrationRequest(system_driver)
#     reg_request.registration_request_search_new()
#     reg_request.registration_request_search_capture(n=13)
#
#     # verification capture
#     search_data = {"ID": {"creg08Applicant": "lyj wqqwqw"}}
#     verification_function = SearchPublicFunction(driver=system_driver)
#     response_search_data = verification_function.search_verification(
#         url=common_url + '89199741-1cfb-477f-9fe9-2b52e34940a8',
#         iframe='mainFrame', col_or_selector=2, **search_data)
