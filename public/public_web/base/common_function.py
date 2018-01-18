# -*- coding:UTF-8 -*-
# !/usr/bin/env python3
# _author = liusong time = 2017/10/11 0011

from selenium.webdriver.common.by import By


def write_file(file_address, **write_data):
    open_file = open(file=file_address, mode='r')
    all_data = open_file.read()
    print(111,all_data)
    open_file = open(file=file_address,mode='w')
    if all_data is '':
        all_data = dict()
    else:
        all_data = eval(all_data)
    for i, j in write_data.items():
        all_data[i] = j
    print(all_data)
    open_file.write(str(all_data))
    open_file.close()


def read_file(read_data, file_address):
    open_file = open(file=file_address)
    all_data = eval(open_file.read())
    print(read_data)
    response_read_data = all_data[read_data]
    return response_read_data


def attachment_click_function(driver, direct_element, *checkbox):
    attachment_elements = driver.find_elements(
        by=By.CSS_SELECTOR, value=direct_element)
    for i in range(len(attachment_elements)):
        attachment_element = attachment_elements[i]
        i = i + 1
        if i in checkbox or checkbox == ():
            attachment_element_status = attachment_element.is_selected()
            if attachment_element_status is False:
                attachment_element.click()


def is_element_exist(driver, by, element):
    flag = True
    try:
        if by == 'id':
            driver.find_element(by=By.ID,value=element)
        if by == 'css':
            driver.find_element(by=By.CSS_SELECTOR,value=element)
        if by == 'xpath':
            driver.find_element(by=By.XPATH,value=element)
        return flag
    except:
        flag = False
        return flag
