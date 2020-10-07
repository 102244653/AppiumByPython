import time

from src.eufyhome.method.Base_Page import BasePage
from src.config.config import GlobalVar
global Page

"""
扫地机通用设置页面操作
"""


class RoboticSchedulePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        if self.platform == GlobalVar.IOS:
            from src.eufyhome.ios.robotic.RoboticSchedulesActivity import RoboticSchedulesActivity
        else:
            from src.eufyhome.android.robotic.RoboticSchedulesActivity import RoboticSchedulesActivity
        global Page
        Page = RoboticSchedulesActivity()

    def back_robotic(self):
        """
        返回扫地机主页
        :return:
        """
        self.tap_element(Page.back_robotic)

    def close_yellow_tip(self):
        """
        关闭小黄条
        :return:
        """
        if self.is_exist(Page.close_yelloe_tip):
            self.tap_element(Page.close_yelloe_tip)

    def save_schedule(self):
        """
        保存定时任务
        :return:
        """
        self.click_element(Page.save_schedule)
        if self.text_display('Scheduled cleaning time is the same as'):
            self.ok
        self.loading()

    def t2123_change_schedule_status(self, desc, index=0):
        """
        t2123修改定时任务
        :return:
        """
        btns = self.get_elements(Page.t2123_btns)
        flag = self.is_colorful(btns[index])
        if desc == 'on' and flag is False:
            self.tap_element(btns[index])
        elif desc == 'off' and flag is True:
            self.tap_element(btns[index])
        self.loading()

    def t2123_click_schedules_btn(self, index=0):
        """
        t2123创建一条修改记录，操作第一个开关
        :return:
        """
        btns = self.get_elements(Page.t2123_btns)
        self.tap_element(btns[index])
        self.loading()

    def t2123_into_history(self):
        """
        t2123进入历史记录界面
        :return:
        """
        if self.wait_exist(Page.t2123_schedule_history, 2):
            self.tap_element(Page.t2123_schedule_history)
            self.loading(3)

    def t2123_delete_all_history(self):
        """
        删除所有的修改记录
        :return:
        """
        if self.platform == 'ios' and len(self.get_elements(Page.t2123_schedule_record_item)) == 0:
            return
        if self.wait_exist(Page.t2123_delete_all_record, 5):
            self.tap_element(Page.t2123_delete_all_record)
            self.yes
            time.sleep(2)

    def t2123_count_history(self):
        """
        统计修改记录总数
        :return:
        """
        return len(self.get_elements(Page.t2123_schedule_record_item))

    def t2123_back_schedule(self):
        self.tap_element(Page.t2123_back_schedule)

    def t2123_read_btn_status(self, index=0):
        """
        读取定时任务开关的状态,默认读第一格开关
        :param index:
        :return:
        """
        time.sleep(2)
        btns = self.get_elements(Page.t2123_btns)
        if self.is_colorful(btns[index]):
            return 'on'
        else:
            return 'off'

    def t2250_click_schedues_btn(self, index=0):
        """
        t2250创建一条修改记录，操作第一个开关
        :return:
        """
        time.sleep(3)
        btns = self.get_elements(Page.t2250_btns)
        self.tap_element(btns[index])
        self.loading()

    def t2250_change_schedule_status(self, desc, index=0):
        btns = self.get_elements(Page.t2250_btns)
        flag = self.is_colorful(btns[index])
        if desc == 'on' and flag is False:
            self.tap_element(btns[index])
        elif desc == 'off' and flag is True:
            self.tap_element(btns[index])
        self.loading()

    def t2250_read_btn_status(self, index=0):
        """
        读取定时任务开关的状态,默认读第一格开关
        :param index:
        :return:
        """
        time.sleep(2)
        btns = self.get_elements(Page.t2250_btns)
        if self.is_colorful(btns[index]):
            return 'on'
        else:
            return 'off'

    def t2190_count_schedule(self):
        """
        统计定时任务个数
        :return:
        """
        return len(self.get_elements(Page.t2190_schedule_item))

    def t2190_creat_new_schedule(self, device=None, ty=0):
        """
        新增一个定时任务
        :return:
        """
        if self.wait_exist(Page.t2190_null_add_schedule, 5):
            self.tap_element(Page.t2190_null_add_schedule)
        else:
            self.click_element(Page.t2190_add_schedule)
        if ty != 0:
            _t = self.swipe_schedule_time(device, ty)
        self.set_schedule_week()
        self.save_schedule()
        if ty != 0:
            return _t

    def t2190_delete_schedule(self):
        """
        循环删除
        :return:
        """
        flag = True
        while flag:
            time.sleep(2)
            eles = self.get_elements(Page.t2190_schedule_item)
            if len(eles) != 0:
                self.swipe_by_element('left', 0.8, 0.2, 0.5, eles[0], 1000)
                self.tap_element(Page.t2190_delete_schedule)
                self.yes
                self.loading()
            else:
                flag = False

    def t2190_click_schedule_btn(self, index=0):
        """
        点击定时任务开关按钮
        :param index:
        :return:
        """
        eles = self.get_elements(Page.t2190_schedule_btn)
        self.tap_element(eles[index])
        self.loading()

    def t2190_read_btn_status(self, index=0):
        """
        读取定时任务按钮状态
        :param index:
        :return:
        """
        time.sleep(2)
        btns = self.get_elements(Page.t2190_schedule_btn)
        if self.is_colorful(btns[index]):
            return 'on'
        else:
            return 'off'

    def t2190_read_schedule_time(self, simple_week):
        """
        读取定时任务时间
        :param simple_week:
        :return:
        """
        if self.platform == 'android':
            text = self.get_text(('xpath', '//*[@text="{}. "]/../android.widget.TextView[1]'.format(simple_week)))
        if self.platform == 'ios':
            text = self.get_text(('xpath', '//*[@name=" {}."]/../XCUIElementTypeStaticText[1]'.format(simple_week)))
        text = text.split('ON')[0].strip().split(':')
        return list(map(int, text))

    def read_schedule_time(self, week):
        """
        2123/2250读取定时任务时间
        :param week:日期
        :return:
        """
        if self.platform == 'android':
            text = self.get_text(('xpath', '//*[@text="{}"]/../android.widget.TextView[2]'.format(week)))
        if self.platform == 'ios':
            text = self.get_text(('xpath', '//*[@name="{}"]/../XCUIElementTypeStaticText[2]'.format(week)))
        text = text.split(':')
        return list(map(int, text))

    def into_schedule_edit(self):
        """
        t2123/t2250进入定时任务编辑界面
        :return:
        """
        week = self.week_name
        if self.platform == 'android':
            self.tap_element(('xpath', '//*[@text="{}"]'.format(week)))
        if self.platform == 'ios':
            self.tap_element(('name', week))
        self.loading()

    def set_schedule_week(self):
        """
        设置定时任务的日期
        :return:
        """
        w = self.week_id
        eles = self.get_elements(Page.week)
        self.tap_element(eles[w])
