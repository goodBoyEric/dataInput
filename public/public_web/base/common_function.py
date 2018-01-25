# -*- coding:UTF-8 -*-
# !/usr/bin/env python3
# _author = liusong time = 2017/10/11 0011
import time
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


def date(current_date):
    day = current_date[:2]
    mouth = current_date[3:5]
    year = current_date[6:]
    if int(day) < 2:
        day = '28'
        if int(mouth) < 2:
            year = str(int(year) - 1)
            mouth = '12'
        else:
            mouth = str(int(mouth) - 1)
            if len(mouth)<2:
                mouth = '0' + mouth
    else:
        day = str(int(day) - 1)
        if len(day) < 2:
            day = '0' + day
    edit_year = str(day) + '-' + mouth + '-' + year
    return edit_year


def judge_date(original_date, compare_date=1):
    if compare_date ==1:
        compare_date = time.strftime('%d-%m-%Y', time.localtime())
    if len(original_date) != 10:
        raise ImportError('original_date 格式不正确')
    #
    original_date_day = original_date[:2]
    original_date_mouth = original_date[3:5]
    original_date_year = original_date[6:]
    compare_date_day = compare_date[:2]
    compare_date_mouth = compare_date[3:5]
    compare_date_year = compare_date[6:]
    if original_date_year < compare_date_year:
        return True
    elif original_date_year == compare_date_year:
        if original_date_mouth < compare_date_mouth:
            return True
        elif original_date_mouth == compare_date_mouth:
            if original_date_day <= compare_date_day:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
