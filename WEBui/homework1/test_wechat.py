# -*- coding: utf-8 -*-
# @Time  :2020/11/7 5:55 下午
# @Author : caohe
# @File :test_wechat.py


'''
使用 cookie 登录企业微信，完成添加联系人，加上断言验证
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import pytest


class Testcase:
    def setup(self):
        # 复用浏览器1-3行pycharm设置
        option = Options()
        #option.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome()
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        self.driver.implicitly_wait(10)

    def test_case1(self):
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688853467184768'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'C7iCWS3f3zDGIL27RDTG4LqQSDsOyJ3CfLEcCrMPaScqSZGnAsx4vBH-GdxQ7zn02T4qCLBWTr6vpZO5Nzj-oM_UvS1W_rojOQrbfnDpxO_Q3k-3TF5BepVP_CWdu0JqPQAJUE7JA-KAYcZ3MAwqTz6TZZyf09QWp7k5hPGe7sgzFxKKGY8u0mUxDdpS_8b9wWVx9pRx4YQjTS5SpTc2fAdkg7r2vA4klGQpYFXvLD6FQDUCrYJ-1RuD-H8Vul0oY3PGy_JcGqeVoGd3MGzLEQ'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688853467184768'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325101179281'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'mvcYEzNBrJ3HCplGrQFtvWPLKAuu5jyxlsIQ2iI5gjgTrkaDjKgRuaKFuuZPgycH'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a2936803'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1604774311, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '5mjndv3'},
            {'domain': '.qq.com', 'expiry': 1604832071, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.848934998.1604742786'},
            {'domain': '.qq.com', 'expiry': 1667817671, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.1027902669.1604742786'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1636278775, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
             'value': '7c52ad33478032d6bcfd6a31981a571ac81941761a5785ffd8f192369e1c1744'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1636280906, 'httpOnly': False,
                             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
                             'value': '1604743207,1604743240,1604743262,1604744907'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
             'value': 'qKKttnzSS7'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1607338787, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
             'path': '/', 'secure': False, 'value': '1604744907'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '32205548631706142'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
             'secure': False, 'value': '7902091264'}]
        # 获取当前的cookie
        #cookies = self.driver.get_cookies()
        #print(cookies)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        tianjia=self.driver.find_element_by_xpath('//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]/div/span[2]')
        tianjia.click()
        username=self.driver.find_element_by_xpath('//*[@id="js_contacts74"]/div/div[2]/div/div[4]/div/form/div[2]/div[1]/div[1]/div[2]/div[1]/div')
        username.send_keys("chhh")
        phonenumber=self.driver.find_element_by_xpath('memberAdd_phone')
        phonenumber.send_keys("13800100100")
        account=self.driver.find_element_by_id("memberAdd_acctid")
        account.send_keys("chhhhh")
        save=self.driver.find_element_by_xpath('//*[@id="js_contacts74"]/div/div[2]/div/div[4]/div/form/div[3]/a[2]')
        save.click()