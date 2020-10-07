from src.eufyhome.method.Base_Page import BasePage
from src.config.config import GlobalVar
global Page

"""
扫地机设置页面操作
"""


class RoboticFindPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        if self.platform == GlobalVar.IOS:
            from src.eufyhome.ios.robotic.RoboticFindActivity import RoboticFindActivity
        else:
            from src.eufyhome.android.robotic.RoboticFindActivity import RoboticFindActivity
        global Page
        Page = RoboticFindActivity()

    def find_back(self):
        """
        find界面返回
        :return:
        """
        self.tap_element(Page.find_back)

    def click_find(self, device):
        """
        点击寻找按钮
        :return:
        """
        if device == 'random':
            self.tap_element(Page.T2123_find_img)
        elif device == 'inertia':
            self.tap_element(Page.T2250_find_img)
        elif device == 'laser':
            self.tap_element(Page.T2190_find_img)

    def check_find_img(self, device, expect_img):
        """
        根据按钮图片检查状态
        :return:
        """
        if device == 'random':
            return self.compare_img(Page.T2123_find_img, expect_img)
        elif device == 'inertia':
            return self.compare_img(Page.T2250_find_img, expect_img)
        elif device == 'laser':
            return self.compare_img(Page.T2190_find_img, expect_img)

    def wait_status(self, status):
        """
        等待状态出现
        :param status:
        :return:
        """
        if self.wait_in(status) is not None:
            return True
        return False
