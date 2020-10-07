from src.eufyhome.method.Base_Page import BasePage
from src.config.config import GlobalVar
global Page

"""
扫地机通用设置页面操作
"""


class BulbsSettingPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        if self.platform == GlobalVar.IOS:
            from src.eufyhome.ios.bulbs.BulbsSettingActivity import BulbsSettingActivity
        else:
            from src.eufyhome.android.bulbs.BulbsSettingActivity import BulbsSettingActivity
        global Page
        Page = BulbsSettingActivity()

    def back_bulbs_home(self):
        """
        返回灯泡主页
        :return:
        """
        self.tap_element(Page.back_bulb)

    def read_bulbs_name(self):
        """
        读取灯泡名称
        :return:
        """
        return self.get_text(Page.bulb_name)

    def change_bulbs_name(self, n_name):
        """
        修改灯泡名称
        :param n_name:
        :return:
        """
        self.tap_element(Page.bulb_name)
        self.send_keys(Page.bulbs_name_edit, n_name, 1)
        self.tap_element(Page.save_name)

    def into_share(self):
        """
        进入分享界面
        :return:
        """
        self.tap_element(Page.share)
        self.loading()

    def into_group(self):
        """
        进入分组
        :return:
        """
        self.tap_element(Page.group)

    def into_default_light(self):
        """
        默认设置
        :return:
        """
        self.tap_element(Page.default_light)

    def into_update(self):
        """
        升级
        :return:
        """
        self.tap_element(Page.update)

    def into_help(self):
        """
        帮助
        :return:
        """
        self.tap_element(Page.help)
        self.loading()
        self.try_again()

    def click_remove(self):
        self.click_element(Page.remove)

    def commit_remove(self):
        self.tap_element(Page.commit_remove)

    def is_update(self):
        return self.is_exist(Page.update_tip)
