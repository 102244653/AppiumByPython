from src.eufyhome.method.Base_Page import BasePage
from src.config.config import GlobalVar
global Page

"""
app登陆注册页面操作
"""


class LanguagePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        if self.platform == GlobalVar.IOS:
            from src.eufyhome.ios.app.LanguageActivity import LanguageActivity
        else:
            from src.eufyhome.android.app.LanguageActivity import LanguageActivity
        global Page
        Page = LanguageActivity()

    def back_system(self):
        """
        返回
        :return:
        """
        self.click_element(Page.back_system)

    def done(self):
        """
        确认切换语言
        :return:
        """
        self.click_element(Page.done)
        self.loading()

    def select_language(self, language):
        """
        切换语言
        :param language:
        :return:
        """
        if self.platform == 'android':
            _lan = ('xpath', '//*[@text="{}"]'.format(language))
        if self.platform == 'ios':
            _lan = ('name', language)

        if not self.text_display(language):
            self.swipe_page('up')

        self.tap_element(_lan)
        self.tap_element(Page.done)
        self.loading()

    @staticmethod
    def get_language(language=None):
        """
        设备默认语言库
        :param language:
        :return:
        """
        l_dict = {'简体中文': '语言',
                  '繁體中文': '語言',
                  'Deutsch': 'Sprache',
                  'Español': 'Idioma',
                  '日本語': '言語',
                  'Français': 'La langue',
                  'Italiano': 'linguaggio',
                  'Português': 'Língua',
                  'Nederlands': 'Taal',
                  'Русский': 'Язык',
                  'Türkçe': 'Dil',
                  'العربية': 'لغة',
                  'Tiếng Việt': 'Ngôn ngữ',
                  '한국어': '언어',
                  'Polski': 'Język',
                  'ไทย': 'ภาษา'
                  }
        if language is None:
            return l_dict.keys()
        else:
            return l_dict.get(language)

