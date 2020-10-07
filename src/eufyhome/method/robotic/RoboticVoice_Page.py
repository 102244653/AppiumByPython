from random import random

from src.eufyhome.method.Base_Page import BasePage
from src.config.config import GlobalVar
global Page

"""
扫地机音量设置页面操作
"""


class RoboticVoicePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        if self.platform == GlobalVar.IOS:
            from src.eufyhome.ios.robotic.RoboticVoiceActivity import RoboticVoiceActivity
        else:
            from src.eufyhome.android.robotic.RoboticVoiceActivity import RoboticVoiceActivity
        global Page
        Page = RoboticVoiceActivity()

    def back_setting(self):
        """
        返回
        :return:
        """
        self.tap_element(Page.back_setting)

    def change_voice(self, percent=None):
        """
        音量调节
        :param percent: 0-1
        :return:
        """
        start = 0.5
        el = self.get_element(Page.voice_btn)
        if percent is None:
            percent = random.uniform(0, 1)
        if self.platform == 'ios':
            value = self.get_text(Page.voice_value)
            if value == 'The device is Muted.':
                start = 0.05
            else:
                start = ((eval(value.rstrip("%")))+2) / 100
        if percent < 0.5:
            self.swipe_by_element('left', start, percent, 0.5, el)
        else:
            self.swipe_by_element('right', start, percent, 0.5, el)
        self.loading()

    def read_voice_value(self):
        """
        读取音量值
        :return:
        """
        return self.get_text(Page.voice_value)

    def change_language_voice(self):
        """
        切换扫地机的语音语言包
        :return:
        """
        pass

