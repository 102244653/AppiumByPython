from src.eufyhome.method.Base_Page import BasePage
from src.config.config import GlobalVar
global Page


class GeniePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        if self.platform == GlobalVar.IOS:
            from src.eufyhome.ios.GenieActivity import GenieActivity
        else:
            from src.eufyhome.android.GenieActivity import GenieActivity
        global Page
        Page = GenieActivity()

    def back_home(self):
        self.click_element(Page.back_home)

    def into_setting(self):
        self.click_element(Page.into_setting)

    def back_genie(self):
        self.click_element(Page.back_genie)

    def click_remove(self):
        self.click_element(Page.remove_device)

    def done(self):
        self.click_element(Page.done)

    def commit_remove(self):
        """
        弹窗确认移除
        :return:
        """
        self.tap_element(Page.commit_remove)