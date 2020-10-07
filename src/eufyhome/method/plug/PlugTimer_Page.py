from src.eufyhome.method.Base_Page import BasePage
from src.config.config import GlobalVar
global Page

"""
扫地机通用设置页面操作
"""


class PlugTimerPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        if self.platform == GlobalVar.IOS:
            from src.eufyhome.ios.plug.PlugTimerActivity import PlugTimerActivity
        else:
            from src.eufyhome.android.plug.PlugTimerActivity import PlugTimerActivity
        global Page
        Page = PlugTimerActivity()

    def back_plug(self):
        """
        返回pulg
        :return:
        """
        self.click_element(Page.back_plug)

    def set_timer(self, desc, yt=1):
        self.swipe_schedule_time('timer', yt, True)
        if desc == 'ON':
            self.tap_element(Page.on)
        elif desc == 'OFF':
            self.tap_element(Page.off)

    def start_timer(self):
        self.tap_element(Page.start)
        self.loading()

    def stop_timer(self):
        self.tap_element(Page.stop)
