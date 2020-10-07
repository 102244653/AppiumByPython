from src.eufyhome.method.Base_Page import BasePage
from src.config.config import GlobalVar
global Page

"""
app登陆注册页面操作
"""


class NewsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        if self.platform == GlobalVar.IOS:
            from src.eufyhome.ios.app.NewsActivity import NewsActivity
        else:
            from src.eufyhome.android.app.NewsActivity import NewsActivity
        global Page
        Page = NewsActivity()

    def back_system(self):
        """
        返回
        :return:
        """
        self.tap_element(Page.back_system)

    def clear_all(self):
        """
        一键清除
        :return:
        """
        self.tap_element(Page.clear_news)

    def delete_news(self, index=0):
        """
        单条清除
        :return:
        """
        ele = self.get_elements(Page.item_new)[index]
        self.swipe_by_element('left', 0.8, 0.2, 0.5, ele, 300)
        if self.is_exist(Page.delete_news):
            self.tap_element(Page.delete_news)

    def count_news(self):
        """
        统计消息总数
        :return:
        """
        ele = self.get_elements(Page.item_new)
        return len(ele)

    def click_news(self, index=0):
        """
        查看消息
        :param index:
        :return:
        """
        ele = self.get_elements(Page.item_new)[index]
        self.tap_element(ele)

    def read_news_title(self, index=0):
        """
        读取消息标题
        :param index:
        :return:
        """
        ele = self.get_elements(Page.item_new)[index]
        return self.get_text(ele)
