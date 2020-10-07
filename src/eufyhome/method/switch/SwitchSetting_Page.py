from src.eufyhome.method.Base_Page import BasePage
from src.config.config import GlobalVar
global Page

"""
扫地机通用设置页面操作
"""


class SwitchSettingPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        if self.platform == GlobalVar.IOS:
            from src.eufyhome.ios.switchs.SwitchSettingActivity import SwitchSettingActivity
        else:
            from src.eufyhome.android.switchs.SwitchSettingActivity import SwitchSettingActivity
        global Page
        Page = SwitchSettingActivity()

    def back_switch(self):
        """
        返回灯泡首页
        :return:
        """
        self.click_element(Page.back_switch)

    def read_switch_name(self):
        """
        读取设备名
        :return:
        """
        return self.get_text(Page.device_name)

    def change_switch_name(self, new_name):
        """
        修改设备名
        :param new_name:
        :return:
        """
        self.tap_element(Page.device_name)
        self.send_keys(Page.edit_device_name, new_name)
        self.tap_element(Page.save_name)

    def into_share(self):
        """
        进入分享
        :return:
        """
        self.tap_element(Page.into_share)
        self.loading()

    def into_update(self):
        """
        进入升级
        :return:
        """
        self.tap_element(Page.into_update)

    def is_update(self):
        """
        是否有升级
        :return:
        """
        return self.is_exist(Page.update_tip)

    def into_help(self):
        """
        进入分享
        :return:
        """
        self.tap_element(Page.into_help)
        self.try_again()

    def click_remove(self):
        """
        点击移除
        :return:
        """
        self.click_element(Page.remove_device)

    def commit_remove(self):
        """
        弹窗确认移除
        :return:
        """
        self.tap_element(Page.commit_remove)