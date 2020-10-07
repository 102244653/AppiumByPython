from selenium.webdriver.common.by import By

from src.eufyhome.method.Base_Page import BasePage
from src.config.config import GlobalVar
global Page

"""
扫地机通用设置页面操作
"""


class BulbsGroupHomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        if self.platform == GlobalVar.IOS:
            from src.eufyhome.ios.bulbs.BulbsGroupHomeAvtivity import BulbsGroupHomeActivity
        else:
            from src.eufyhome.android.bulbs.BulbsGroupHomeAvtivity import BulbsGroupHomeActivity
        global Page
        Page = BulbsGroupHomeActivity()

    def back_home(self):
        """
        返回app主页
        :return:
        """
        self.click_element(Page.back_home)

    def read_home_group_name(self):
        return self.get_text(Page.home_group_name)

    def into_group_effect(self):
        self.tap_element(Page.group_effect)

    def into_group_setting(self):
        self.tap_element(Page.group_setting)

    def back_group(self):
        self.click_element(Page.save)
        self.loading()

    def change_group_name(self, new_name):
        self.click_element(Page.setting_group_name)
        self.send_keys(Page.edit_group_name, new_name, 1)
        self.click_element(Page.save_group_name)

    def delete_this_group(self):
        self.click_element(Page.delete_group)

    def group_is_on(self):
        """
        灯组是否开启
        :return:
        """
        return self.wait_exist(Page.group_is_on)

    def click_group_bulbs(self):
        """
        点击灯组的灯泡按钮
        :return:
        """
        self.tap_element(Page.group_bulbs_bar)

    def read_group_status(self):
        """
        读取开启后的灯组状态
        :return:
        """
        return self.get_text(Page.group_home_status)

    # *******************************分组模式界面********************************** #

    def click_white(self):
        self.click_element(Page.white_btn)

    def click_color(self):
        self.click_element(Page.color_btn)

    def click_flow(self):
        self.click_element(Page.flow_btn)

    def close_effect(self):
        self.click_element(Page.close_effect)

    def read_group_effect(self):
        return self.get_text(Page.effect_text)

    def check_group_effect(self, effect):
        """
        检查灯泡模式
        :param effect:
        :return:
        """
        self.add_check_image('灯组'+effect+'模式')
        if self.platform == 'ios':
            expect_img = 'bulbs_group_'+effect
        else:
            expect_img = 'bulbs_'+effect
        return self.compare_img(Page.effect_text, expect_img, 10)
