from src.eufyhome.method.Base_Page import BasePage
from src.config.config import GlobalVar
global Page

"""
扫地机通用设置页面操作
"""


class RoboticCleanSettingPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        if self.platform == GlobalVar.IOS:
            from src.eufyhome.ios.robotic.RoboticCleanSettingActivity import RoboticCleanSettingActivity
        else:
            from src.eufyhome.android.robotic.RoboticCleanSettingActivity import RoboticCleanSettingActivity
        global Page
        Page = RoboticCleanSettingActivity()

    def back_setting(self):
        """
        返回
        :return:
        """
        self.click_element(Page.back_setting)

    def click_auto_return(self):
        """
        自动回充
        :return:
        """
        self.tap_element(Page.auto_return_btn)

    def check_auto_return(self):
        """
        检查开关状态
        :return:
        """
        return self.is_colorful(Page.auto_return_btn)

