from src.eufyhome.method.Base_Page import BasePage
from src.config.config import GlobalVar
global Page

"""
扫地机清扫模式页面操作
"""


class RoboticCleanModelPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        if self.platform == GlobalVar.IOS:
            from src.eufyhome.ios.robotic.RoboticCleanModelActivity import RoboticCleanModelActivity
        else:
            from src.eufyhome.android.robotic.RoboticCleanModelActivity import RoboticCleanModelActivity
        global Page
        Page = RoboticCleanModelActivity()

    def is_t2123_model(self):
        """
        是否在t2123模式界面
        :return:
        """
        return self.is_exist(Page.T2123_close_model)

    def t2123_close_model(self):
        """
        t2123关闭模式界面
        :return:
        """
        self.tap_element(Page.T2123_close_model)

    def t2123_play(self):
        """
        启动清扫
        :return:
        """
        self.tap_element(Page.T2123_play)

    def t2123_auto(self):
        """
        t2123自动模式
        :return:
        """
        self.tap_element(Page.T2123_auto)

    def t2123_quickly(self):
        """
        t2123自动模式
        :return:
        """
        self.tap_element(Page.T2123_quickly)

    def t2123_spot(self):
        """
        t2123自动模式
        :return:
        """
        self.tap_element(Page.T2123_spot)

    def t2123_edge(self):
        """
        t2123自动模式
        :return:
        """
        self.tap_element(Page.T2123_edge)

    def t2250_spot(self):
        """
        t2250定点清扫模式
        :return:
        """
        self.tap_element(Page.T2250_spot)

