import time

from src.eufyhome.method.Base_Page import BasePage
from src.config.config import GlobalVar
global Page

"""
扫地机通用设置页面操作
"""


class PlugHomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        if self.platform == GlobalVar.IOS:
            from src.eufyhome.ios.plug.PlugHomeActivity import PlugHomeActivity
        else:
            from src.eufyhome.android.plug.PlugHomeActivity import PlugHomeActivity
        global Page
        Page = PlugHomeActivity()

    def skip_plug_guide(self):
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

    def plug_is_offline(self):
        """
        插座是否离线状态
        :return:
        """
        if self.platform == 'ios':
            status = ('xpath', '//XCUIElementTypeStaticText[@name="Offline"]')
        else:
            status = ('xpath', '//android.widget.TextView[@text="Offline"]')
        return self.wait_not_exist(status, 20)

    def back_home(self):
        """
        返回app首页
        :return:
        """
        self.tap_element(Page.back_home)

    def into_setting(self):
        """
        进入设置
        :return:
        """
        self.click_element(Page.plug_setting)

    def read_plug_name(self):
        """
        读取设备名
        :return:
        """
        return self.get_text(Page.plug_name)

    def click_plug_btn(self):
        """
        点击开关
        :return:
        """
        self.tap_element(Page.plug_btn)

    def read_deivce_status(self):
        """
        读取设备状态
        :return:
        """
        time.sleep(2.5)
        return self.get_text(Page.plug_status)

    def into_schedule(self):
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

    def read_energy(self):
        """
        读取耗电量
        :return:
        """
        return self.get_text(Page.energy)

    def read_runtime(self):
        """
        读取运行时间
        :return:
        """
        return self.get_text(Page.runtime)

    def is_plug_home(self):
        """
        判断是否在插座主页
        :return:
        """
        return self.wait_exist(Page.plug_btn)

