# -*- coding:UTF-8 -*-
# !/usr/bin/env python3
# _author=liusong time= 2017/9/7 0007

import configparser
import logging

from public.public_web.base.globalVariable import logFile, systemConfig


class Logger(object):
    def __init__(self, filename):
        # 对读取的format进行替换（由于%无法在Config中读取）
        self.format = self.format.replace('\\', '%')
        formatter_format = logging.Formatter(fmt=self.format)

        # 控制台控制器
        console_handler = logging.StreamHandler()
        console_handler.setLevel(self.consoleLevel)
        console_handler.setFormatter(formatter_format)

        # 添加文件控制器
        file_handler = logging.FileHandler(logFile, mode='w')
        file_handler.setLevel(self.fileLevel)
        file_handler.setFormatter(formatter_format)

        # 创建logger&将控制器赋值给logger
        self.logger = logging.getLogger(name='ITAS')
        self.logger.setLevel('DEBUG')
        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)
        # print(111111111)

    def logger_function(self):
        return self.logger

    def __new__(cls, filename):
        # 添加属性logConfig&读取Config中的数据
        if not hasattr(cls, 'logConfig'):
            cls.logConfig = super(Logger, cls).__new__(cls)
            open_config_file = configparser.ConfigParser()
            open_config_file.read(filenames=filename)
            cls.logConfig.format = open_config_file.get('logConfig', 'format')
            cls.logConfig.fileLevel = open_config_file.get('logConfig', 'fileLevel')
            cls.logConfig.consoleLevel = open_config_file.get('logConfig', 'consoleLevel')
            # print(cls.logConfig.format)
        return cls.logConfig

logger = Logger(systemConfig).logger_function()
# logger.debug('111111')
# logger.info('222222')
# logger.warning('33333')
# logger.error('444444')
# logger.critical('555555')
