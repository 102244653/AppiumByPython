from src.eufyhome.method.Base_Page import BasePage
from src.config.config import GlobalVar
global Page

"""
扫地机通用设置页面操作
"""


class RoboticMaintencePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        if self.platform == GlobalVar.IOS:
            from src.eufyhome.ios.robotic.RoboticMaintenanceActivity import RoboticMaintenanceActivity
        else:
            from src.eufyhome.android.robotic.RoboticMaintenanceActivity import RoboticMaintenanceActivity
        global Page
        Page = RoboticMaintenanceActivity()

    def back_setting(self):
        self.click_element(Page.back_setting)

    def clear_all(self):
        """
        重置所有配材
        :return:
        """
        self.click_element(Page.clear_all)

    def clear_filter(self):
        """
        重置filter
        :return:
        """
        self.tap_element(Page.filter)
        self.click_element(Page.reset_filter)


