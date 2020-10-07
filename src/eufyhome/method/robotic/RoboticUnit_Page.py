from src.eufyhome.method.Base_Page import BasePage
from src.config.config import GlobalVar
global Page

"""
扫地机通用设置页面操作
"""


class RoboticUnitPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        if self.platform == GlobalVar.IOS:
            from src.eufyhome.ios.robotic.RoboticUnitActivity import RoboticUnitActivity
        else:
            from src.eufyhome.android.robotic.RoboticUnitActivity import RoboticUnitActivity
        global Page
        Page = RoboticUnitActivity()

    def back_setting(self):
        """
        返回
        :return:
        """
        self.click_element(Page.back_setting)

    def click_m2(self):
        """
        选择m2
        :return:
        """
        self.click_element(Page.m2)

    def click_ft2(self):
        """
        选择ft2
        :return:
        """
        self.click_element(Page.ft2)

    def check_m2(self):
        """
        检查选择单位
        :return:
        """
        return self.compare_img(Page.m2, 'm2', res=0)

    def check_ft2(self):
        """
        检查选择单位
        :return:
        """
        return self.compare_img(Page.ft2, 'ft2', res=0)
