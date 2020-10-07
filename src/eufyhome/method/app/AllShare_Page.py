import time

from src.eufyhome.method.Base_Page import BasePage
from src.config.config import GlobalVar
global Page

"""
app登陆注册页面操作
"""


class AllSharePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        if GlobalVar.get_platform() == GlobalVar.IOS:
            from src.eufyhome.ios.app.AllShareActivity import AllShareActivity
        else:
            from src.eufyhome.android.app.AllShareActivity import AllShareActivity
        global Page
        Page = AllShareActivity()

    def back_system(self):
        """
        返回
        :return:
        """
        self.tap_element(Page.back_system)

    def into_device(self, device_name):
        """
        根据设备名进入设备分享
        :param device_name:
        :return:
        """
        if self.platform == 'ios':
            device = ('xpath', '//XCUIElementTypeStaticText[contains(@name,"{}")]'.format(device_name))
        else:
            device = ('xpath', '//*[contains(@text,"{}")]'.format(device_name))
        self.tap_element(device)

    def read_share_status(self, device_name):
        """
        根据设备名读取分享状态
        :return:
        """
        if self.platform == 'ios':
            ele = ('xpath', '//*[starts-with(@text,"{}")]'.format(device_name))
        else:
            ele = ('xpath', '//*[starts-with(@text,"{}")]/following-sibling::android.widget.TextView[1]'.format(device_name))
        return self.get_text(ele)

    def read_share_to_me_list(self):
        """
        读取分享列表
        :return:
        """
        share_list = set()
        els = self.get_elements(Page.shared_to_me_device)
        for el in els:
            text = el.text
            if text not in share_list:
                share_list.add(el.text)
        return share_list

    def delete_share_to_me_list(self):
        els = self.get_elements(Page.shared_to_me_device)
        for el in els:
            self.tap_element(el)
            time.sleep(1)
            if self.platform == 'ios':
                ele = ('name', 'Remove')
            else:
                ele = ('xpath', '//*[@text="Remove"]')
            self.click_element(ele)
            time.sleep(2)
            if self.platform == 'ios':
                self.tap_element(('xpath', '(//XCUIElementTypeButton[@name="Remove"])[2]'))
            else:
                self.tap_element(('id', 'com.eufylife.smarthome:id/dialog_btn_right'))
            self.loading()
