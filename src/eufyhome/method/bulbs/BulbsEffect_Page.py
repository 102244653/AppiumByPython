from src.eufyhome.method.Base_Page import BasePage
from src.config.config import GlobalVar
global Page

"""
扫地机通用设置页面操作
"""


class BulbsEffectPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        if self.platform == GlobalVar.IOS:
            from src.eufyhome.ios.bulbs.BulbsEffectActivity import BulbsEffectActivity
        else:
            from src.eufyhome.android.bulbs.BulbsEffectActivity import BulbsEffectActivity
        global Page
        Page = BulbsEffectActivity()

    def close_effect_page(self):
        """
        关闭界面
        :return:
        """
        self.tap_element(Page.close_effect)
        if self.text_display('Do you want to exit Music Mode?'):
            try:
                self.yes
            except Exception as e:
                print(e)
                self.ok

    def read_bulbs_color(self):
        """
        读取灯效
        :return:
        """
        return self.get_text(Page.bulb_title)

    def click_white(self):
        """
        切换模式
        :return:
        """
        self.click_element(Page.bulbs_white)
        if self.text_display('Your phone and bulb are not'):
            self.ok

    def click_recommened(self):
        """
        模式切换
        :return:
        """
        self.click_element(Page.bulbs_recommended)
        if self.text_display('Your phone and bulb are not'):
            self.ok

    def click_color(self):
        """
        模式切换
        :return:
        """
        self.click_element(Page.bulbs_color)
        if self.text_display('Your phone and bulb are not'):
            self.ok

    def click_music(self):
        self.click_element(Page.bulbs_music)
        try:
            if self.text_display('Allow EyfuHome to record audio?'):
                self.tap_element(('xpath', '//*[@text="ALLOW"]'))
        except Exception as e:
            print(e)
            pass
        if self.text_display('Your phone and bulb are not'):
            self.ok

    def click_flow(self):
        self.click_element(Page.bulbs_flow)
        if self.text_display('Your phone and bulb are not'):
            self.ok

    def check_bulbs_effect(self, effect):
        """
        检查灯泡模式
        :param effect:
        :return:
        """
        expect_img = 'bulbs_'+effect
        return self.compare_img(Page.bulb_title, expect_img, 10)

    # def select_Relax(self):
    #     """
    #     选择灯效
    #     :return:
    #     """
    #     if self.is_exist(Page.Night_Light) is False:
    #         self.swipe_by_element('right', 0.2, 0.8, 0.5, Page.color_area, 300)
    #     self.tap_element(Page.Relax)
    #
    # def select_Read(self):
    #     """
    #     选择灯效
    #     :return:
    #     """
    #     self.tap_element(Page.Read)
    #
    # def select_Focus(self):
    #     """
    #     选择灯效
    #     :return:
    #     """
    #     self.tap_element(Page.Focus)
    #
    # def select_Night_Light(self):
    #     """
    #     选择灯效
    #     :return:
    #     """
    #     if self.is_exist(Page.Night_Light) is False:
    #         self.swipe_by_element('left', 0.8, 0.2, 0.5, Page.color_area, 300)
    #     self.tap_element(Page.Night_Light)

    def add_favorite_effect(self, text):
        """
        添加收藏,返回收藏亮度值
        :return:
        """
        self.tap_element(Page.add_favorite)
        self.send_keys(Page.favorite_name, text, 1)
        self.tap_element(Page.save_favorite)
        self.loading()

    def click_bulbs(self):
        """
        点击灯泡
        :return:
        """
        self.tap_element(Page.bulbs_btn)







