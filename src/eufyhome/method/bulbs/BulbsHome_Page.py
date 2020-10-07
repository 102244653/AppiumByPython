import time

from src.eufyhome.method.Base_Page import BasePage
from src.config.config import GlobalVar
global Page

"""
扫地机通用设置页面操作
"""


class BulbsHomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        if self.platform == GlobalVar.IOS:
            from src.eufyhome.ios.bulbs.BulbsHomeActivity import BulbsHomeActivity
        else:
            from src.eufyhome.android.bulbs.BulbsHomeActivity import BulbsHomeActivity
        global Page
        Page = BulbsHomeActivity()

    def skip_bulbs_guide(self):
        """
        跳过指引
        :return:
        """
        if self.wait_exist(Page.skip_guide, 3):
            for i in range(10):
                if self.wait_exist(Page.end_guide, 3):
                    self.tap_element(Page.end_guide)
                else:
                    self.swipe_by_element('left', 0.8, 0.2, 0.5, None, 1000)

    def bulbs_is_offline(self):
        """
        扫地机是否离线状态
        :return:
        """
        if self.platform == 'ios':
            status = ('xpath', '//XCUIElementTypeButton[@name="Offline"]')
        else:
            status = ('xpath', '//android.widget.TextView[@text="Offline"]')
        return self.wait_not_exist(status, 20)

    def back_home(self):
        """
        返回app主页
        :return:
        """
        self.click_element(Page.back_home)
        time.sleep(2)

    def into_setting(self):
        """
        进入设置界面
        :return:
        """
        self.tap_element(Page.bulb_setting)
        self.loading()

    def read_bulbs_name(self):
        """
        读取设备名
        :return:
        """
        return self.get_text(Page.device_name)

    def close_offline_window(self):
        """
        显示弹窗
        :return:
        """
        if self.is_exist(Page.offline_window):
            self.ok

    def change_bulbs_lightness(self, desc):
        """
        调节灯泡亮度
        :return:
        """
        if desc == 'big':
            self.swipe_by_element('up', 0.9, 0.1, 0.5, Page.bulb_progress_bar, 400)
        elif desc == 'small':
            self.swipe_by_element('down', 0.1, 0.9, 0.5, Page.bulb_progress_bar, 400)
        self.loading()

    def into_effect(self):
        """
        进入effect
        :return:
        """
        self.click_element(Page.effect)
        self.loading()

    def into_schedules(self, is_color=True):
        """
        进入schedules
        :return:
        """
        if is_color:
            self.tap_element(Page.color_schedules)
        else:
            self.tap_element(Page.white_schedules)
        self.loading()

    def into_favorites(self, is_color=True):
        """
        进入收藏
        :return:
        """
        if is_color:
            self.tap_element(Page.favorites_page)
        else:
            self.tap_element(Page.white_favorites_page)
        self.loading(10)

    def read_bulbs_effect(self):
        """
        读取灯效
        :return:
        """
        if self.is_exist(Page.bulb_color):
            return self.get_text(Page.bulb_color)
        return ''

    def bulb_status(self, is_color=True):
        """
        读取灯泡状态:开或关
        :return:
        """
        if is_color:
            return self.wait_exist(Page.bulb_color)
        else:
            return self.wait_exist(Page.add_white_favorites)

    def click_bulbs(self):
        """
        点击灯泡
        :return:
        """
        self.tap_element(Page.bulb_progress_bar)

    def change_lightness(self, desc):
        """
        读取灯泡亮度值
        :return:
        """
        if desc == 'down':
            self.swipe_by_element('down', 0.25, 0.7, 0.5, None, 3000)
        elif desc == 'up':
            if self.platform == 'ios':
                self.swipe_by_element('up', 0.5, 0.25, 0.5, None, 3000)
            else:
                self.swipe_by_element('up', 0.6, 0.25, 0.5, None, 3000)

    def check_lightness_img(self, expect_img):
        return self.compare_img(Page.bulb_progress_bar, expect_img, 10)

    def is_bulbs_home_page(self):
        """
        判断是否在灯泡主页
        :return:
        """
        return self.is_exist(Page.bulb_progress_bar)
