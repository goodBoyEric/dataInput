# -*- coding:UTF-8 -*-
# !/usr/bin/env python3
# _author=liusong time= 2017/9/5 0005

from public.public_api.newLogger import logger


class TemFile(object):
    def __init__(self, file_address):
        self.file_address = file_address

    def create_tem_function(self):
        logger.debug(self.file_address)
        create_tem = open(self.file_address, 'w+')
        create_tem.close()

    def read_tem_function(self):
        read_tem = open(self.file_address, 'r')
        read_tem_data = eval(read_tem.read())
        read_tem.close()
        return read_tem_data

    def write_tem_funciton(self, data):
        if not isinstance(data, str):
            # print(data)
            data = str(data)
        write_tem = open(self.file_address, 'w+')
        write_tem.write(data)
        write_tem.close()

    def read_and_write(self, **write_data):
        # 读取文件中的数据
        read_tem = open(self.file_address, 'r+')
        read_tem_data = read_tem.read()
        read_tem.close()

        # 清空数据
        # readTem = open(self.fileAddress , 'r+')
        # readTem.truncate()
        # readTem.close()

        # 清空文件的数据&重新打开
        read_tem_1 = open(self.file_address, 'r+')

        # 对读取数据进行类型转换
        if read_tem_data != str():
            read_tem_data = eval(read_tem_data)
        else:
            read_tem_data = dict(read_tem_data)
        # 将新数据添加到已存文件中
        for key, value in write_data.items():
            read_tem_data[key] = value
        read_tem_1.write(str(read_tem_data))
        read_tem_1.close()

    def find_tem_function(self, *data, **post_data):
        logger.debug('findTemFunction函数，data：%s ，Post data：%s' % (str(data), str(post_data)))
        try:
            if data == ():
                post_data = post_data
                find_data_dict = data
            else:
                read_tem = open(self.file_address, 'r')
                # print(self.fileAddress)
                read_tem_data = eval(read_tem.read())
                find_data_dict = dict()
                for i in data:
                    post_data[i] = read_tem_data[i]
                    find_data_dict[i] = read_tem_data[i]
                    read_tem.close()
            return post_data, find_data_dict
        except Exception as err:
            logger.error('findTemFunction:', err)
