import time


from src.eufyhome.method.Base_Page import BasePage
from src.config.config import GlobalVar
global Page

"""
app登陆注册页面操作
"""


class RoboticHomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        if self.platform == GlobalVar.IOS:
            from src.eufyhome.ios.robotic.RoboticHomeActivity import RoboticHomeActivity
        else:
            from src.eufyhome.android.robotic.RoboticHomeActivity import RoboticHomeActivity
        global Page
        Page = RoboticHomeActivity()

    def skip_robotic_guide(self):
        """
        跳过设备指引页面
        :return:
        """
        if self.wait_exist(Page.skip_guide, 3):
            for i in range(10):
                if self.wait_exist(Page.end_guide, 3):
                    self.tap_element(Page.end_guide)
                else:
                    self.swipe_by_element('left', 0.8, 0.2, 0.5, None, 1000)

    def robovac_is_offline(self):
        """
        扫地机是否离线状态
        :return:
        """
        if self.platform == 'ios':
            status = ('xpath', '//XCUIElementTypeButton[@name="Offline"]')
        else:
            status = ('xpath', '//android.widget.TextView[@text="Offline"]')
        return self.wait_not_exist(status, 20)

    def close_offline_window(self):
        """
        显示弹窗
        :return:
        """
        if self.is_exist(Page.offline_window):
            self.ok

    def read_t2123_name(self):
        """
        设备名称
        :return:
        """
        return self.get_text(Page.t2123_name)

    def read_t2250_name(self):
        return self.get_text(Page.t2250_name)

    def read_t2190_name(self):
        return self.get_text(Page.t2190_name)

    def read_robovac_status(self, index=8):
        """
        读取设备状态
        :return:
        """
        time.sleep(index)
        if self.platform == 'ios':
            if self.wait_exist(Page.t2123_status):
                return self.get_text(Page.t2123_status).strip()
            elif self.wait_exist(Page.t2250_status):
                return self.get_text(Page.t2250_status).strip()
            elif self.wait_exist(Page.t2190_status):
                return self.get_text(Page.t2190_status).strip()
            else:
                return ''
        else:
            return self.get_text(Page.device_status).strip()

    def check_btn_pic(self, ele_name, expect_img):
        """
        检查按钮图片是否一致
        :param ele_name: 实际图片元素
        :param expect_img: 目标图片名称
        :return:
        """
        if ele_name == 't2123play':
            locator = Page.T2123_play
        elif ele_name == 't2250play':
            locator = Page.T2250_play
        return self.compare_img(locator, expect_img, 8)

    def into_setting(self, is_2250=False):
        """
        进入设置
        :return:
        """
        if is_2250:
            self.tap_element(Page.T2250_robotic_setting)
        else:
            self.tap_element(Page.robotic_setting)
        time.sleep(1.5)

    def back_home(self):
        """
        返回app主页
        :return:
        """
        self.tap_element(Page.back_app)

    def t2123_play(self):
        """
        点击清扫按钮
        :return:
        """
        self.tap_element(Page.T2123_play)

    def t2123_mode(self):
        """
        模式选择
        :return:
        """
        self.tap_element(Page.T2123_mode)

    def t2123_schedules(self):
        """
        定时任务
        :return:
        """
        self.tap_element(Page.T2123_schedules)
        self.loading()

    def t2123_charge(self):
        """
        回充
        :return:
        """
        self.tap_element(Page.T2123_recharge)

    def t2123_find(self):
        """
        寻找扫地机
        :return:
        """
        self.tap_element(Page.T2123_find_me)

    def t2250_swipe_menu(self):
        """
        向上滑动菜单
        :return:
        """
        pass

    def t2250_suction(self):
        """
        T2250吸力设置
        :return:
        """
        self.tap_element(Page.T2250_power_set)

    def t2250_play(self):
        """
        同150开始清扫按钮
        :return:
        """
        self.tap_element(Page.T2250_play)

    def read_clean_btn_status(self):
        """
        读取开关状态:2250,2190
        :return:
        """
        text = self.get_text(Page.T2250_btn_status)
        return text

    def t2250_charge(self):
        """
        t2250回充
        :return:
        """
        self.tap_element(Page.T2250_recharge)

    def t2250_spot(self):
        """
        t2250定点清扫
        :return:
        """
        self.click_element(Page.T2250_spot)

    def t2250_schedule(self):
        """
        t2250定时任务
        :return:
        """
        self.click_element(Page.T2250_schedules)
        self.loading()

    def t2250_clean_history(self):
        """
        t2250清扫历史记录
        :return:
        """
        self.click_element(Page.T2250_cleaning_history)

    def read_clean_area(self):
        """
        读取t2190/t2250的清扫面积,单位:1, m2
        :return:
        """
        area = self.get_text(Page.clean_area)
        if self.platform == 'android':
            return float(area), self.get_text(Page.clean_area_util).strip()
        if self.platform == 'ios':
            if '㎡' in area:
                return float(area.replace('㎡', '')), '㎡'
            else:
                return float(area.replace('ft²', '')), 'ft²'

    def read_clean_time(self):
        """
        t2190/t2250清扫时间
        :return:
        """
        return self.get_text(Page.clean_time)

    def t2190_suction(self):
        """
        t2190吸力设置
        :return:
        """
        self.click_element(Page.T2190_power_set)

    def t2190_play(self):
        """
        t2190开始清扫
        :return:
        """
        self.tap_element(Page.T2190_play)
        if self.platform == 'ios':
            ele = ('xpath', '//*[starts-with(@name, "Stop")]')
        else:
            ele = ('xpath', '//*[starts-with(@text, "Stop")]')
        if self.wait_exist(ele, 5):
            self.tap_element(ele)

    def t2190_stop_spot_clean(self):
        if self.platform == 'ios':
            ele = ('name', 'Stop Spot Cleaning')
        else:
            ele = ('xpath', '//*[@text="Stop Spot Cleaning"]')
        if self.wait_exist(ele, 5):
            self.tap_element(ele)

    def t2190_read_btn_status(self):
        """
        读取开关按钮状态
        :return:
        """
        return self.get_text()

    def t2190_charge(self):
        """
        t2190回充
        :return:
        """
        self.click_element(Page.T2190_recharge)

    def t2190_zone_clean(self):
        """
        t2190指定区域清扫
        :return:
        """
        self.tap_element(Page.T2190_zone_clean)

    def t2190_schedule(self):
        """
        定时任务
        :return:
        """
        self.click_element(Page.T2190_schedule)
        self.loading()

    def into_clean_history(self):
        """
        t2190/t2250清扫历史记录
        :return:
        """
        self.click_element(Page.clean_history)
        self.loading(10)

    def t2190_creat_new_clean_history(self):
        """
        创建一条新的清扫记录
        :return:
        """
        self.t2190_play()
        time.sleep(45)
        self.t2190_charge()
        times = 1
        while times < 7:
            times = times + 1
            if self.text_display('Charging') or self.text_display('Standby'):
                break
            else:
                time.sleep(10)

    def ingore_update_languge(self):
        """
        语言包升级忽略
        固件升级忽略
        :return:
        """
        if self.text_display('RoboVac voice and APP language are different'):
            self.cancel
        if self.text_display('Firmware Update'):
            self.ignore

    def sure_charge(self):
        if self.platform == 'ios':
            self.click_element(('xpath', '//XCUIElementTypeButton[@name="Recharge"]'))
        if self.platform == 'android':
            self.click_element(('xpath', '//*[@text="Yes"]'))
