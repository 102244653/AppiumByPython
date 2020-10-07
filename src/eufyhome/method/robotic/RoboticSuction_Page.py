from src.eufyhome.method.Base_Page import BasePage
from src.config.config import GlobalVar
global Page

"""
扫地机通用设置页面操作
"""


class RoboticSuctionPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        if self.platform == GlobalVar.IOS:
            from src.eufyhome.ios.robotic.RoboticSuctionActivity import RoboticSuctionActivity
        else:
            from src.eufyhome.android.robotic.RoboticSuctionActivity import RoboticSuctionActivity
        global Page
        Page = RoboticSuctionActivity()

    def t2190_close_suction(self):
        """
        关闭吸力设置弹窗
        :return:
        """
        self.tap_element(Page.T2190_power_close)

    def t2190_standard(self):
        """
        标准模式
        :return:
        """
        self.tap_element(Page.T2190_power_standard)

    def t2190_max(self):
        """
        最大吸力
        :return:
        """
        self.tap_element(Page.T2190_power_max)

    def t2190_quiet(self):
        """
        安静模式
        :return:
        """
        self.tap_element(Page.T2190_power_quiet)

    def t2190_turbo(self):
        """
        turbo模式
        :return:
        """
        self.tap_element(Page.T2190_power_turbo)

    def t2190_is_standard(self):
        """
        是否是标准模式
        :return:
        """
        return self.is_exist(Page.T2190_power_standard_icon)

    def t2190_is_quiet(self):
        """
        是否安静模式
        :return:
        """
        return self.is_exist(Page.T2190_power_quiet_icon)

    def t2190_is_turbo(self):
        """
        是否turbo模式
        :return:
        """
        return self.is_exist(Page.T2190_power_turbo_icon)

    def t2190_is_max(self):
        """
        是否max模式
        :return:
        """
        return self.is_exist(Page.T2190_power_max_icon)

    def t2190_click_boostiq(self):
        """
        点击boostiq开关
        :return:
        """
        self.tap_element(Page.T2190_power_boostiq)

    def read_t2190_boostiq_status(self):
        """
        boostiq开关状态
        :return:
        """
        return self.is_colorful(Page.T2190_power_boostiq)

    def t2123_standard(self):
        """
        t2123吸力设置standard
        :return:
        """
        self.tap_element(Page.T2123_power_standard)

    def no_standard(self):
        """
        找不到吸力：standard
        :return:
        """
        return self.wait_exist(Page.T2123_power_standard, 5)

    def t2123_boostiq(self):
        """
        t2123吸力设置boostiq
        :return:
        """
        self.tap_element(Page.T2123_power_boostiq)

    def t2123_max(self):
        """
        t2123吸力设置max
        :return:
        """
        self.tap_element(Page.T2123_power_max)

    def t2123_close_suction(self):
        """
        t2123关闭吸力界面
        :return:
        """
        self.tap_element(Page.T2123_power_close)

    def t2250_close_suction(self):
        """
        t2250关闭吸力界面
        :return:
        """
        self.tap_element(Page.T2250_power_close)

    def t2250_standard(self):
        """
        t2250吸力设置standard
        :return:
        """
        self.tap_element(Page.T2250_power_standard)

    def t2250_turbo(self):
        """
        t2250吸力设置standard
        :return:
        """
        self.tap_element(Page.T2250_power_turbo)

    def t2250_max(self):
        """
        t2250吸力设置max
        :return:
        """
        self.tap_element(Page.T2250_power_max)

    def t2250_boostiq(self):
        """
        t2250吸力设置boostiq
        :return:
        """
        self.tap_element(Page.T2250_power_boostiq)

    def t2250_is_max(self):
        """
        t2250吸力设置max校验
        :return:
        """
        return self.wait_exist(Page.T2250_power_max_icon)

    def t2250_is_standard(self):
        """
        t2250吸力设置standard校验
        :return:
        """
        return self.wait_exist(Page.T2250_power_standard_icon)

    def t2250_is_turbo(self):
        """
        t2250吸力设置turbo
        :return:
        """
        return self.wait_exist(Page.T2250_power_turbo_icon)

    def t2250_is_boostiq(self):
        """
        t2250吸力设置turbo
        :return:
        """
        return self.wait_exist(Page.T2250_power_boostiq_icon)
