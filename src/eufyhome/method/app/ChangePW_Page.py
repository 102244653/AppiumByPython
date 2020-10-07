from src.eufyhome.method.Base_Page import BasePage
from src.config.config import GlobalVar
global Page

"""
用户中心界面
"""


class ChangePWPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        if self.platform == GlobalVar.IOS:
            from src.eufyhome.ios.app.ChangePWActivity import ChangePWActivity
        else:
            from src.eufyhome.android.app.ChangePWActivity import ChangePWActivity
        global Page
        Page = ChangePWActivity()

    def back_user(self):
        """
        返回用户中心
        :return:
        """
        self.tap_element(Page.back_user)

    def change_pw(self, old_pw, new_pw):
        """
        修改密码
        :rtype: object
        :param old_pw:
        :param new_pw:
        :return:
        """
        self.tap_element(Page.old_pwd_visible)
        self.send_keys(Page.old_pwd, old_pw, 1)
        self.tap_element(Page.new_pwd_visible)
        self.send_keys(Page.new_pwd, new_pw, 1)
        self.tap_element(Page.submit_change)

    def read_fail_text(self):
        """
        读取修改失败的提示文案,建议直接查看文本
        :return:
        """
        if self.is_exist(Page.old_pwd_error_text):
            return self.get_text(Page.old_pwd_error_text)
        elif self.is_exist(Page.new_pw_error_text):
            return self.get_text(Page.new_pw_error_text)
        return None

    def close_tip(self):
        """
        关闭密码修改错误的提示
        :return:
        """
        if self.is_exist(Page.close_change_fail):
            self.tap_element(Page.close_change_fail)



