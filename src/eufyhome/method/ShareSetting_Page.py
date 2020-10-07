from src.eufyhome.method.Base_Page import BasePage
from src.config.config import GlobalVar
global Page

"""
"""


class ShareSettingPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        if self.platform == GlobalVar.IOS:
            from src.eufyhome.ios.ShareSettingActivity import ShareSettingActivity
        else:
            from src.eufyhome.android.ShareSettingActivity import ShareSettingActivity
        global Page
        Page = ShareSettingActivity()

    def back_setting(self):
        """
        返回设置界面
        :return:
        """
        self.tap_element(Page.back_setting)

    def back_share(self):
        """
        返回分享列表界面
        :return:
        """
        self.tap_element(Page.back_share)

    def add_share(self):
        """
        点击添加分享人按钮
        :return:
        """
        if self.is_exist(Page.share_null_add):
            self.tap_element(Page.share_null_add)
        else:
            self.tap_element(Page.share_add)

    def commit_share(self, email):
        """
        发起分享
        :param email:
        :return:
        """
        if self.platform == 'ios' and '@' not in email:
            self.send_keys(Page.share_member_phone_input, email, 1)
        else:
            self.send_keys(Page.share_member_input, email, 1)
        self.tap_element(Page.share_commit)
        self.loading()

    def close_share_tip(self):
        """
        关闭分享提示
        :return:
        """
        if self.is_exist(Page.close_share_tip):
            self.tap_element(Page.close_share_tip)

    def share_result(self):
        """
        正确账号提交分享后的结果
        :return:
        """
        if self.text_display('Sent Successfully'):
            return True
        else:
            return False

    def read_share_status(self, share_id):
        """
        读取指定分享者的分享状态
        :param share_id:
        :return:
        """
        ele = ''
        if self.platform == 'ios':
            ele = ('xpath', '//XCUIElementTypeStaticText[@name="{}"]/following-sibling::XCUIElementTypeStaticText'.format(share_id))
        if self.platform == 'android':
            ele = ('xpath', '//android.widget.TextView[@text="{}"]/following-sibling::android.widget.TextView'.format(share_id))
        return self.get_text(ele)

    def read_share_to_me_list(self):
        """
        读取分享列表
        :return:
        """
        share_list = set()
        els = self.get_elements(Page.share_member_item)
        for el in els:
            text = el.text
            if text not in share_list:
                share_list.add(text)
        return share_list

    def delete_share(self):
        """
        删除分享人
        :param index:
        :return:
        """
        eles = self.get_elements(Page.share_member_item)
        while eles:
            try:
                self.tap_element(eles[0])
                self.loading()
                self.tap_element(Page.share_remove)
                self.tap_element(Page.commit_remove)
                self.loading()
            except Exception as e:
                print(e)
                pass
            eles = self.get_elements(Page.share_member_item)
