import time

from src.eufyhome.method.Base_Page import BasePage
from src.config.config import GlobalVar
global Page

"""
app首页
"""


class DeviceHelpPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        if self.platform == GlobalVar.IOS:
            from src.eufyhome.ios.DevicesHelpActivity import DevicesHelpActivity
        else:
            from src.eufyhome.android.DevicesHelpActivity import DevicesHelpActivity
        global Page
        Page = DevicesHelpActivity()

    def back_setting(self):
        """
        返回设置界面
        :return:
        """
        self.tap_element(Page.back_setting)

    def read_help_title(self):
        """
        读取title列表
        :return:
        """
        title_list = set()
        for i in range(20):
            flag = False
            els = self.get_elements(Page.title_list)
            for el in els:
                text = self.get_text(el).strip()
                if text not in title_list:
                    title_list.add(text)
                    flag = True
            if flag:
                self.swipe_by_element('up', 0.7, 0.3, 0.5, None, 2250)
            else:
                break
        return title_list

    def into_feed_back(self):
        """
        点击进入反馈界面
        :return:
        """
        while not self.wait_exist(Page.feed_back):
            self.swipe_page('up')
        else:
            self.tap_element(Page.feed_back)
            time.sleep(2)

    def into_chat(self):
        """
        进入交流界面
        :return:
        """
        while not self.wait_exist(Page.chat):
            self.swipe_page('up')
        else:
            self.tap_element(Page.chat)
            time.sleep(2)

    def into_call_us(self):
        """
        进入电话界面
        :return:
        """
        while not self.wait_exist(Page.call_us):
            self.swipe_page('up')
        else:
            self.tap_element(Page.call_us)
            time.sleep(2)

    def read_phone_number(self, desc):
        """
        读取电话号码
        :param desc:
        :return:
        """
        if desc == 'us':
            text = self.get_text(Page.us_phone)
        elif desc == 'uk':
            text = self.get_text(Page.uk_phone)
        elif desc == 'de':
            text = self.get_text(Page.de_phone)
        elif desc == 'jp':
            text = self.get_text(Page.jp_phone)
        print(text)
        return text

    def submit_feed_back(self, text=None):
        """
        提交反馈:
        失败：Feedback field cannot be blank.
        成功：Thank you!Your feedback has been sent.
        :return:
        """
        self.tap_element(Page.issue_type)
        if text is not None:
            self.send_keys(Page.feed_back_text, text)
        self.tap_element(Page.submit)

    def is_help_page(self):
        """
        在设备帮助列表界面
        :return:
        """
        return self.wait_exist(Page.see_all)

    def search_device(self, device_name):
        """
        设备搜索
        :param device_name:
        :return:
        """
        self.click_element(Page.see_all)
        self.click_element(Page.search_input)
        self.send_keys(Page.search_input, device_name)

