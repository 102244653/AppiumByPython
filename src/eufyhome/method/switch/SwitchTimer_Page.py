from src.eufyhome.method.Base_Page import BasePage
from src.config.config import GlobalVar
global Page

"""
扫地机通用设置页面操作
"""


class SwitchTimerPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        if self.platform == GlobalVar.IOS:
            from src.eufyhome.ios.switchs.SwitchTimerActivity import SwitchTimerActivity
        else:
            from src.eufyhome.android.switchs.SwitchTimerActivity import SwitchTimerActivity
        global Page
        Page = SwitchTimerActivity()

    def back_switch(self):
        """
        返回
        :return:
        """
        self.click_element(Page.back_switch)

    def set_timer(self, desc, yt=1):
        """
        选择状态：on/off
        :param desc:
        :return:
        """
        self.swipe_schedule_time('timer', yt, True)
        if desc == 'ON':
            self.tap_element(Page.on)
        elif desc == 'OFF':
            self.tap_element(Page.off)

    def start_timer(self):
        """
        启动倒计时
        :return:
        """
        self.tap_element(Page.start)

    def stop_timer(self):
        """
        停止倒计时
        :return:
        """
        self.tap_element(Page.stop)

    def read_timer_status(self):
        """
        读取倒计时界面的状态
        :return:
        """
        return self.get_text(Page.switch_status)

    def is_on(self):
        """
        开关的状态是开启
        :return:
        """
        return self.compare_img(Page.on, 'switch_on')

    def is_off(self):
        """
        开关状态是关闭
        :return:
        """
        return self.compare_img(Page.off, 'switch_off')
