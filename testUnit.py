# -*- coding:UTF-8 -*-
# !/usr/bin/env python3
# _author = liusong time = 2017/11/7 0007
import ddt
import unittest
from public.public_web.base.loginItas import Itasbrowser
from public.public_web.module.ret.retReturn import *
from public.public_web.base.verificationMethod import *
from public.public_web.module.ret.retBatch import RETBatch
from public.public_web.base.common_function import read_file, write_file
from public.public_web.module.reg.regMaintainTaxpayer import REGMaintainTaxpayer
from public.public_web.module.reg.regRegistrationRequest import REGRegistrationRequest
from public.public_web.module.reg.regOperationRequest import REGOperationRequest
from public.public_web.module.ppr.ppr_office import PPROffice
from public.public_web.module.ppr.ppt_till import PPRTill
from public.public_web.module.ppr.ppr_capture_payment import PPRCapturePayment
from public.public_web.module.tac.tacJournal import TACJournal


@ddt.ddt
class Test001REGRegistrationRequest(unittest.TestCase):
    def setUp(self):
        self.driver = browser_driver
        self.aaa = REGRegistrationRequest(self.driver)
        self.bbb = SearchPublicFunction(self.driver)
        self.start_browser = Itasbrowser(itas_browser_driver=self.driver)
        self.start_browser.login_itas(username_01=username, password_01=password)

    # # Capture 单元测试 # #
    @ddt.data([13, '89199741-1cfb-477f-9fe9-2b52e34940a8', 2, temporaryFile_web_01])
    @ddt.unpack
    def test_001_registration_request_search_capture(self, taxpayer_type, target_id, col_or_selector, file_address):
        print(2, file_address)
        # 进入capture界面
        self.aaa.registration_request_search_new()
        # 填写相关信息&提交
        taxpayer_name = self.aaa.registration_request_search_capture(taxpayer_type)
        # 将taxpayer name进行存储，以便approve&complete操作
        write_file(file_address=file_address, **{'taxpayer_name': taxpayer_name})
        self.driver.implicitly_wait(time_to_wait=10)
        # search界面填写纳税人name，以此验证是否提交成功。
        assert_taxpayer_name = self.bbb.search_verification(url=common_url + target_id,
                                                            col_or_selector=col_or_selector,
                                                            **{"ID": {"creg08Applicant": taxpayer_name}})
        # 验证提交纳税人姓名与实际查找的是否提交成功及一致
        self.assertEqual(taxpayer_name, assert_taxpayer_name)

    # # Approve 单元测试 # #
    @ddt.data([temporaryFile_web_01])
    @ddt.unpack
    def test_002_registration_request_search_approve(self, file_address):
        # print(1, file_address)
        search_input_data = read_file(read_data='taxpayer_name', file_address=file_address)
        self.aaa.registration_request_search_process(**{'creg08Applicant': search_input_data})
        self.aaa.registration_request_search_approve()

    # # Complete 单元测试 # #
    @ddt.data([temporaryFile_web_01])
    @ddt.unpack
    def test_003_registration_request_search_complete(self, file_address):
        search_input_data = read_file(read_data='taxpayer_name', file_address=file_address)
        self.aaa.registration_request_search_process(**{'creg08Applicant': search_input_data})
        self.aaa.registration_request_search_complete()


@ddt.ddt
class Test002REGMaintainTaxpayer(unittest.TestCase):
    def setUp(self):
        self.driver = browser_driver
        self.start_browser = Itasbrowser(itas_browser_driver=self.driver)
        self.start_browser.login_itas(username_01=username, password_01=password)
        self.ccc = REGMaintainTaxpayer(self.driver)
        self.ddd = REGOperationRequest(self.driver)

    @ddt.data([temporaryFile_web_01])
    @ddt.unpack
    def test_001_contact_information(self, file_address):
        # 读取Taxpayer Name
        taxpayer_name = read_file('taxpayer_name', file_address=file_address)
        # 进行相关操作
        self.ccc.maintain_taxpayer_search_screen(file_address=file_address,
                                                 taxpayer_name=taxpayer_name, **{'taxpayer': 1})
        # 进行修改
        edit_data = self.ccc.contact_information()
        # 验证是否真正修改成功
        self.ccc.maintain_taxpayer_search_screen(file_address=file_address,
                                                 taxpayer_name=taxpayer_name, **{'taxpayer': 1})
        actual_data = contact_information_verification(self.driver)
        print(1, actual_data, '\n', 2, edit_data)
        self.assertEqual(actual_data, edit_data)

    @ddt.data([temporaryFile_web_01])
    @ddt.unpack
    def test_002_modify_other_information(self, file_address):
        # 读取Taxpayer Name
        taxpayer_name = read_file('taxpayer_name', file_address=file_address)
        tin = read_file('TIN', file_address=file_address)
        # 进行相关操作
        self.ccc.maintain_taxpayer_search_screen(file_address=file_address,
                                                 taxpayer_name=taxpayer_name, **{'taxpayer': 2})
        # modify_other_information
        self.ccc.modify_other_information()
        # Operation Request---search
        self.ddd.approve(tin)
        self.ddd.complete(tin)


@ddt.ddt
class Test003RETReturn(unittest.TestCase):
    def setUp(self):
        self.driver = browser_driver
        self.start_browser = Itasbrowser(itas_browser_driver=self.driver)
        self.start_browser.login_itas(username_01=username, password_01=password)
        self.ee = RETReturn(self.driver)
        self.ff = RETBatch(self.driver)

    @ddt.data([temporaryFile_web_01])
    @ddt.unpack
    def test_001_return_search_screen(self, file_address):
        # 读取TIN
        tin = read_file('TIN', file_address=file_address)
        # 提交Return
        self.ee.return_search_screen(tin=tin)
        self.ee.return_process_screen()
        # 获取Return ID&写入到临时文件
        return_id = self.ee.get_return_id(tin=tin)
        write_file(file_address=file_address, **{'return_id':return_id})
        # Send Batch
        self.ff.batch_search_screen(return_id=return_id)
        return_number_of_return = self.ff.batch_send_batch()
        # Accept Batch
        self.ff.batch_search_screen(return_id=return_id)
        self.ff.batch_accept(number_of_return=return_number_of_return)
        # Allocate Batch
        self.ff.batch_search_screen(return_id=return_id)
        self.ff.batch_allocate()
        # Capture Return
        self.ee.return_search_screen(tin=tin,return_status='RCV')
        self.ee.capture_vat_return()
        # 读取数据
        assessment_amount = return_post_verification\
            (driver=self.driver, url=common_url+menu_id_search_tac_transaction, tin=tin, tax_type=1)
        write_file(file_address=file_address,**{'VAT': float(assessment_amount)})
        self.assertEqual(150,int(assessment_amount))


@ddt.ddt
class Test004PPROffice(unittest.TestCase):
    def setUp(self):
        self.driver = browser_driver
        self.start_browser = Itasbrowser(itas_browser_driver=self.driver)
        self.start_browser.login_itas(username_01=username, password_01=password)
        self.gg = PPROffice(driver=self.driver, **database)
        self.hh = PPRTill(self.driver)
        self.jj = PPRCapturePayment(self.driver)

    def test001_open_office(self):
        self.gg.open_office(Local_Time)

    @ddt.data([temporaryFile_web_01])
    @ddt.unpack
    def test002_allocate_till(self, file_address):
        # 读取tin
        tin = read_file('TIN', file_address=file_address)
        # 创建till
        self.hh.till_search()
        till_no = self.hh.till_new(tin=tin)
        write_file(file_address, **{'till_no':till_no})
        # 分配till
        self.hh.till_search(till=till_no)
        self.hh.till_prepare()
        # Open till
        self.hh.till_search(till=till_no)
        self.hh.till_open()

    @ddt.data([temporaryFile_web_01])
    @ddt.unpack
    def test003_capture_payment(self, file_address):
        tin = read_file('TIN',file_address)
        capture_payment_total_amount = self.jj.capture_payment(tin)
        write_file(file_address, **{'capture_payment_total_amount':capture_payment_total_amount})

    @ddt.data([temporaryFile_web_01])
    @ddt.unpack
    def test004_close_reconcile_till(self, file_address):
        # 读取till no.
        till_no = read_file('till_no', file_address)
        capture_payment_total_amount = read_file('capture_payment_total_amount', file_address)

        # close till
        self.hh.till_search(till=till_no)
        self.hh.till_close(capture_payment_total_amount)

        # reconcile till
        self.hh.till_search(till=till_no)
        self.hh.till_reconcile()

class Test005TACJournal(unittest.TestCase):
    def setUp(self):
        self.driver = browser_driver
        self.start_browser = Itasbrowser(itas_browser_driver=self.driver)
        self.start_browser.login_itas(username_01=username, password_01=password)
        self.ii = TACJournal(self.driver)

    def test001_MAJ_AR(self):
        pass



if __name__ == "__main__":
    # ITAS_suite = unittest.TestSuite()
    # ITAS_suite.addTest(unittest.defaultTestLoader.loadTestsFromName(TestREGRegistrationRequest))
    unittest.main()
