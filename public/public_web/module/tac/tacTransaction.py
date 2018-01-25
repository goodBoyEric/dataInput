# -*- coding:UTF-8 -*-
# !/usr/bin/env python3
# _author = liusong time = 2018/1/23
from public.public_web.base.globalVariable import *
from selenium.webdriver.common.by import By
from public.public_web.elements_inputdata.tac.element.element_tac_transaction import *


class TACTransaction:
    def __init__(self, driver):
        self.driver = driver
        self.URLTACTransaction = common_url + menu_id_search_tac_transaction

    def tac_transaction_search(self, tin,doc_no='', element=''):
        self.driver.find_element(by=By.ID, value=TTransaction_TIN).send_keys(tin)
        if doc_no != '':
            self.driver.find_element(by=By.ID,value=TTransaction_DocNo).send_keys(doc_no)
