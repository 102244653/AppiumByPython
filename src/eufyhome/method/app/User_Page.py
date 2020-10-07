from src.eufyhome.method.Base_Page import BasePage
from src.config.config import GlobalVar
global Page

"""
用户中心界面
"""


class UserPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        if self.platform == GlobalVar.IOS:
            from src.eufyhome.ios.app.UserActivity import UserActivity
        else:
            from src.eufyhome.android.app.UserActivity import UserActivity
        global Page
        Page = UserActivity()

    def back_system(self):
        self.tap_element(Page.back_btn)

    def change_name(self, new_name):
        """
        修改用户昵称
        :param new_name:
        :return:
        """
        self.tap_element(Page.username)
        self.send_keys(Page.username_input, new_name, 1)
        self.tap_element(Page.save_btn)
        self.loading()

    def is_user_id(self, user_id):
        """
        检查用户账号是否显示
        :param user_id:
        :return:
        """
        return user_id == self.get_text(Page.user_id).strip()

    def is_user_name(self, username):
        """
        检查用户名是否显示正确
        :username:
        :return:
        """
        return username == self.get_text(Page.username).strip()

    def into_change_pw(self):
        """
        点击修改密码
        :return:
        """
        self.tap_element(Page.chang_password)

    def delete_account(self):
        """
        进入删除账号
        :return:
        """
        self.tap_element(Page.delete_account)
        self.tap_element(Page.delete)

    def delete_account_window(self):
        """
        确认删除弹窗
        :return:
        """
        return self.get_text(Page.delete_window)

    def click_logout(self):
        """
        退出登陆
        :return:
        """
        self.tap_element(Page.sign_out)

    def is_logout_window(self):
        """
        是否显示退出登录确认弹窗
        :return:
        """
        return self.wait_exist(Page.logout_tip)

    def logout(self):
        self.click_logout()
        self.loading()
        if self.platform == 'ios':
            self.yes
        else:
            self.ok
        self.loading()
