from src.eufyhome.method.Base_Page import BasePage
from src.config.config import GlobalVar
global Page

"""
侧边栏界面
"""


class SystemPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        if self.platform == GlobalVar.IOS:
            from src.eufyhome.ios.app.SystemActivity import SystemActivity
        else:
            from src.eufyhome.android.app.SystemActivity import SystemActivity
        global Page
        Page = SystemActivity()

    def back_home(self):
        """
        返回主页
        :return:
        """
        self.tap_element(Page.back_home)

    def is_account(self):
        """
        是否显示账号信息
        :return:
        """
        return self.is_exist(Page.account)

    def view_account(self):
        """
        查看账户
        :return:
        """
        self.tap_element(Page.view_account)

    def read_account(self):
        """
        读取当前账号的昵称
        :return:
        """
        return self.get_text(Page.account)

    def into_news(self):
        """
        进入消息页面
        :return:
        """
        self.tap_element(Page.news)
        self.loading()

    def is_new_tip(self):
        """
        是否有新消息（小红点）
        :return:
        """
        return self.is_exist(Page.news_tip)

    def into_sharing(self):
        """
        进入分享界面
        :return:
        """
        self.tap_element(Page.device_sharing)
        self.loading()

    def into_timezone(self):
        """
        进入时区界面
        :return:
        """
        self.tap_element(Page.timezone)
        self.loading()
        if self.platform == 'ios':
            self.swipe_by_element('down', 0.4, 0.6, 0.5, None, 2000)

    def into_help(self):
        """
        进入FAQ界面
        :return:
        """
        self.tap_element(Page.help)
        self.loading()

    def into_language(self):
        """
        进入language页面
        :return:
        """
        if self.is_exist(Page.language):
            self.tap_element(Page.language)

    def read_language(self):
        """
        读取当前语言类型
        :return:
        """
        return self.get_text(Page.language)

