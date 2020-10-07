from src.eufyhome.method.Base_Page import BasePage
from src.config.config import GlobalVar
global Page

"""
扫地机通用设置页面操作
"""


class BulbsGroupPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        if self.platform == GlobalVar.IOS:
            from src.eufyhome.ios.bulbs.BulbsGroupActivity import BulbsGroupActivity
        else:
            from src.eufyhome.android.bulbs.BulbsGroupActivity import BulbsGroupActivity
        global Page
        Page = BulbsGroupActivity()

    def back_setting(self):
        """
        返回设置界面
        :return:
        """
        self.tap_element(Page.back_setting)

    def click_add_group(self):
        """
        添加分组
        :return:
        """
        if self.is_exist(Page.null_add_group):
            self.tap_element(Page.null_add_group)
        else:
            self.tap_element(Page.add_group)

    def select_room_type(self, index=0):
        """
        选择一个房间类型
        :return:
        """
        room = self.get_elements(Page.icons)
        self.tap_element(room[index])
        self.tap_element(Page.next_add)

    def set_group_name(self, group_name):
        """
        设置分组名称
        :return:
        """
        self.tap_element(Page.group_name)
        self.send_keys(Page.group_name_edit, group_name)
        self.tap_element(Page.save_name)

    def selct_device(self, device_name):
        """
        选择设备
        :param device_name:
        :return:
        """
        for ele in self.get_elements(Page.device_name):
            if device_name in ele.text:
                self.tap_element(ele)
                break

    def save_group(self):
        """
        保存分组
        :return:
        """
        self.tap_element(Page.save_group)
        self.loading()

    def find_group_list(self, group_name):
        """
        在分组列表中查找
        :return:
        """
        self.swipe_page('down')
        groups = self.get_elements(Page.list_name)
        for group in groups:
            if group_name in self.get_text(group):
                return True
        return False

    def click_group(self, group_name):
        """
        点击进入分组
        :param group_name:
        :return:
        """
        groups = self.get_elements(Page.list_name)
        for group in groups:
            if group_name in self.get_text(group):
                self.tap_element(group)
                break

    def delete_group(self):
        self.click_element(Page.delete_group_btn)
        self.yes
        self.loading()


