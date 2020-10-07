from src.eufyhome.method.Base_Page import BasePage
from src.config.config import GlobalVar
global Page

"""
扫地机清扫模式页面操作
"""


class RoboticZoneCleanPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        if self.platform == GlobalVar.IOS:
            from src.eufyhome.ios.robotic.RoboticZoneCleanActivity import RoboticZoneCleanActivity
        else:
            from src.eufyhome.android.robotic.RoboticZoneCleanActivity import RoboticZoneCleanActivity
        global Page
        Page = RoboticZoneCleanActivity()

    def back_robovac(self):
        self.click_element(Page.back_robovac)

    def close_tip(self):
        if self.wait_exist(Page.close_tip):
            self.tap_element(Page.close_tip)

    def add_zone(self):
        self.click_element(Page.add_zone)

    def start_zone_clean(self):
        self.click_element(Page.clean_btn)
