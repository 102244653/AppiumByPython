import time

from src.eufyhome.method.Base_Page import BasePage
from src.config.config import GlobalVar
global Page

"""
扫地机通用设置页面操作
"""


class SwitchHomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        if self.platform == GlobalVar.IOS:
            from src.eufyhome.ios.switchs.SwitchHomeActivity import SwitchHomeActivity
        else:
            from src.eufyhome.android.switchs.SwitchHomeActivity import SwitchHomeActivity
        global Page
        Page = SwitchHomeActivity()

    def skip_switch_guide(self):
        """
        跳过指引
        :return:
        """
        if self.wait_exist(Page.skip_guide, 3):
            for i in range(10):
                if self.wait_exist(Page.end_guide, 3):
                    self.tap_element(Page.end_guide)
                else:
                    self.swipe_by_element('left', 0.8, 0.2, 0.5, None, 1000)

    def switch_is_offline(self):
        """
        开关是否离线状态
        :return:
        """
        if self.platform == 'ios':
            status = ('xpath', '//XCUIElementTypeButton[@name="Offline"]')
        else:
            status = ('xpath', '//android.widget.TextView[@text="Offline"]')
        return self.wait_not_exist(status, 20)

    def back_home(self):
        """
        返回首页
        :return:
        """
        self.click_element(Page.back_home)
        time.sleep(2)

    def into_setting(self):
        """
        进入设置界面
        :return:
        """
        self.click_element(Page.switch_setting)

    def read_switch_name(self):
        """
        读取设备名称
        :return:
        """
        return self.get_text(Page.device_name)

    def click_switch_btn(self):
        """
        点击开关
        :return:
        """
        self.tap_element(Page.switch_btn)

    def read_deivce_status(self):
        """
        读取设备状态
        :return:
        """
        time.sleep(4)
        return self.get_text(Page.switch_status)

    def into_schedules(self):
        """
        进入定时任务
        :return:
        """
        self.tap_element(Page.schedules)
        self.loading()

    def into_timer(self):
        """
        进入倒计时
        :return:
        """
        self.tap_element(Page.timer)
        self.loading()

    def is_switch_home(self):
        return self.is_exist(Page.switch_btn)