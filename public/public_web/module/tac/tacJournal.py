# -*- coding:UTF-8 -*-
# !/usr/bin/env python3
# _author = liusong time = 2018/1/19
from selenium.webdriver.common.by import By
from public.public_web.base.globalVariable import *
from selenium.webdriver.support.select import Select
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

    def capture_miscellaneous_adjustment(self):
        self.__change_default_iframe()

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
