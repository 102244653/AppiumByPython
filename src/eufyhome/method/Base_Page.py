import random
import time
from datetime import datetime

import allure
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

import base_path
from src.util.base_method import BaseMethod
from src.config.config import GlobalVar
global Page
"""
基类页面：：公共方法
"""


class BasePage(BaseMethod):

    def __init__(self, driver):
        super().__init__(driver)
        if GlobalVar.get_platform() == GlobalVar.IOS:
            from src.eufyhome.ios.BaseActivity import BaseActivity
        else:
            from src.eufyhome.android.BaseActivity import BaseActivity
        global Page
        Page = BaseActivity()

    def loading(self, second=7):
        try:
            self.wait_not_exist(Page.progress, second)
        except Exception as e:
            print(e)
            time.sleep(5)

    @property
    def kill(self):
        self.kill_app()

    @property
    def open(self):
        self.open_app()

    @property
    def ok(self):
        """
        点击确认按钮，全局通用
        :return:
        """
        if self.platform == 'android' and self.wait_exist(Page.right_btn, 5):
            self.tap_element(Page.right_btn)
            return
        if self.wait_exist(Page.ok, 5):
            self.click_element(Page.ok)
            return
        raise NoSuchElementException

    @property
    def yes(self):
        """
        点击yes按钮，全局通用
        :return:
        """
        if self.wait_exist(Page.yes, 5):
            self.click_element(Page.yes)
            return
        raise NoSuchElementException

    @property
    def no(self):
        """
        点击no按钮，全局通用
        :return:
        """
        if self.wait_exist(Page.no, 5):
            self.click_element(Page.no)
            return
        raise NoSuchElementException

    @property
    def cancel(self):
        """
        点击取消按钮
        :return:
        """
        if self.wait_exist(Page.common_cancel, 5):
            self.click_element(Page.common_cancel)
            return
        raise NoSuchElementException

    @property
    def ignore(self):
        """
        点击取消按钮
        :return:
        """
        if self.wait_exist(Page.ignore, 5):
            self.click_element(Page.ignore)
            return
        raise NoSuchElementException

    def ignore_ios_update(self):
        """
        取消ios手机系统升级
        :return:
        """
        if self.platform == 'ios' and self.text_display('Software Update'):
            self.click_element(('name', 'Later'))
            time.sleep(3)
            self.click_element(('name', 'Remind Me Later'))
        if self.text_display('The update will try again later'):
            self.ok

    @property
    def week_id(self):
        """
        获取当前的时间：周日-周六：0-6
        :return:
        """
        now_time = datetime.now()
        return int(now_time.strftime('%w'))

    @property
    def week_name(self):
        return datetime.now().strftime('%A')

    @property
    def week_simple_name(self):
        return datetime.now().strftime('%a')

    def find_ele(self, text, classname=None):
        """
        通过文本查找元素
        :param text:
        :param classname:
        :return:
        """
        return self.get_element(self.get_text_locator(text, classname))

    def text_display(self, text):
        """
        文本是否显示，主要用于各种提示信息的校验
        :return:
        """
        if self.platform == 'ios':
            ele = '//*[contains(@name,"{}")]'.format(text)
        else:
            ele = '//*[contains(@text,"{}")]'.format(text)
        return self.wait_exist(('xpath', ele))

    def toast_text(self, message, android, ios):
        """
        读取toast内容
        :param message:
        :param android:toast是否在当前页面显示
        :param ios:toast是否在当前页面显示
        :return:
        """
        toast = self.find_toast(message, android, ios)
        return toast.text

    def is_toast_exist(self, message, android, ios):
        """
        判断toast是否显示
        :param message:
        :param android:toast是否在当前页面显示
        :param ios:toast是否在当前页面显示
        :return:
        """
        toast = self.find_toast(message, android, ios)
        if toast:
            return True
        else:
            return False

    @property
    def is_offline(self):
        """
        是否显示离线弹窗
        :return:
        """
        return self.wait_exist(Page.offline_window, 5)

    @property
    def is_ota_update(self):
        """
        是否需要固件升级
        :return:
        """
        return self.wait_exist(Page.update_window)

    def get_str(self, num=4):
        """
        获取随机字符串
        :param num:
        :return:
        """
        return ''.join(random.sample(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'z', 'y', 'x', 'w', 'v', 'u',
                                      't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e',
                                      'd', 'c', 'b', 'a'], num))

    def swipe_page(self, desc, t=1000):
        """
        页面滑动
        :param desc:
        :param t:
        :return:
        """
        try:
            if desc == 'up' or desc == 'left':
                self.swipe_by_element(desc, 0.8, 0.2, 0.5, None, t)
            elif desc == 'down' or desc == 'right':
                self.swipe_by_element(desc, 0.2, 0.8, 0.5, None, t)
        except Exception as e:
            print(e)
            pass
        time.sleep(6)

    def try_again(self):
        """
        页面是否需要刷新
        :return:
        """
        if self.wait_exist(Page.try_again, 5):
            self.tap_element(Page.try_again)

    def long_wait(self, s=30):
        """
        长时间等待，默认等待30s
        :param s:
        :return:
        """
        ele = ('xpath', '//*[@value="noelements"]')
        for i in range(int(s/10)):
            try:
                WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(ele))
            except Exception as e:
                e.args
                pass
            print('休眠时间：{} S'.format(str(10*(i+1))))

    def ignore_update(self):
        """
        固件升级忽略
        :return:
        """
        if self.text_display('Firmware Update'):
            self.ignore

    def add_check_image(self, desc):
        name = datetime.now().strftime('%m%d%H%M%S')
        path_name = u'{}/result_images/{}.png'.format(base_path.get_path(), name)
        self.screen_shot(path_name)
        allure.attach.file(path_name, "【" + desc + " checkpoint截图:{}.png】".format(name), allure.attachment_type.PNG)

    def read_time_by_img(self, device):
        """
        图片识别滚轮时间
        :return:
        """
        if device == 'T2123':
            img = self.screen_ele_shot(Page.t2123_ocr_img)
        elif device == 'T2250':
            img = self.screen_ele_shot(Page.t2250_ocr_img)
        elif device == 'T2190':
            img = self.screen_ele_shot(Page.t2190_ocr_img)
        elif device in ['T1013', 'T1015']:
            img = self.screen_ele_shot(Page.t1013_ocr_img)
        elif device == 'T1100':
            img = self.screen_ele_shot(Page.t1100_ocr_img)
        elif device == 'T1211':
            img = self.screen_ele_shot(Page.t1211_ocr_img)
        elif device == 'timer':
            img = self.screen_ele_shot(Page.timer_ocr_img)
        elif device == 'start':
            img = self.screen_ele_shot(Page.start_ocr_img)
        elif device == 'end':
            img = self.screen_ele_shot(Page.end_ocr_img)

        from PIL import Image
        import pytesseract
        text = pytesseract.image_to_string(Image.open(img))
        # 时间格式处理
        if device == 'timer':
            text = text.replace('min', '').replace(' ', '').replace('O', '0').replace('s', '').split('hour')
        else:
            text = text.replace('O', '0').split('\n\n')
        return list(map(int, text))

    def swipe_schedule_time(self, device, yt, is_timer=False):
        """
        设置定时时间
        :param device:
        :param yt: 要后延的时间
        :param is_timer: 倒计时专用
        :return:
        """
        img_t = self.read_time_by_img(device)
        t = time.localtime(time.time())
        if is_timer:
            # 读取当前时间并设置定时开始时间
            st = [0 if yt < 60 else yt//60, yt if yt < 60 else yt % 60]
            hour_btn = self.get_element(Page.timer_hour)
        else:
            # 读取当前时间并设置定时开始时间
            st = [t.tm_hour if t.tm_min + yt < 60 else t.tm_hour + 1,
                  t.tm_min + yt - 60 if t.tm_min + yt >= 60 else t.tm_min + yt]
            if device == 'start':
                hour_btn = self.get_element(Page.start_hour)
            elif device == 'end':
                hour_btn = self.get_element(Page.end_hour)
            else:
                hour_btn = self.get_element(Page.hour)

        t0 = st[0] - img_t[0]
        # 设置时钟
        for i in range(abs(t0)):
            if t0 > 0:
                self.swipe_by_element('up', 0.7, 0.3, 0.5, hour_btn, 0.8)
            if t0 < 0:
                self.swipe_by_element('down', 0.3, 0.7, 0.5, hour_btn, 0.8)

        # 设置分钟
        if is_timer:  # 倒计时操作
            min_btn = self.get_element(Page.timer_min)
        else:  # 非倒计时操作
            if device == 'start':  # away模式开始时间
                min_btn = self.get_element(Page.start_min)
            elif device == 'end':  # away模式结束时间
                min_btn = self.get_element(Page.end_min)
            else:
                min_btn = self.get_element(Page.min)
        if st[1] > img_t[1]:  # 目标时间比图片时间大
            if (img_t[1] - st[1] + 60) < (st[1] - img_t[1]):  # 上滑次数大于下滑次数
                for i in range(abs(img_t[1] - st[1] + 60)):
                    self.swipe_by_element('down', 0.3, 0.7, 0.5, min_btn, 0.8)
            else:  # 上滑次数小于下滑次数
                for i in range(abs(st[1] - img_t[1])):
                    self.swipe_by_element('up', 0.7, 0.3, 0.5, min_btn, 0.8)
        if st[1] < img_t[1]:  # 目标时间比图片时间小
            if (st[1] - img_t[1] + 60) < (img_t[1] - st[1]):  # 上滑次数小于下滑次数
                for i in range(abs(st[1] - img_t[1] + 60)):
                    self.swipe_by_element('up', 0.7, 0.3, 0.5, min_btn, 0.8)
            else:  # 上滑次数大于下滑次数
                for i in range(abs(img_t[1] - st[1])):
                    self.swipe_by_element('down', 0.3, 0.7, 0.5, min_btn, 0.8)

        print('已设置定时任务时间：'+str(st[0])+':'+str(st[1]))
        return st

    def read_schedule_time(self, simple_week):
        """
        插座、灯泡、开关读取定时任务列表时间
        :param simple_week:
        :return:
        """
        if self.platform == 'android':
            text = self.get_text(('xpath', '//*[@text="{}. "]/../android.widget.TextView[1]'.format(simple_week)))
        if self.platform == 'ios':
            text = self.get_text(('xpath', '//*[@name=" {}."]/../XCUIElementTypeStaticText[1]'.format(simple_week)))
        text = text.split('O')[0].strip().split(':')
        return list(map(int, text))

