# -*- coding:UTF-8 -*-
# !/usr/bin/env python3
# _author = liusong time = 2018/1/19
from selenium.webdriver.common.by import By
from public.public_web.base.globalVariable import *
from selenium.webdriver.support.select import Select
from public.public_web.base.newRandom import *
from public.public_web.base.common_function import date, amount_change
from public.public_api.oracle import Oracle
from public.public_web.base.common_function import attachment_click_function
from public.public_web.elements_inputdata.tac.element.element_tac_journal import *


class TACJournal:
    def __init__(self, driver, **oracle_link_data):
        self.driver = driver
        self.oracle = Oracle(**oracle_link_data)
        self.URLTacJournal = common_url + menu_id_search_tac_journal

    def __change_default_iframe(self):
        time.sleep(2)
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame(iframe_element)

    def journal_new(self, journal_type):
        self.driver.get(self.URLTacJournal)
        self.__change_default_iframe()
        self.driver.find_element(by=By.ID, value=TAC_Journal_Search_New_button).click()
        time.sleep(1)
        if journal_type == 'RORJ':
            self.driver.find_element(by=By.CSS_SELECTOR, value=TAC_Journal_Search_Reallocation_of_Receipt_CSS).click()
        if journal_type == 'MAJ':
            self.driver.find_element(by=By.CSS_SELECTOR, value=TAC_Journal_Search_Miscellaneous_Adjustment_CSS).click()
        if journal_type == 'TJ':
            self.driver.find_element(by=By.CSS_SELECTOR, value=TAC_Journal_Search_Transfer_CSS).click()
        if journal_type == 'WOJ':
            self.driver.find_element(by=By.CSS_SELECTOR, value=TAC_Journal_Search_Write_off_CSS).click()

    def journal_search_data(self, tin='', journal_category='', journal_status='', journal_type=''):
        self.driver.get(self.URLTacJournal)
        self.__change_default_iframe()
        # 输入journal_category
        if journal_category != '':
            Select(self.driver.find_element(by=By.ID, value=TAC_Journal_Search_Journal_Category)). \
                select_by_value(journal_category)
        # 输入journal_status
        if journal_status != '':
            Select(self.driver.find_element(by=By.ID, value=TAC_Journal_Search_Journal_Status)). \
                select_by_value(journal_status)
        # 输入tin
        if tin != '':
            self.driver.find_element(by=By.ID, value=TAC_Journal_Search_TIN).send_keys(tin)

        # 输入journal type
        if journal_type != '':
            self.driver.find_element(by=By.ID, value=TAC_Journal_Search_Journal_Type).send_keys(journal_type)
        self.driver.find_element(by=By.ID, value=TAC_Journal_Search_Search_button).click()

    def journal_search_doc_no(self, tin='', journal_category='', journal_status='', journal_type='', i=1):
        self.journal_search_data(tin, journal_category, journal_status, journal_type)
        time.sleep(2)
        journal_search_get_data_element = TAC_Journal_Search_Table_First_Line + '>td:nth-child(' + str(i) + ')'
        journal_search_get_data = self.driver.find_element(
            by=By.CSS_SELECTOR, value=journal_search_get_data_element).text
        return journal_search_get_data

    def journal_search(self, tin='', journal_category='', journal_status='', journal_type=''):
        self.journal_search_data(tin, journal_category, journal_status, journal_type)
        time.sleep(2)
        self.driver.find_element(by=By.CSS_SELECTOR, value=TAC_Journal_Search_Table_First_Line).click()
        self.driver.find_element(by=By.ID, value=TAC_Journal_Search_Process_button).click()
        time.sleep(2)

    def capture_miscellaneous_adjustment(self, tin, journal_type='',doc_no1=''):
        self.__change_default_iframe()
        self.driver.switch_to_frame(iframe_reg_req_app)
        self.driver.find_element(by=By.ID, value=TAC_Journal_Capture_TIN).send_keys(tin)
        for i in [TAC_Journal_Capture_Submission_Source, TAC_Journal_Capture_Request_by]:
            Select(self.driver.find_element(by=By.ID, value=i)).\
                select_by_index(Random().randint(a=2, b=8))
        self.driver.find_element(by=By.ID, value=TAC_Journal_Capture_Requestor).send_keys(username)
        self.driver.find_element(by=By.ID, value=TAC_Journal_Capture_Journal_Description).\
            send_keys(RandomData().itas_random_char_nine)
        if journal_type == 'AR':
            Select(self.driver.find_element(by=By.ID, value=TAC_Journal_Capture_Journal_Type)).select_by_value('AR')
            self.driver.find_element(by=By.ID,value=TAC_Journal_Capture_Add_button).click()
            get_vat_doc_no = """select t.ctac03_document_num from ttac03_transaction t
                                inner join treg01_taxpayer a
                                on t.creg01_taxpayer_uid = a.creg01_taxpayer_uid and t.ctac03_cr_dr='Cr'
                                and a.creg01_tin =""" + str(tin)
            doc_no = self.oracle.oracle_sql_execute_function(get_vat_doc_no,response=1)
            time.sleep(2)
            self.driver.find_element(by=By.ID,value=TAC_Journal_Capture_AR_Doc_No_Text).send_keys(doc_no)
            self.driver.find_element(by=By.ID, value=TAC_Journal_Capture_AR_Search_button).click()
            time.sleep(1)
            adjust_receipt_get_payment_date = self.driver.find_element\
                (by=By.CSS_SELECTOR,value=TAC_Journal_Capture_AR_Table_Data_CSS).text
            edit_date = date(adjust_receipt_get_payment_date)
            print(edit_date)
            self.driver.find_element(by=By.CSS_SELECTOR, value=TAC_Journal_Capture_AR_Table_Data_CSS).click()
            self.driver.find_element(by=By.ID, value=TAC_Journal_Capture_AR_Target_Issue_Date).clear()
            self.driver.find_element(by=By.ID, value=TAC_Journal_Capture_AR_Target_Issue_Date).send_keys(edit_date)
            self.driver.find_element(by=By.ID, value=TAC_Journal_Capture_AR_Add_to_Journal_button).click()
            time.sleep(1)
        elif journal_type == 'AA':
            Select(self.driver.find_element(by=By.ID,value=TAC_Journal_Capture_Journal_Type)).select_by_value('AA')
            self.driver.find_element(by=By.ID, value=TAC_Journal_Capture_BF_Add_button).click()
            time.sleep(2)
            self.driver.find_element(by=By.ID, value=TAC_Journal_Capture_RT_Doc_No_NO).click()
            Select(self.driver.find_element(by=By.ID, value=TAC_Journal_Capture_ARA_Tax_Type)).select_by_value('1')
            Select(self.driver.find_element(by=By.ID, value=TAC_Journal_Capture_ARA_Liability_Type)).\
                select_by_value('TAXLB')
            self.driver.find_element(by=By.ID, value=TAC_Journal_Capture_ARA_Tax_Year).clear()
            self.driver.find_element(by=By.ID, value=TAC_Journal_Capture_RT_Search_button).click()
            time.sleep(2)
            original_amount = self.driver.find_element(
                by=By.CSS_SELECTOR, value=TAC_Journal_Capture_ARA_Table_Data_CSS+'10'+')').text
            change_amount = amount_change(original_amount, 5000)
            print(change_amount)
            self.driver.find_element(by=By.ID, value=TAC_Journal_Capture_ARA_Table_Data_Amount).\
                send_keys(str(change_amount))
            self.driver.find_element(by=By.ID, value=TAC_Journal_Capture_AR_Add_to_Journal_button).click()
            time.sleep(1)

        elif journal_type == 'RT':
            Select(self.driver.find_element(by=By.ID, value=TAC_Journal_Capture_Journal_Type)).select_by_value('RJ')
            self.driver.find_element(by=By.ID, value=TAC_Journal_Capture_BF_Add_button).click()
            time.sleep(2)
            self.driver.find_element(by=By.ID, value=TAC_Journal_Capture_RT_Doc_No_Yes).click()
            self.driver.find_element(by=By.ID, value=TAC_Journal_Capture_RT_Doc_No).send_keys(doc_no1)
            self.driver.find_element(by=By.ID, value=TAC_Journal_Capture_RT_Search_button).click()
            time.sleep(2)
            self.driver.find_element(by=By.CSS_SELECTOR, value=TAC_Journal_Capture_RT_CheckAll_CSS).click()
            self.driver.find_element(by=By.ID, value=TAC_Journal_Capture_RT_AddtoJournal_button).click()
            time.sleep(1)

        elif journal_type == 'ABFB':
            time.sleep(1)
            Select(self.driver.find_element(by=By.ID, value=TAC_Journal_Capture_Journal_Type)).select_by_value('BF')
            Select(self.driver.find_element(by=By.ID, value=TAC_Journal_Capture_BF_Tax_Type)).select_by_value('1')
            Select(self.driver.find_element(by=By.ID, value=TAC_Journal_Capture_BF_Liability_Type)).select_by_value('TAXLB')
            self.driver.find_element(by=By.ID, value=TAC_Journal_Capture_BF_Tax_Year).clear()
            self.driver.find_element(by=By.ID, value=TAC_Journal_Capture_BF_Tax_Year).send_keys('2019')
            self.driver.find_element(by=By.ID, value=TAC_Journal_Capture_BF_Liability_Type).click()
            time.sleep(1)
            Select(self.driver.find_element(by=By.ID, value=TAC_Journal_Capture_BF_Tax_Period)).select_by_value('1')
            self.driver.find_element(by=By.ID, value=TAC_Journal_Capture_BF_Amount).send_keys('2019')
            self.driver.find_element(by=By.ID, value=TAC_Journal_Capture_BF_Add_button).click()
        else:
            pass
        attachment_click_function(driver=self.driver,direct_element=TAC_Journal_Capture_attachments, *[])
        self.driver.find_element(by=By.ID, value=TAC_Journal_Capture_Submit_button).click()
        time.sleep(2)

    def capture_write_off(self):
        self.__change_default_iframe()
        self.driver.find_element(by=By.ID,)

    def capture_reallocation_of_receipt(self):
        self.__change_default_iframe()

    def capture_transfer(self):
        self.__change_default_iframe()

    def approve_journal(self):
        self.__change_default_iframe()
        self.driver.switch_to_frame(iframe_reg_req_app)
        self.driver.find_element(by=By.ID, value=TAC_Journal_Capture_Approve_button).click()
        time.sleep(2)
        self.driver.switch_to_default_content()
        self.driver.find_element(by=By.CSS_SELECTOR, value=TAC_Journal_Capture_Approve_Yes_button_CSS).click()

    def send_back_journal(self):
        pass

    def reject_journal(self):
        pass

    def complete_journal(self):
        self.__change_default_iframe()
        self.driver.switch_to_frame(iframe_reg_req_app)
        self.driver.find_element(by=By.ID, value=TAC_Journal_Capture_Complete_button).click()
        time.sleep(2)
