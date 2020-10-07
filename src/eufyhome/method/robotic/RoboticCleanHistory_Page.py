from src.eufyhome.method.Base_Page import BasePage
from src.config.config import GlobalVar
global Page

"""
扫地机清扫模式页面操作
"""


class RoboticCleanHistoryPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        if self.platform == GlobalVar.IOS:
            from src.eufyhome.ios.robotic.RoboticCleanHistoryActivity import RoboticCleanHistoryActivity
        else:
            from src.eufyhome.android.robotic.RoboticCleanHistoryActivity import RoboticCleanHistoryActivity
        global Page
        Page = RoboticCleanHistoryActivity()

    def back_robovac(self):
        """
        返回
        :return:
        """
        self.click_element(Page.back_robotic)

    def clear_all(self):
        """
        清除所有历史记录
        :return:
        """
        self.click_element(Page.clear)

    def commit_clear(self):
        if self.platform == 'ios':
            ele = ('xpath', '//*[@name="Yes"]')
        else:
            ele = ('id', 'com.eufylife.smarthome:id/dialog_btn_right')
        self.tap_element(ele)
        self.loading()

    def delete_one_by_one(self):
        """
        单条删除
        :return:
        """
        flag = True
        while flag:
            eles = self.get_elements(Page.history_item)
            if len(eles) == 0:
                return
            if len(eles) == 1:
                flag = False
            self.swipe_by_element('left', 0.9, 0.1, 0.5, eles[0], 1000)
            self.tap_element(Page.left_delete)
            self.loading()

    def count_record(self):
        return len(self.get_elements(Page.history_item))
