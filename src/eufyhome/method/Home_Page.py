import time

import allure

from src.eufyhome.method.Base_Page import BasePage
from src.config.config import GlobalVar
global Page

"""
app首页
"""


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        if self.platform == GlobalVar.IOS:
            from src.eufyhome.ios.HomeActivity import HomeActivity
        else:
            from src.eufyhome.android.HomeActivity import HomeActivity
        global Page
        Page = HomeActivity()

    def into_help(self):
        """
        点击首页的help按钮
        :return:
        """
        self.tap_element(Page.home_help)
        self.loading()

    def click_add_device(self):
        """
        添加设备
        :return:
        """
        if self.is_exist(Page.add_device):
            self.tap_element(Page.add_device)
        else:
            self.tap_element(Page.null_add_device)
        self.loading()

    def into_system(self):
        """
        进入侧边栏
        :return:
        """
        self.tap_element(Page.menu_icon)

    def is_welcome(self):
        """
        是否显示welcome
        :return:
        """
        return self.wait_exist(Page.welcome, 5)

    def find_username(self, name):
        """
        是否显示用户昵称,模糊匹配
        :param name:
        :return:
        """
        if self.platform == 'ios':
            ele = ('xpath', '//*[@name="{}"]'.format(name))
        else:
            ele = ('xpath', '//*[@text="{}"]'.format(name))
        return self.wait_exist(ele, 5)

    def read_username(self):
        """
        读取用户昵称
        :return:
        """
        return self.get_text(Page.username)

    def into_device_home_page(self, device_name):
        """
        点击设备名称进入主页
        :param device_name:
        :return:
        """
        self.swipe_page('down')
        d_list = self.get_elements(Page.device_name)
        for ele in d_list:
            if device_name in self.get_text(ele):
                self.tap_element(ele)
                return True
        raise Exception('未查找到设备：' + device_name)

    def is_update_tip(self, device):
        """
        显示固件升级标志
        :return:
        """
        if device == 'T2123':
            return self.is_exist(Page.T2123_update)
        elif device == 'T2250':
            return self.is_exist(Page.T2250_update)
        elif device == 'T2190':
            return self.is_exist(Page.T2190_update)

    def read_device_status(self, device_name):
        """
        读取设备状态
        :param device_name:
        :return:
        """
        d_list = self.get_elements(Page.device_name)
        for ele in d_list:
            if device_name in self.get_text(ele):
                _id = d_list.index(ele)
                s_ele = self.get_elements(Page.device_status)[_id]
                return s_ele.text
        raise Exception('未查找到设备：' + device_name)

    def click_device_btn(self, device_name):
        """
        点击设备开关
        :param device:
        :return:
        """
        d_list = self.get_elements(Page.device_name)
        for ele in d_list:
            if device_name in self.get_text(ele):
                _id = d_list.index(ele)
                btn_ele = self.get_elements(Page.device_btn)[_id]
                self.tap_element(btn_ele)
                return
        raise Exception('未找到设备：'+device_name)

    def find_device(self, device_name):
        """
        寻找设别
        :return:
        """
        i = 0
        while i < 2:
            i = i+1
            d_list = self.get_elements(Page.device_name)
            for ele in d_list:
                if device_name in ele.text:
                    return True
        return False

    def find_group(self, group_name):
        """
        寻找分组
        :param group_name:
        :return:
        """
        for group in self.get_elements(Page.group_name):
            if group_name in group.text:
                return True
        return False

    def into_group_page(self, group_name):
        for group in self.get_elements(Page.group_name):
            if group_name in group.text:
                self.tap_element(group)
                return
        raise Exception('未查找到分组：' + group_name)

    def read_group_status(self):
        """
        读取灯组状态
        :return:
        """
        time.sleep(3)
        return self.get_text(Page.bulbs_group_status)

    def click_group_btn(self):
        """
        点击灯组状态
        :return:
        """
        self.click_element(Page.bulbs_group_btn)

    def have_schedule_icon(self, device_name):
        """
        检查设备是否显示定时任务图标
        :param device_name:
        :return:
        """
        schedule_icon = ''
        if self.platform == 'android':
            schedule_icon = '//android.widget.TextView[starts-with(@text,"{}")]/../*[@resource-id="com.eufylife.smarthome:id/schedule_icon"]'.format(device_name)
        if self.platform == 'ios':
            schedule_icon = '//XCUIElementTypeStaticText[@name="{}"]/../XCUIElementTypeButton[@name="home icon schedule"]'.format(device_name)
        return self.wait_exist(('xpath', schedule_icon))

    def have_update_icon(self, device_name):
        """
        检查设备是否显示升级图标
        :param device_name:
        :return:
        """
        update_icon = ''
        if self.platform == 'android':
            update_icon = '//android.widget.TextView[starts-with(@text,"{}")]/../android.widget.ImageView[@resource-id="com.eufylife.smarthome:id/firmware_dot"]'.format(device_name)
        if self.platform == 'ios':
            update_icon = '//XCUIElementTypeStaticText[@name="{}"]/../XCUIElementTypeButton[@name="home icon update"]'.format(device_name)
        return self.wait_exist(('xpath', update_icon))

    def click_schedule_icon(self, device_name):
        """
        点击定时任务图标
        :param device_name:
        :return:
        """
        schedule_icon = ''
        if self.platform == 'android':
            schedule_icon = '//android.widget.TextView[starts-with(@text,"{}")]/../*[@resource-id="com.eufylife.smarthome:id/schedule_icon"]'.format(
                device_name)
        if self.platform == 'ios':
            schedule_icon = '//XCUIElementTypeStaticText[@name="{}"]/../XCUIElementTypeButton[@name="home icon schedule"]'.format(
                device_name)
        self.click_element(('xpath', schedule_icon))
        self.loading()

    def click_update_icon(self, device_name):
        """
        点击升级图标
        :param device_name:
        :return:
        """
        update_icon = ''
        if self.platform == 'android':
            update_icon = '//android.widget.TextView[starts-with(@text,"{}")]/../android.widget.ImageView[@resource-id="com.eufylife.smarthome:id/firmware_dot"]'.format(
                device_name)
        if self.platform == 'ios':
            update_icon = '//XCUIElementTypeStaticText[@name="{}"]/../XCUIElementTypeButton[@name="home icon update"]'.format(
                device_name)
        self.click_element(('xpath', update_icon))
        self.loading()
