from src.eufyhome.method.Base_Page import BasePage
from src.config.config import GlobalVar
global Page

"""
扫地机通用设置页面操作
"""


class BulbsDefaultLightPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        if self.platform == GlobalVar.IOS:
            from src.eufyhome.ios.bulbs.BulbsDefaultLightActivity import BulbsDefaultLightActivity
        else:
            from src.eufyhome.android.bulbs.BulbsDefaultLightActivity import BulbsDefaultLightActivity
        global Page
        Page = BulbsDefaultLightActivity()

    def is_Last_status(self):
        """
        是否是选择的最后一次效果
        :return:
        """
        return self.wait_exist(Page.last_status_icon)

    def is_custom_status(self):
        """
        是否选择的自定义灯效
        :return:
        """
        return self.wait_exist(Page.custom_status_icon)

    def click_last_status(self):
        """
        点击选择最后一次灯效
        :return:
        """
        self.tap_element(Page.last_title)

    def click_custom_status(self):
        """
        点击选择自定义灯效
        :return:
        """
        self.tap_element(Page.custom_title)

    def click_white_btn(self):
        self.click_element(Page.white_btn)

    def click_color_btn(self):
        self.click_element(Page.color_btn)

    def back_setting(self):
        """
        返回
        :return:
        """
        self.tap_element(Page.back_setting)

    def custom_save(self):
        """
        自定义灯效确认
        :return:
        """
        self.tap_element(Page.custom_done)

    def min_custom_lightness(self):
        """
        设置到最低亮度
        :return:
        """
        self.tap_element(Page.custom_title)
        self.swipe_by_element('down', 0.8, 0.2, 0.5, Page.white_bulbs_pic, 2)
        self.custom_save()
        self.loading()
