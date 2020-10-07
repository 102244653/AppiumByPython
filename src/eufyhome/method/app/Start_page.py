from src.eufyhome.method.Base_Page import BasePage
from src.config.config import GlobalVar
import allure
global Page

"""
app登陆注册页面操作
"""


class StartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        if self.platform == GlobalVar.IOS:
            from src.eufyhome.ios.app.StartActivity import StartActivity
        else:
            from src.eufyhome.android.app.StartActivity import StartActivity
        global Page
        Page = StartActivity()

    def is_update(self):
        """
        如果需要升级，则点击取消
        :return:
        """
        pass

    def into_sign(self):
        """
        进入注册页面
        :return:
        """
        if self.wait_exist(Page.into_signup_btn, 3):
            self.tap_element(Page.into_signup_btn)

    def into_login(self):
        """
        进入登陆界面
        :return:
        """
        if self.wait_exist(Page.into_login_btn, 3):
            self.tap_element(Page.into_login_btn)

    def login_back(self):
        """
        登陆界面返回
        :return:
        """
        if self.wait_exist(Page.login_back, 3):
            self.tap_element(Page.login_back)

    def check_country(self, country):
        """
        判定地区是否为一致
        :country:
        :return:
        """
        # if self.platform == 'ios':
        #     ele = self.get_text_locator(country)
        # else:
        #     ele = self.get_text_locator(country, 'android.widget.TextView')
        # return self.wait_exist(ele, 5)
        return self.text_display(country)

    def select_country(self, desc, country):
        """
        选择指定国家
        :type:
        :country:
        :return:
        """
        if self.check_country(country) is False:
            if self.platform == 'ios':
                ele = self.get_text_locator(country, 'XCUIElementTypeStaticText')
            else:
                ele = self.get_text_locator(country, 'android.widget.TextView')
            if desc == 'login':
                self.tap_element(Page.login_country)
                self.send_keys(Page.login_country_input, country, 1)
            else:
                self.tap_element(Page.sign_country)
                self.send_keys(Page.sign_country_input, country, 1)
            self.hide_keyboard()
            self.tap_element(ele)
            if self.wait_exist(Page.country_window, 5):
                self.ok
            self.loading()

    def login_email(self, username, password):
        """
        邮箱登录
        :param country:
        :param username:
        :param password:
        :return:
        """
        self.send_keys(Page.login_email_input, username, 1)
        self.tap_element(Page.pw_visible_btn)
        self.send_keys(Page.email_pw_input, password, 1)
        self.tap_element(Page.login_btn)
        self.loading(20)

    def login_phone(self, username, password):
        """
        手机登录
        :param username:
        :param password:
        :return:
        """
        self.send_keys(Page.login_phone_input, username, 1)
        self.tap_element(Page.pw_visible_btn)
        self.send_keys(Page.phone_pw_input, password, 1)
        self.tap_element(Page.login_btn)
        self.loading(20)

    def read_login_tip(self):
        """
        读取登陆失败的弹窗
        :return:
        """
        if self.is_exist(Page.login_error_tip):
            return self.get_text(Page.login_error_tip)

    def close_login_tip(self):
        """
        关闭登陆失败提示弹窗
        :return:
        """
        if self.is_exist(Page.close_login_tip):
            self.tap_element(Page.close_login_tip)

    def sign_email(self, country, username, password):
        """
        邮箱注册
        :param country:
        :param username:
        :param password:
        :return:
        """
        self.select_country('sign', country)
        self.send_keys(Page.sign_email_input, username, 1)
        self.swipe_by_element('up', 0.45, 0.1, 0.5, None, 400)
        self.send_keys(Page.sign_password_input, password, 1)
        self.click_element(Page.signup_btn)
        self.loading(15)

    def read_sign_tip(self):
        """
        读取注册失败信息
        :return:
        """
        if self.is_exist(Page.sign_email_error_tip):
            return self.get_text(Page.sign_email_error_tip)
        elif self.is_exist(Page.sign_pw_error_tip):
            return self.get_text(Page.sign_pw_error_tip)
        else:
            return ""

    def close_sign_tip(self):
        """
        关闭注册失败弹窗
        :return:
        """
        if self.is_exist(Page.close_login_tip):
            self.tap_element(Page.close_login_tip)

    def has_login_btn(self):
        """
        是否显示登陆按钮
        :return:
        """
        if self.platform == 'ios':
            return self.is_exist(Page.into_login_btn)
        return self.is_exist(Page.login_btn)

    def logout_back_page(self):
        """
        判断是否在登陆页面
        ios=>登陆页面
        android=>默认页面
        :return:
        """
        if self.platform == 'ios':
            return self.is_exist(Page.into_login_btn)
        else:
            return self.is_exist(Page.login_btn)

    def is_start_page(self):
        return self.is_exist(Page.into_login_btn)

