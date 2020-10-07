import os
import time

from src.config.readconfig import data
from src.eufyhome.method.Base_Page import BasePage
from src.config.config import GlobalVar
global Page

"""
扫地机通用设置页面操作
"""


class AddDevicePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        if self.platform == GlobalVar.IOS:
            from src.eufyhome.ios.AddDeviceActivity import AddDeviceActivity
        else:
            from src.eufyhome.android.AddDeviceActivity import AddDeviceActivity
        global Page
        Page = AddDeviceActivity()

    def close(self):
        """
        关闭界面
        :return:
        """
        self.tap_element(Page.close)

    def select_device_by_type(self, desc):
        eles = self.get_elements(Page.device_type)
        for ele in eles:
            if desc in ele.text:
                self.tap_element(ele)
                break
        raise Exception('未找到指定的设备类型：'+desc)

    def click_robotic(self):
        """
        点击扫地机
        :return:
        """
        self.tap_element(Page.robotic)

    def click_bulds(self):
        """
        点击灯泡
        :return:
        """
        self.tap_element(Page.bulds)

    def click_plug(self):
        """
        点击插座
        :return:
        """
        self.tap_element(Page.plug)

    def click_switch(self):
        """
        点击开关
        :return:
        """
        self.tap_element(Page.switch)

    def click_genie(self):
        """
        点击genie开关
        :return:
        """
        self.click_element(Page.genie)
        self.loading()
        self.tap_element(Page.Next_btn)
        time.sleep(2)
        self.tap_element(Page.Next_btn)

    def read_robotic_list(self):
        """
        读取扫地机型号列表
        :return:
        """
        robotic_list = set()
        for i in range(20):
            flag = False
            els = self.get_elements(Page.robotic_type)
            for el in els:
                text = el.text
                if text not in robotic_list:
                    flag = True
                    robotic_list.add(el.text)
            if flag:
                self.swipe_by_element('up', 0.8, 0.3, 0.5, None, 2000)
            else:
                break
        return robotic_list

    def select_robotic(self, type_name):
        """
        选择指定扫地机
        :param type_name:
        :return:
        """
        if self.platform == 'ios':
            ele = ('xpath', '//*[@name="{}"]'.format(type_name))
        else:
            ele = ('xpath', '//*[@text="{}"]'.format(type_name))
        for i in range(10):
            if self.is_exist(ele):
                self.tap_element(ele)
                break
            else:
                self.swipe_by_element('up', 0.8, 0.2, 0.5, None, 3000)

    def read_device_type(self):
        """
        读取设备类型
        :return:
        """
        device_list = set()
        els = self.get_elements(Page.device_type)
        for el in els:
            text = el.text
            if text not in device_list:
                device_list.add(el.text)
        return device_list

    # *********************扫地机添加流程************************ #
    def set_wifi(self, wifi_name, pass_word):
        """
        wifi页面设置
        :return:
        """
        self.send_keys(Page.robovac_wifi_name, wifi_name, 1)
        self.hide_keyboard()
        # self.click_element(Page.robovac_display_pw)
        self.send_keys(Page.robovac_wifi_password, pass_word, 1)
        self.hide_keyboard()
        # self.click_element(Page.save_network)
        self.tap_element(Page.robotic_wifi_next)

        # if self.text_display(wifi_name) is False:
        #     if self.platform == 'ios':
        #         self.click_element(('name', 'adddevice icon arrow down'))  # 展开wifi列表
        #         self.tap_element(('name', wifi_name))
        #     elif self.platform == 'android':
        #         self.click_element(('id', 'com.eufylife.smarthome:id/wifi_checkbox'))
        #         try:
        #             # 点击列表刷新按钮
        #             self.click_element(('id', 'com.eufylife.smarthome:id/wifi_rssi'))
        #         except Exception as e:
        #             print(e)
        #             pass
        #         self.tap_element(('xpath', '//*[@text="{}"]'.format(wifi_name)))
        # self.tap_element(Page.robotic_wifi_next)

    def confirm_status(self):
        """
        确认配网状态
        :return:
        """
        if self.platform == 'ios':
            btns = self.get_elements(Page.robotic_status_confirm)
            for btn in btns:
                text = self.get_text(btn)
                if text is not None and 'Status confirmed' in text:
                    self.click_element(btn)
                    break
            time.sleep(0.5)
            self.click_element(Page.robotic_status_next)
            self.wait_exist(Page.robotic_into_setting)
            # self.tap_element(Page.robotic_into_setting)
        else:
            self.tap_element(Page.robotic_status_confirm)
            self.tap_element(Page.robotic_status_next)

    def select_robotic_by_id(self, udid):
        """
        选择配网设备
        :return:
        """
        if self.platform == 'ios':
            self.activate_app('com.apple.Preferences')  # 打开手机系统设置
            try:
                self.click_element(Page.system_wifi_moudle)
            except Exception as e:
                print(e)
                pass
            loc = self.get_text_locator(udid)
            for i in range(3):
                if self.wait_exist(loc):
                    try:
                        self.click_element(loc)
                        time.sleep(2)
                    except Exception as e:
                        print(e)
                        pass
                    break
                else:
                    time.sleep(2)
                    # self.swipe_by_element('up', 0.7, 0.3, 0.5, None, 1500)
            self.click_element(Page.into_eufyhome)
            self.terminate_app('com.apple.Preferences')

        if self.platform == 'android':
            i = 0
            while i < 3:
                i = i + 1
                self.tap_element(Page.robotic_refresh)
                eles = self.get_elements(Page.device_udid)
                for ele in eles:
                    if udid in ele.text:
                        self.tap_element(ele)
                        self.loading()
                        i = 3
                        break
                time.sleep(5)

    # *********************开关添加流程************************ #
    def skip_switch_guide(self):
        """
        跳过开关的引导流程
        :return:
        """
        if self.platform == 'ios':
            next_btn = ('xpath', '//*[@name="Next"]')
            self.tap_element(('name', 'Start'))  # //XCUIElementTypeButton[@name="Next"]
        elif self.platform == 'android':
            next_btn = ('xpath', '//*[@text="Next"]')
            self.tap_element(('xpath', '//*[@text="Start"]'))
        flag = True
        times = 0
        while flag and times < 3:
            times = times + 1
            if self.wait_exist(Page.switch_guide, 5):
                self.click_element(Page.switch_guide)
                # self.swipe_page('left')
            elif self.wait_exist(Page.connect_wifi, 5):
                self.tap_element(Page.connect_wifi)
                flag = False
        # self.click_element(Page.switch_guide)
        self.tap_element(next_btn)

    def select_switch_by_udid(self, udid):
        """
        选择设备联网
        :param udid:
        :return:
        """
        if self.platform == 'ios':
            self.wait_exist(Page.already_connected)
            self.activate_app('com.apple.Preferences')  # 打开手机系统设置
            try:
                self.click_element(Page.system_wifi_moudle)
            except Exception as e:
                print(e)
                pass
            loc = self.get_text_locator(udid)
            for i in range(3):
                try:
                    self.tap_element(loc)
                    break
                except Exception as e:
                    print(e)
                    time.sleep(3)
            time.sleep(2.5)
            self.click_element(Page.into_eufyhome)
            self.terminate_app('com.apple.Preferences')
            try:
                self.tap_element(Page.already_connected)
            except Exception as e:
                print(e)
                pass

        if self.platform == 'android':
            i = 0
            while i < 3:
                i = i + 1
                eles = self.get_elements(Page.device_udid)
                if eles is None:
                    time.sleep(5)
                    self.tap_element(Page.switch_refresh)
                else:
                    for ele in eles:
                        if udid in ele.text:
                            self.tap_element(ele)
                            self.loading()
                            i = 3
                            break

    def select_wifi_with_switch(self, wifi_name, wifi_pw):
        """
        开关设备设置wifi
        :param wifi_name:
        :return:
        """
        if self.platform == 'android':
            self.tap_element(('xpath', '//*[@resource-id="com.eufylife.smarthome:id/list_ap"]/android.widget.RelativeLayout[1]'))
        for i in range(4):
            if self.wait_exist(Page.manual_connect):
                break
            else:
                self.swipe_page('up')
        self.tap_element(Page.manual_connect)
        time.sleep(2)
        self.send_keys(Page.switch_wifi_name, wifi_name, 1)
        # self.tap_element(Page.switch_wifi_pw_display)
        self.send_keys(Page.switch_wifi_pw, wifi_pw, 1)
        time.sleep(2)
        self.hide_keyboard()
        time.sleep(2)
        # self.tap_element(Page.switch_save_network)
        if self.platform == 'ios':
            self.click_element(('name', 'Next'))
        else:
            self.click_element(('xpath', '//*[@text="Next"]'))
        self.loading()

    # def select_wifi_with_switch(self, wifi_name):
    #     """
    #     选择要配网的wifi
    #     :param wifi_name:
    #     :return:
    #     """
    #     if self.platform == 'ios':
    #         if self.text_display(wifi_name):
    #             self.tap_element(Page.robotic_wifi_next)
    #         else:
    #             self.tap_element(Page.manual_connect)
    #             time.sleep(2)
    #             self.send_keys(Page.wifi_name, wifi_name)
    #             self.send_keys(Page.wifi_password, '00000001')
    #             self.hide_keyboard()
    #             self.tap_element(Page.save_network)
    #             self.click_element(('name', 'Next'))
    #     if self.platform == 'android':
    #         i = 0
    #         while i < 3:
    #             i = i + 1
    #             eles = self.get_elements(Page.device_udid)
    #             if eles is None:
    #                 time.sleep(5)
    #                 self.tap_element(Page.switch_refresh)
    #             else:
    #                 for ele in eles:
    #                     if wifi_name == ele.text.strip():
    #                         self.tap_element(ele)
    #                         self.loading()
    #                         i = 3
    #                         break
    #         self.wait_exist(('xpath', '//*[@text="{}"]'.format(wifi_name)))
    #         self.tap_element(('xpath', '//*[@text="Next"]'))
    #     self.loading()

    # *********************添加灯泡************************ #

    def confirm_bulbs_status(self):
        """
        确认配网状态
        :return:
        """
        if self.platform == 'ios':
            btns = self.get_elements(Page.robotic_status_confirm)
            for btn in btns:
                text = self.get_text(btn)
                if text is not None and 'Status confirmed' in text:
                    self.click_element(btn)
                    break
        else:
            self.tap_element(Page.robotic_status_confirm)

    def bulbs_next(self):
        self.tap_element(Page.robotic_status_next)
        time.sleep(2)

    # *********************结果确认************************ #

    def wait_connect(self):
        """
        等待连接，时间180s
        :return:
        """
        if self.platform == 'ios':
            for i in range(3):
                if self.wait_exist(('xpath', '//*[@name="Connecting"]')):
                    break
            for i in range(12):
                if self.wait_not_exist(('xpath', '//*[@name="Connecting"]')):
                    break
        if self.platform == 'android':
            for i in range(3):
                if self.wait_exist(('xpath', '//*[@text="Connecting"]')):
                    break
            for i in range(12):
                if self.wait_not_exist(('xpath', '//*[@text="Connecting"]')):
                    break

    def connect_result(self):
        """
        配网结果
        :return:
        """
        if self.is_exist(Page.connect_successed):
            return True
        else:
            return False

    def set_device_name(self, name):
        """
        设置扫地机名称
        :param name:
        :return:
        """
        if self.platform == 'ios':
            self.clear_text(Page.set_device_name)
        self.send_keys(Page.set_device_name, name, 1)
        self.tap_element(Page.commit_name)

    def set_system_wifi(self, defult_wifi):
        """
        设置手机系统的wifi网络，防止配网失败导致网络异常
        :return:
        """
        if self.platform == 'ios':
            try:
                self.activate_app('com.apple.Preferences')  # 打开手机系统设置
                try:
                    self.click_element(Page.system_wifi_moudle)
                except Exception as e:
                    print(e)
                    pass
                loc = self.get_text_locator(defult_wifi)
                for i in range(3):
                    if self.wait_exist(loc):
                        try:
                            self.click_element(loc)
                            time.sleep(2)
                        except Exception as e:
                            print(e)
                            pass
                        break
                    else:
                        time.sleep(2)
            except Exception as e:
                print(e)
                self.terminate_app('com.apple.Preferences')

        if self.platform == 'android':
            try:
                self.activate_app('com.android.settings')
                time.sleep(2)
                self.tap_element(('xpath', '//*[@text="Network & internet"]'))
                time.sleep(2)
                self.tap_element(('xpath', '//*[@text="Wi‑Fi"]'))
                time.sleep(2)
                self.click_element(('id', 'com.android.settings:id/switch_widget'))
                time.sleep(2)
                self.click_element(('id', 'com.android.settings:id/switch_widget'))
                time.sleep(8)
                self.click_element(('xpath', '//*[@text="{}"]'.format(defult_wifi)))
                time.sleep(5)
            except Exception as e:
                print(e)
                time.sleep(5)
                os.system('adb shell am force-stop com.android.settings')
                # self.terminate_app('com.android.settings')
