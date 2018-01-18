# coding:utf-8
# !/usr/bin/python3
import xlwt
import xlrd
import time
import xlutils.copy
from copy import deepcopy
from public.public_api.newLogger import logger


class ReadExcel(object):
    def __init__(self, file_name):
        logger.debug('ReadExcel:（%s）' % file_name)
        self.file_name = file_name
        self.D1 = dict()
        self.all_sheet = None

        # 判定filename是否为空或无值
        try:
            if self.file_name is None:
                raise "fileName：%s 不能为空" % file_name
            self.open_excel = xlrd.open_workbook(filename=file_name, formatting_info=True)
        except Exception as err:
            logger.error('ReadExcel初始化，出现错误：%s' % err)

    def get_open_excel(self):
        return self.open_excel

    # 获取所有sheet名称
    def get_sheets(self):
        # 对传入值self.openExcel进行判断
        if not isinstance(self.open_excel, xlrd.book.Book) and self.open_excel is None:
            raise '%s：存在错误' % self.open_excel
        try:
            self.all_sheet = self.open_excel.sheet_names()
        except Exception as err:
            logger.error('函数getSheets，出现错误：%s' % err)
        else:
            logger.debug('class: ReadExcel;function:getSheets. .over')
        return self.all_sheet

    # 获取sheet name与Number的字典
    def get_sheet_name_number(self):
        # 对传入值self.openExcel进行判断
        # print(self.open_excel)
        if not isinstance(self.open_excel, xlrd.book.Book) and self.open_excel is None:
            raise '%s：存在错误' % self.open_excel
        try:
            all_sheet = self.open_excel.sheets()
            for i in all_sheet:
                self.D1[i.name] = i.number
        except Exception as err:
            logger.error('函数出现错误：getSheetNameNumber%s' % err)
        else:
            logger.debug('class: ReadExcel;funciton:getSheets. .over；D1=%s' % self.D1)
        return self.D1


class ReadSheet(ReadExcel):
    def __init__(self, file_name):
        super(ReadSheet, self).__init__(file_name)
        super(ReadSheet, self).get_sheets()
        self.dict_name_rows = dict()
        logger.debug('class:ReadSheet,初始化：%s' % file_name)

    # 获取sheet名称与行数字典
    def get_sheet_rows(self):
        for sheet in self.all_sheet:
            open_sheet = self.open_excel.sheet_by_name(sheet)
            row = open_sheet.nrows
            # print(row)
            self.dict_name_rows[sheet] = row
        logger.debug('获取sheet名称与行数字典，%s' % self.dict_name_rows)
        return self.dict_name_rows


class GetSheetData(ReadExcel):
    def __init__(self, file_name, **sheet_data):
        logger.debug('class:GetSheetData , 初始化filename：%s ，sheet name：%s' % (file_name, sheet_data))
        super(GetSheetData, self).__init__(file_name=file_name)
        self.sheet_name_and_rows = sheet_data

    # 读取行数据的生成器
    def read_sheet_data(self):
        for sheet_name, rows in self.sheet_name_and_rows.items():
            open_sheet = self.open_excel.sheet_by_name(sheet_name)
            for row in range(1, rows):
                data = open_sheet.row_values(rowx=row)
                yield data


class GetSheetDataGenerator(object):
    # 行数据生成器
    def __init__(self, filename, sheet_name):
        self.start_row = 0
        open_excel = xlrd.open_workbook(filename)
        self.open_sheet_name = open_excel.sheet_by_name(sheet_name)
        logger.debug('生成器初始化，filename：%s，sheet name：%s' % (filename, sheet_name))

    def __iter__(self):
        return self

    def __next__(self):
        self.start_row += 1
        self.rows_data = self.open_sheet_name.row_values(rowx=self.start_row)
        logger.debug('生成器返回结果：%s' % self.rows_data)
        return self.rows_data


class ExcelStyle(object):
    def __init__(self):
        # 字体
        excel_font = xlwt.Font()
        excel_font.name = 'Arial'

        # 边框
        excel_borders = xlwt.Borders()
        excel_borders.bottom = excel_borders.left = excel_borders.right = excel_borders.top = 1

        # 对齐方式
        excel_alignment = xlwt.Alignment()
        excel_alignment.horz = xlwt.Alignment.HORZ_LEFT
        excel_alignment.vert = xlwt.Alignment.VERT_TOP
        excel_alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT

        # 样式整合
        excel_style = xlwt.XFStyle()
        excel_style.alignment = excel_alignment
        excel_style.font = excel_font
        excel_style.borders = excel_borders

        # 初始化excel格式
        self.excelBorders = excel_borders
        self.excelFont = excel_font
        self.excelAlignment = excel_alignment
        self.style = excel_style
        logger.debug('完成类:ExcelStyle初始化')

    def excel_font_function(self):
        return self.excelFont

    def excel_borders_function(self):
        return self.excelBorders

    def excel_alignment_function(self):
        return self.excelAlignment

    # style进行背景颜色赋值函数
    def style_function(self, fore_colour=None):
        style = deepcopy(self.style)
        if fore_colour not in ([None, '']):
            patterni = xlwt.Pattern()
            patterni.pattern = 1
            patterni.pattern_fore_colour = fore_colour
            style.pattern = patterni
        logger.debug('完成背景颜色赋值，背景颜色值：%d' % fore_colour)
        return style


class WriteExcel(ReadExcel, ExcelStyle):
    def __init__(self, file_name, till_name):
        ReadExcel.__init__(self, file_name=file_name)
        # super(WriteExcel ,self).__init__(fileName=filename)
        ReadExcel.get_sheet_name_number(self)
        ExcelStyle.__init__(self)
        try:
            self.copyExcel = xlutils.copy.copy(self.open_excel)
            sheet_number = self.D1[till_name]
            self.get_sheet = self.copyExcel.get_sheet(sheetnum=sheet_number)
        except Exception as err:
            logger.error('writeData Function 存在问题：%s' % err)
        logger.debug('类：WriteExcel，完成初始化')

    def write_data(self, row, col, data):
        logger.debug('接收数据，row：%s，col：%s，data：%s' % (row, col, data))
        fore_colour = None
        # 对第8列进行判定，添加背景颜色 红色：2、绿色：3
        if int(col) == 7 and str(data) != str():
            if str(data) == 'Pass':
                fore_colour = 3
            elif str(data) == 'Fail':
                fore_colour = 2
            excel_style = self.style_function(fore_colour=fore_colour)
        else:
            excel_style = self.style

        # 判定写入数据是否为空，为空时不写入
        if str(data) not in (['[]', '{}', '()', None, '']):

            # 判断data类型，若不是str类型进行转换后写入
            if not isinstance(data, str):
                data = str(data)
            self.get_sheet.write(row, col, data, style=excel_style)

        # 若填写数据是一个空字段/元祖/列表，将不想EXCEL写入
        else:
            pass

    def save_copy_excel(self):
        self.copyExcel.save(self.file_name)


class ExcelResultStatistics(ReadSheet, ExcelStyle):
    def __init__(self, file_name, result_address):
        ReadSheet.__init__(self, file_name)
        ExcelStyle.__init__(self)
        self.result_address = result_address
        self.resultName = 'result'
        self.currentTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        try:
            self.excel_workbook = xlwt.Workbook()
            self.add_result_sheet = self.excel_workbook.add_sheet(sheetname=self.resultName, cell_overwrite_ok=True)
            # excelWorkbook.save(self.resultAddress)
        except Exception as err:
            logger.error(err)
        else:
            logger.debug('class:ExcelResultStatistics,初始化完毕')

    def result_excel_initialization(self):
        self.add_result_sheet.write_merge(0, 0, 0, 4, '测试汇总' + self.currentTime, self.style)
        fixed_data_list = ['工作表名称', '通过数量', '失败数量', '总数量', '通过率']
        for i in range(0, 5):
            self.add_result_sheet.write(1, i, fixed_data_list[i], self.style)

    def statistics_function(self, col, start_row):
        self.result_excel_initialization()
        logger.debug('完成统计结果excel初始化')
        for x in range(0, len(self.all_sheet)):
            try:
                open_sheet = self.open_excel.sheet_by_name(self.all_sheet[x])
                pass_or_fail_list = open_sheet.col_values(colx=col, start_rowx=start_row)
                pass_sum = pass_or_fail_list.count('Pass')
                fail_sum = pass_or_fail_list.count('Fail')
                pass_rate = str('%.1f' % ((pass_sum / (pass_sum + fail_sum)) * 100)) + '%'
                sheet_name_statistics_result = [self.all_sheet[x], pass_sum, fail_sum, pass_sum + fail_sum, pass_rate]
                for y in range(0, 5):
                    self.add_result_sheet.write(x + 2, y, sheet_name_statistics_result[y], self.style)
            except Exception as err:
                logger.error(err)
                continue

    def save_result_excel(self):
        self.excel_workbook.save(self.result_address)


# aa = ExcelResultStatistics(filename='E:\\dataInput\\data_excel\\data.xlsx' ,
        # result_address='E:\\dataInput\\data_excel\\result.xlsx')
# aa.statisticsFunction(col=7 , start_row=1)
# aa.save_result_excel()
