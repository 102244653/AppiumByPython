from src.eufyhome.method.Base_Page import BasePage
from src.config.config import GlobalVar
global Page

"""
app登陆注册页面操作
"""


class TimeZonePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        if self.platform == GlobalVar.IOS:
            from src.eufyhome.ios.app.TimeZoneActivity import TimeZoneActivity
        else:
            from src.eufyhome.android.app.TimeZoneActivity import TimeZoneActivity
        global Page
        Page = TimeZoneActivity()

    def move_top(self):
        """
        滑到顶部
        :return:
        """
        for i in range(20):
            if self.wait_exist(Page.time_one, 5):
                break
            else:
                self.swipe_by_element('down', 0.2, 0.8, 0.5, None, 1000)

    def read_timezone1(self):
        """
        读取第一个时区的名称
        :return:
        """
        return self.get_text(Page.time_one)

    def read_time_list(self):
        """
        读取时区列表
        :return:
        """
        if self.platform == 'ios':
            # ios列表的时区名字位置会变化，无法准确读取名称，后期优化
            return self.get_elements(Page.timezone_item)
        timezone_list = set()
        for i in range(20):
            flag = False
            els = self.get_elements(Page.timezone_item)
            for el in els:
                text = el.text
                if text not in timezone_list:
                    flag = True
                    timezone_list.add(text)
            if flag:
                self.swipe_by_element('up', 0.75, 0.2, 0.5, None, 2250)
            else:
                break
        return timezone_list

    def is_beijing(self):
        """
        当前时区是否为北京
        :return:
        """
        if self.platform == 'ios':
            flag = self.compare_img(('xpath', '//XCUIElementTypeImage[@name="common_icon_select"]/..'), 'beijing', 3)
        else:
            flag = self.wait_exist(Page.is_beijing)
        return flag

    def is_hongkong(self):
        """
        当前时区是否为香港
        :return:
        """
        if self.platform == 'ios':
            flag = self.compare_img(('xpath', '//XCUIElementTypeImage[@name="common_icon_select"]/..'), 'hongkong', 3)
        else:
            flag = self.wait_exist(Page.is_hongkong)
        return flag

    def select_timezone(self, timezone):
        """
        选择时区
        :param timezone:
        :return:
        """
        # if self.platform == 'ios':
        #     self.swipe_by_element('down', 0.8, 0.5, 0.5, None, 2000)
        if timezone == 'beijing':
            self.tap_element(Page.beijing)
        elif timezone == 'hongkong':
            self.tap_element(Page.hongkong)
        else:
            raise Exception(timezone+'暂不支持')
        self.loading()

    def back_system(self):
        """
        返回
        :return:
        """
        self.tap_element(Page.back_system)
