from src.eufyhome.method.Base_Page import BasePage
from src.config.config import GlobalVar
global Page

"""
扫地机通用设置页面操作
"""


class BulbsFavoritePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        if self.platform == GlobalVar.IOS:
            from src.eufyhome.ios.bulbs.BulbsFavoriteActivity import BulbsFavoriteActivity
        else:
            from src.eufyhome.android.bulbs.BulbsFavoriteActivity import BulbsFavoriteActivity
        global Page
        Page = BulbsFavoriteActivity()

    def count_favorite_title(self):
        """
        统计收藏总数
        :return:
        """
        return len(self.get_elements(Page.favorite_name))

    def find_favorite(self, name):
        """
        验证某个收藏是否存在
        :param name:
        :return:
        """
        favorite = self.get_elements(Page.favorite_name)
        for ele in favorite:
            if name in ele.text:
                return True
        return False

    def select_favorite(self, name):
        """
        选择一个收藏模式
        :return:
        """
        favorite = self.get_elements(Page.favorite_name)
        for ele in favorite:
            if name in ele.text:
                _id = favorite.index(ele)
                self.tap_element(self.get_elements(Page.select_favorite_btn)[_id])
                return
        raise Exception('收藏列表未找到：'+name)

    def back_bulbs(self):
        """
        返回灯泡主页
        :return:
        """
        self.tap_element(Page.back_bulbs)

    def delete_favorite(self):
        """
        一个个删除
        :return:
        """
        flag = True
        while flag:
            if self.platform == 'ios':
                self.swipe_page('down')
            favorite = self.get_elements(Page.delete_swipe_btn)
            print(str(len(favorite)))
            if len(favorite) > 0:
                self.swipe_by_element('left', 0.9, 0.1, 0.5, favorite[0], 1000)
                self.tap_element(Page.delete_btn)
                self.yes
                self.loading()
            else:
                flag = False
