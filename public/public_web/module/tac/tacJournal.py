# -*- coding:UTF-8 -*-
# !/usr/bin/env python3
# _author = liusong time = 2018/1/19
from selenium.webdriver.common.by import By
from public.public_web.base.globalVariable import *
from selenium.webdriver.support.select import Select
from public.public_web.base.newRandom import *
from public.public_web.base.common_function import date
from public.public_web.elements_inputdata.tac.element.element_tac_journal import *


class TACJournal:
    def __init__(self, driver):
        self.driver = driver
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
            self.driver.find_element(by=By.ID, value=TAC_Journal_Search_Reallocation_of_Receipt_CSS).click()
        if journal_type == 'MAJ':
            self.driver.find_element(by=By.ID, value=TAC_Journal_Search_Miscellaneous_Adjustment_CSS).click()
        if journal_type == 'TJ':
            self.driver.find_element(by=By.ID, value=TAC_Journal_Search_Transfer_CSS).click()
        if journal_type == 'WOJ':
            self.driver.find_element(by=By.ID, value=TAC_Journal_Search_Write_off_CSS).click()

    def journal_search(self, tin='', journal_category='', journal_status=''):
        self.driver.get(self.URLTacJournal)
        self.__change_default_iframe()
        # 输入journal_category
        if journal_category != '':
            Select(self.driver.find_element(by=By.ID, value=TAC_Journal_Search_Journal_Category)).\
                select_by_value(journal_category)
        # 输入journal_status
        if journal_status != '':
            Select(self.driver.find_element(by=By.ID, value=TAC_Journal_Search_Journal_Status)).\
                select_by_value(journal_category)
        # 输入tin
        if tin != '':
            self.driver.find_element(by=By.ID, value=TAC_Journal_Search_TIN).send_keys(tin)
        self.driver.find_element(by=By.ID, value=TAC_Journal_Search_Process_button).click()

    def capture_miscellaneous_adjustment(self, tin, journal_category='', journal_type='', doc_no=''):
        self.__change_default_iframe()
        self.driver.find_element(by=By.ID, value=TAC_Journal_Capture_TIN).send_keys(tin)
        for i in [TAC_Journal_Capture_Submission_Source, TAC_Journal_Capture_Request_by]:
            Select(self.driver.find_element(by=By.ID, value=i)).\
                select_by_index(Random().randint(a=2, b=8))
        self.driver.find_element(by=By.ID, value=TAC_Journal_Capture_Requestor).send_keys(username)
        self.driver.find_element(by=By.ID, value=TAC_Journal_Capture_Journal_Description).\
            send_keys(RandomData().itas_random_char_nine)
        if journal_category == 'MAJ':
            if journal_type == 'AR':
                Select(self.driver.find_element(by=By.ID, value=TAC_Journal_Capture_Journal_Type)).select_by_value('AR')
                self.driver.find_element(by=By.ID,value=TAC_Journal_Capture_Add_button).click()
                time.sleep(2)
                self.driver.find_element(by=By.ID,value=TAC_Journal_Capture_AR_Doc_No_Text).send_keys(doc_no)
                self.driver.find_element(by=By.ID, value=TAC_Journal_Capture_AR_Search_button).click()
                time.sleep(1)
                adjust_receipt_get_payment_date = self.driver.find_element\
                    (by=By.CSS_SELECTOR,value=TAC_Journal_Capture_AR_Table_Data_CSS).text
                edit_date = date(adjust_receipt_get_payment_date)

                time.sleep()
            elif journal_type == 'AA':
                Select(self.driver.find_element(by=By.ID,value=TAC_Journal_Capture_Journal_Type)).select_by_value('AA')
                pass
            elif journal_type == 'RJ':
                Select(self.driver.find_element(by=By.ID, value=TAC_Journal_Capture_Journal_Type)).select_by_value('RJ')
                pass
            elif journal_type == 'BF':
                Select(self.driver.find_element(by=By.ID, value=TAC_Journal_Capture_Journal_Type)).select_by_value('BF')
                pass
            else:pass
        elif journal_category == 'TJ':
            pass
        elif journal_category == 'WOJ':
            pass
        elif journal_category == 'RORJ':
            pass
        else:pass

    def capture_write_off(self):
        self.__change_default_iframe()

    def capture_reallocation_of_receipt(self):
        self.__change_default_iframe()

    def capture_transfer(self):
        self.__change_default_iframe()

    def approve_journal(self):
        self.__change_default_iframe()

    def complete_journal(self):
        self.__change_default_iframe()
