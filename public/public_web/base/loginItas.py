# -*- coding:UTF-8 -*-
# !/usr/bin/env python3
# _author = liusong time = 2017/9/19 0019

from selenium.webdriver.common.by import By
from public.public_web.base.common_function import is_element_exist
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located
from selenium.webdriver.support.wait import WebDriverWait
from public.public_web.base.globalVariable import *


class Itasbrowser(object):
    def __init__(self, itas_browser_driver):
        self.itas_browser_driver = itas_browser_driver

    def login_itas(self, username_01, password_01):
        def first_login():
            try:
                self.itas_browser_driver.maximize_window()
                self.itas_browser_driver.get(url=url)
                self.itas_browser_driver.find_element_by_id(id_='username').send_keys(username_01)
                self.itas_browser_driver.find_element_by_id(id_='password').send_keys(password_01)
                self.itas_browser_driver.find_element_by_class_name(name='sign_btn').click()
                locator = (By.XPATH, "//*[contains(text(), " + username + ")]")
                license_alert_is_exist = is_element_exist(driver=self.itas_browser_driver, by='id', element='licenseWin')
                if license_alert_is_exist is True:
                    self.itas_browser_driver.find_element_by_id(id_='msgCheck').click()
                    self.itas_browser_driver.find_element_by_id(id_='licenseWin').\
                        find_element_by_tag_name(name='button').click()
                WebDriverWait(
                    self.itas_browser_driver, timeout=10, poll_frequency=0.5).until(
                    presence_of_all_elements_located(locator=locator))
            except Exception as err:
                print(err)
                first_login()
        return first_login()

    def logout_itas(self):
        self.itas_browser_driver.switch_to_default_content()
        self.itas_browser_driver.find_element(by=By.ID, value='abc').click()
        self.itas_browser_driver.find_element(by=By.CSS_SELECTOR, value='a[href="javascript:getlogout();"]').click()
        self.itas_browser_driver.switch_to_default_content()
        self.itas_browser_driver.implicitly_wait(10)
        self.itas_browser_driver.find_element(by=By.CSS_SELECTOR, value='button.btn.btn-primary.save.ax-save').click()

    def logout_browser(self):
        self.itas_browser_driver.quit()
