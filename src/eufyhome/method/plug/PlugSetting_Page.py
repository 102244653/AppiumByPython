from src.eufyhome.method.Base_Page import BasePage
from src.config.config import GlobalVar
global Page

"""
扫地机通用设置页面操作
"""


class PlugSettingPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        if self.platform == GlobalVar.IOS:
            from src.eufyhome.ios.plug.PlugSettingActivity import PlugSettingActivity
        else:
            from src.eufyhome.android.plug.PlugSettingActivity import PlugSettingActivity
        global Page
        Page = PlugSettingActivity()

    def back_plug(self):
        """
        返回开关
        :return:
        """
        self.click_element(Page.back_home)

    def read_device_name(self):
        """
        读取设备名
        :return:
        """
        return self.get_text(Page.device_name)

    def change_device_name(self, new_name):
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

    def into_help(self):
        """
        进入帮助
        :return:
        """
        self.tap_element(Page.into_help)
        self.loading()

    def click_remove(self):
        self.tap_element(Page.remove_btn)

    def commit_remove(self):
        self.tap_element(Page.commit_remove)
        self.loading()
