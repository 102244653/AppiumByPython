import time

from src.eufyhome.method.Base_Page import BasePage
from src.config.config import GlobalVar
global Page

"""
扫地机通用设置页面操作
"""


class BulbsSchedulePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        if self.platform == GlobalVar.IOS:
            from src.eufyhome.ios.bulbs.BulbsScheduleActivity import BulbsScheduleActivity
        else:
            from src.eufyhome.android.bulbs.BulbsScheduleActivity import BulbsScheduleActivity
        global Page
        Page = BulbsScheduleActivity()

    def back_bulbs(self):
        self.click_element(Page.back_bulbs)

    def click_away_mode(self):
        """
        点击离家模式开关
        :return:
        """
        self.click_element(Page.away_btn)

    def add_new_schedule(self, device=None, yt=0):
        """
        添加新的定时任务
        :return:
        """
        if self.wait_exist(Page.add_schedule):
            self.click_element(Page.add_schedule)
        else:
            self.click_element(Page.null_add_schedule)

        self.tap_element(Page.edit_effect)
        self.tap_element(Page.on_btn)
        self.tap_element(Page.next)
        self.tap_element(Page.done)

        if yt != 0:
            _t = self.swipe_schedule_time(device, yt)
        weeks = self.get_elements(Page.week)
        self.click_element(weeks[self.week_id])

        self.click_element(Page.save_btn)
        self.loading()
        if yt != 0:
            return _t

    def delete_schedule(self):
        """
        删除定时任务
        :return:
        """
        flag = True
        while flag:
            time.sleep(2)
            eles = self.get_elements(Page.schedule_item)
            if len(eles) != 0:
                self.swipe_by_element('left', 0.8, 0.2, 0.5, eles[0], 1000)
                self.click_element(Page.delete_schedule_btn)
                self.yes
                self.loading()
            else:
                flag = False

    def count_schedule(self):
        """
        统计定时任务数量
        :return:
        """
        return len(self.get_elements(Page.schedule_item))

    def click_schedule_btn(self, index=0):
        """
        点击定时任务开关
        :return:
        """
        btns = self.get_elements(Page.schedule_btn)
        self.click_element(btns[index])

    def read_btn_status(self, index=0):
        """
        读取定时任务开关的状态
        :param index:
        :return:
        """
        btns = self.get_elements(Page.schedule_btn)
        return self.is_colorful(btns[index])

    def close_yellow_tip(self):
        """
        关闭小黄条
        :return:
        """
        if self.is_exist(Page.close_yelloe_tip):
            self.tap_element(Page.close_yelloe_tip)

    def click_away_mode(self):
        """
        点击离家模式开关
        :return:
        """
        self.click_element(Page.away_btn)
        self.loading()

    def read_away_mode_status(self):
        """
        读取离家模式状态
        :return:
        """
        return self.is_colorful(Page.away_btn)

