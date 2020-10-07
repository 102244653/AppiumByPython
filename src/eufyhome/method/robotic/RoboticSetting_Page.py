from src.eufyhome.method.Base_Page import BasePage
from src.config.config import GlobalVar
global Page

"""
扫地机通用设置页面操作
"""


class RoboticSettingPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        if self.platform == GlobalVar.IOS:
            from src.eufyhome.ios.robotic.RoboticSettingActivity import RoboticSettingActivity
        else:
            from src.eufyhome.android.robotic.RoboticSettingActivity import RoboticSettingActivity
        global Page
        Page = RoboticSettingActivity()

    def back_robovac(self):
        """
        返回设备主界面
        :return:
        """
        self.tap_element(Page.back_device)

    def read_device_name(self):
        """
        读取设备名称
        :return:
        """
        return self.get_text(Page.device_name)

    def change_device_name(self, new_name):
        """
        修改设备名称
        :new_name:
        :return:
        """
        self.tap_element(Page.device_name)
        self.send_keys(Page.device_name_input, new_name, 1)
        self.tap_element(Page.save)
        self.loading()

    def into_share(self):
        """
        进入分享界面
        :return:
        """
        self.tap_element(Page.setting_share)
        self.loading()

    def is_update(self):
        """
        是否有更新
        :return:
        """
        return self.is_exist(Page.is_update)

    def is_update_btn(self):
        """
        是否显示升级入口
        :return:
        """
        return self.is_exist(Page.setting_update)

    def into_update(self):
        """
        进入update界面
        :return:
        """
        self.tap_element(Page.setting_update)
        self.loading()

    def into_device_help(self):
        """
        进入设备帮助界面
        :return:
        """
        self.tap_element(Page.setting_help)
        self.try_again()

    def into_voice(self):
        """
        T2250/T2190声音设置
        :return:
        """
        self.tap_element(Page.setting_voice)
        self.loading()

    def into_find(self):
        """
        T2250/T2190寻找扫地机
        :return:
        """
        self.tap_element(Page.setting_find)

    def into_manual(self):
        """
        T2250/T2190手动控制
        :return:
        """
        self.tap_element(Page.setting_manual)

    def into_auto_clean(self):
        """
        T2250断点续扫设置
        :return:
        """
        self.tap_element(Page.auto_return)

    def t2250_back_setting(self):
        """
        t2250从断点续扫界面返回
        :return:
        """
        self.tap_element(Page.t2250_back_setting)

    def t2250_auto_clean(self):
        """
        t2250断点续撒开关点击
        :return:
        """
        self.tap_element(Page.t2250_auto_clean)

    def t2250_auto_clean_status(self):
        """
        断点续扫开关状态
        :return:
        """
        return self.is_colorful(Page.t2250_auto_clean_btn)

    def into_maintenance(self):
        """
        T2250/T2190配材
        :return:
        """
        self.tap_element(Page.setting_maintenance)
        self.loading()

    def into_unit(self):
        """
        T2190面积单位
        :return:
        """
        self.tap_element(Page.setting_unit)
        self.loading()

    def click_remove(self):
        """
        点击移除设备
        :return:
        """
        self.tap_element(Page.setting_remove)

    def commit_remove(self):
        """
        点击移除确认按钮
        :return:
        """
        self.tap_element(Page.commit_remove)



