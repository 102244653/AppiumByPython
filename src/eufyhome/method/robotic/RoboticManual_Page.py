import time

from src.eufyhome.method.Base_Page import BasePage
from src.config.config import GlobalVar
global Page

"""
扫地机通用设置页面操作
"""


class RoboticManualPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        if self.platform == GlobalVar.IOS:
            from src.eufyhome.ios.robotic.RoboticManualActivity import RoboticManualActivity
        else:
            from src.eufyhome.android.robotic.RoboticManualActivity import RoboticManualActivity
        global Page
        Page = RoboticManualActivity()

    def back_setting(self):
        self.click_element(Page.back_setting)

    def click_spot(self):
        self.tap_element(Page.spot)
        if self.text_display('Please place the RoboVac outside'):
            self.ok
            self.click_clean()
            time.sleep(5)
            self.click_clean()
            self.tap_element(Page.spot)
        if self.text_display('Stop heading home and start spot cleaning'):
            self.yes
        if self.text_display('Stop cleaning and start spot cleaning'):
            self.yes

    def click_clean(self):
        self.tap_element(Page.clean)
        if self.wait_exist(Page.stop_spot, 5):
            self.click_element(Page.stop_spot)

    def check_clean_status(self, expect_img):
        return self.compare_img(Page.clean, expect_img)

    def click_recharge(self):
        self.tap_element(Page.recharge)
        if self.text_display('Stop spot cleaning and head home'):
            self.yes
        if self.text_display('Stop cleaning and head home'):
            self.yes
