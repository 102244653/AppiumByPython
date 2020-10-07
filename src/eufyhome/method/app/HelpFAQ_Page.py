from src.eufyhome.method.Base_Page import BasePage
from src.config.config import GlobalVar
global Page

"""
app首页
"""


class HelpFAQPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        if self.platform == GlobalVar.IOS:
            from src.eufyhome.ios.app.HelpFAQActivity import HelpFAQActivity
        else:
            from src.eufyhome.android.app.HelpFAQActivity import HelpFAQActivity
        global Page
        Page = HelpFAQActivity()

    def help_back(self):
        """
        点击help的返回按钮
        :return:
        """
        self.tap_element(Page.help_back)

    def read_product_list(self):
        """
        统计设备的列表
        :return:
        """
        product_list = set()
        for i in range(20):
            flag = False
            els = self.get_elements(Page.product_name)
            for el in els:
                text = el.text
                if text not in product_list:
                    flag = True
                    product_list.add(el.text)
            if flag:
                self.swipe_by_element('up', 0.8, 0.2, 0.5, None, 1500)
            else:
                break
        return product_list

    def is_faq_page(self):
        """
        是在faq页面
        :return:
        """
        return self.wait_exist(Page.faq_title)
