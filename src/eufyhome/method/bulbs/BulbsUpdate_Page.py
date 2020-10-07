from src.eufyhome.method.Base_Page import BasePage
from src.config.config import GlobalVar
global Page

"""
app登陆注册页面操作
"""


class BulbsUpdatePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        if self.platform == GlobalVar.IOS:
            from src.eufyhome.ios.bulbs.BulbsUpdateActivity import BulbsUpdateActivity
        else:
            from src.eufyhome.android.bulbs.BulbsUpdateActivity import BulbsUpdateActivity
        global Page
        Page = BulbsUpdateActivity()

    def back_setting(self):
        """
        返回设置界面
        :return:
        """
        self.tap_element(Page.back_setting)

    def click_update_btn(self):
        """
        点击升级按钮
        :return:
        """
        self.tap_element(Page.update_btn)

    # def read_update_status(self):
    #     """
    #     读取升级状态
    #     :return:
    #     """
    #     ac_img = self.screen_ele_shot(Page.update_btn)
    #     if self.compare_img(ac_img, 'noupdate'):
    #         return ''
    #     elif self.compare_img(ac_img, 'isupdate'):
    #         return ''
    #     elif self.compare_img(ac_img, 'updateing'):
    #         return ''
    #     else:
    #         return ''

    def read_version(self):
        """
        读取版本信息
        :return:
        """
        return self.get_text(Page.ota_version)

