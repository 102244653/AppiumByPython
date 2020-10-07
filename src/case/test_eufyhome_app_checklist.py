import time

import allure
import pytest
from src.config.readconfig import data
from src.config.config import GlobalVar

from src.eufyhome.method.Home_Page import HomePage
from src.eufyhome.method.AddDevice_Page import AddDevicePage
from src.eufyhome.method.ShareSetting_Page import ShareSettingPage
from src.eufyhome.method.Base_Page import BasePage
from src.eufyhome.method.DeviceHelp_Page import DeviceHelpPage

from src.eufyhome.method.app.HelpFAQ_Page import HelpFAQPage
from src.eufyhome.method.app.Language_Page import LanguagePage
from src.eufyhome.method.app.User_Page import UserPage
from src.eufyhome.method.app.TimeZone_page import TimeZonePage
from src.eufyhome.method.app.System_Page import SystemPage
from src.eufyhome.method.app.Start_page import StartPage
from src.eufyhome.method.app.News_Page import NewsPage
from src.eufyhome.method.app.ChangePW_Page import ChangePWPage
from src.eufyhome.method.app.AllShare_Page import AllSharePage

global base_page, start_page, user_page, time_zone_page, system_page, news_page, change_pw_page, home_page, \
            all_share_page, share_setting_page, add_device_page, device_help_page, help_faq_page, language_page


@pytest.mark.flaky(reruns=0)  # 失败重跑
@pytest.mark.repeat(0)  # 重复执行次数
@pytest.mark.usefixtures('driver_setup')  # 引用conftest.py中的driver_setup方法，创建会话
@pytest.mark.usefixtures('appium_setup')  # 引用conftest.py中的appium_setup方法，启动appium服务
class TestAPP(object):
    @pytest.fixture(scope='function')
    def init_setup(self):

        global base_page, start_page, user_page, time_zone_page, system_page, news_page, change_pw_page, home_page, \
            all_share_page, share_setting_page, add_device_page, device_help_page, help_faq_page, language_page

        GlobalVar.set_test_flag('f')

        base_page = BasePage(self.driver)
        start_page = StartPage(self.driver)
        home_page = HomePage(self.driver)
        user_page = UserPage(self.driver)
        time_zone_page = TimeZonePage(self.driver)
        system_page = SystemPage(self.driver)
        news_page = NewsPage(self.driver)
        change_pw_page = ChangePWPage(self.driver)
        all_share_page = AllSharePage(self.driver)
        share_setting_page = ShareSettingPage(self.driver)
        add_device_page = AddDevicePage(self.driver)
        device_help_page = DeviceHelpPage(self.driver)
        help_faq_page = HelpFAQPage(self.driver)
        language_page = LanguagePage(self.driver)

        # 检查ios升级弹窗
        try:
            start_page.ignore_ios_update()
        except Exception as e:
            print('升级弹窗处理失败：\n'+e)

    @staticmethod
    def change_account(account):
        """
        切换登陆账号
        :return:
        """
        home_page.into_system()
        system_page.view_account()
        user_page.logout()
        time.sleep(2)
        start_page.into_login()
        start_page.select_country('login', data.get_country(account))
        start_page.login_email(data.get_account(account),
                               data.get_account('pw'))
        start_page.loading(10)

    @pytest.fixture(scope='function')
    def is_login(self, init_setup):
        """
        检查并返回登陆状态
        :return:
        """
        return home_page.is_welcome()

    @pytest.fixture(scope='function')
    def not_login(self, init_setup):
        """
        不登陆，如果登陆则退出登录
        :return:
        """
        if home_page.is_welcome():
            home_page.into_system()
            system_page.view_account()
            user_page.logout()

    @pytest.fixture(scope='function')
    def check_account(self, request, init_setup):
        """
        校验当前登陆账号是否正确，不正确则自动切换
        调用的函数需要传参：
        @pytest.mark.parametrize('switch_account', ['robotic'], indirect=True)
        :param init_setup:
        :param request:
        :return:
        """
        account = request.param
        if home_page.is_welcome() is False:
            start_page.into_login()
            if account is not None:
                start_page.select_country('login', data.get_country(account))
                start_page.login_email(data.get_account(account),
                                       data.get_account('pw'))
            else:
                raise BaseException('登陆账号为空')
        else:
            if data.get_username(account) in home_page.read_username():
                return
            if account is not None:
                TestAPP.change_account(account)
            else:
                raise BaseException('登陆账号为空')

    @pytest.fixture(scope='function')
    def logout(self):
        """
        后置操作，退出登录
        首页》侧边栏》用户中心
        :return:
        """
        yield 1
        base_page.kill_app()
        base_page.open_app()
        if home_page.is_welcome():
            home_page.into_system()
            system_page.view_account()
            user_page.logout()

    @pytest.mark.run(order=1)
    @pytest.mark.app
    @pytest.mark.flaky(reruns=1, reruns_delay=20)
    @pytest.mark.parametrize('username,password,expect',
                             [('Yi@aaa.com', '12345678', 'This email address is already registered'),
                              ('Yi@a.com', '123456', 'Your password must be 8-20 characters long')])
    def test_sign_error_param(self, username, password, expect, not_login):
        """
        使用已注册的邮箱不能注册:  init_setup
        1. 点击 Sign Up，进入注册页面
        2. 选择地区：UK，输入邮箱：Yi@aaa.com，默认密码：12345678，点击Sign Up按钮提交注册
        【checkpoint】弹窗提示邮箱Yi@aaa.com已注册【This email adress is already registered . . . 】
        密码不符合规范不能注册:
        1. 点击 Sign Up，进入注册页面
        2. 输入邮箱：Yi@a.com,密码：123456，点击Sign Up按钮提交注册
        【checkpoint】注册失败，文案提示：Your password must be 8-20 characters long.
        """
        country = data.get_country('email')
        if start_page.platform != 'ios':
            start_page.login_back()
        start_page.into_sign()
        start_page.select_country('sign', country)
        start_page.sign_email(country, username, password)
        assert start_page.text_display(expect), '错误提示信息不对'

    @pytest.mark.app
    @pytest.mark.run(order=2)
    @pytest.mark.flaky(reruns=1, reruns_delay=20)
    @pytest.mark.parametrize('username,password', [(data.get_account('sign'), data.get_account('pw'))])
    def test_sign_success(self, username, password, not_login):
        """
        输入未注册的邮箱及正确的密码可注册成功：
        1. 点击 Sign Up，进入注册页面
        2. 输入密码Yi@a. com,密码：12345678，点击SignUp按住提交注册
        【checkpoint】注册成功进入app，显示 welcome
        【checkpoint】检查当前登陆账号是否为：Yi@a.com
        """
        country = data.get_country('email')
        if start_page.platform != 'ios':
            start_page.login_back()
        start_page.into_sign()
        start_page.select_country('sign', country)
        start_page.sign_email(country, username, password)

        assert home_page.is_welcome(), '注册后未进入APP首页'
        home_page.into_system()
        system_page.view_account()
        assert user_page.is_user_id(username), '登陆账号与注册账号不一致'

    @pytest.mark.app
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('check_account', ['sign'], indirect=True)
    @pytest.mark.parametrize('old_pw,new_pw,expect',
                             [('1111111111', '11111111', 'The password you entered is incorrect.'),
                              (data.get_account('pw'), '111111', 'Your password must be 8-20 characters long.')])
    @pytest.mark.flaky(reruns=1, reruns_delay=20)
    def test_change_error_password(self, old_pw, new_pw, expect, check_account):
        """
        当前密码输入错误不能修改:
        1. 进入用户中心，点击 changge password
        2. 输入错误当前密码：11111111，新密码：11111111，点击提交修改
        【checkpoint】文本提示当前密码错误：The password you entered is incorrect.
        1. 进入用户中心，点击 changge password
        2. 输入正确当前密码：00000000，新密码：111111，点击提交修改
        【checkpoint】注册失败，文案提示：Your password must be 8-20 characters long.
        新密码不符合要求不能修改:
        """
        home_page.into_system()
        system_page.view_account()
        user_page.into_change_pw()
        change_pw_page.change_pw(old_pw, new_pw)
        assert change_pw_page.text_display(expect), '错误提示信息显示不对'

    @pytest.mark.app
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('check_account', ['sign'], indirect=True)
    @pytest.mark.parametrize('old_pw,new_pw', [(data.get_account('pw'), data.get_account('npw'))])
    @pytest.mark.flaky(reruns=1, reruns_delay=20)
    def test_change_password_success(self, old_pw, new_pw, check_account):
        """
        新旧密码均满足要求修改成功:
        1. 进入用户中心，点击 changge password
        2. 输入正确当前密码：12345678，新密码：11111111，点击提交修改
        【checkpoint】toast提示密码修改成功：Your Password has been successfully changed.
        【checkpoint】 成功返回用户中心页面
        """
        home_page.into_system()
        system_page.view_account()
        user_page.into_change_pw()
        change_pw_page.change_pw(old_pw, new_pw)

        assert user_page.is_user_id(data.get_account('sign')), '用户修改密码失败'

    @pytest.mark.app
    @pytest.mark.run(order=5)
    @pytest.mark.parametrize('check_account', ['sign'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=20)
    def test_change_username(self, check_account):
        """
        修改当前用户昵称：
        1. 进入用户中心个人信息页面，将用户昵称修改为AA，点击保存
        【checkpoint】用户中心昵称变更为AA
        2.点击返回回到侧边栏
        【checkpoint】用户昵称变更为AA
        3.点击返回回到app首页
        【checkpoint】用户昵称变更为AA
        """
        home_page.into_system()
        system_page.view_account()
        _id = user_page.get_str()
        user_page.change_name('sign' + _id)
        assert user_page.is_user_name('sign' + _id), '用户中心昵称显示错误'
        user_page.back_system()
        assert system_page.read_account() == 'sign' + _id, '侧边栏昵称显示错误'
        system_page.back_home()
        assert home_page.read_username() == 'sign' + _id, 'app主页昵称显示错误'

    @pytest.fixture(scope='function')
    def set_default_english(self):
        """
        设置app默认语言为英语
        :return:
        """
        yield 1
        system_page.into_language()
        language_page.swipe_page('down')
        language_page.select_language('English')

    @pytest.mark.app
    @pytest.mark.run(order=6)
    @pytest.mark.parametrize('check_account', ['sign'], indirect=True)
    def change_app_language(self, check_account, set_default_english):
        """
        切换app语言包：
        1.便利切换语言包，退出然后校验语言选项标题是否切换正确
        :return:
        """
        home_page.into_system()
        lan = language_page.get_language()
        f = []

        for l in lan:
            time.sleep(2)
            system_page.into_language()
            language_page.select_language(l)
            time.sleep(2)

            now_lan = system_page.read_language()
            if language_page.get_language(l) not in now_lan:
                f.append(l)

        assert len(f) == 0, '语言遍历切换异常，校验错误语种：' + str(f)

    @pytest.mark.app
    @pytest.mark.run(order=7)
    @pytest.mark.parametrize('check_account', ['sign'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=20)
    def test_delete_account(self, check_account):
        """
        正常删除账户:
        1. 进入用户中心，点击 delete account
        2.点击 delete按钮
        【checkpoint】弹出确认弹窗:Are you sure you want to delete this account?
        3.点击 ok按钮
        【checkpoint】检查是否回到登陆页面（安卓和ios页面不一样）
        """
        home_page.into_system()
        system_page.view_account()
        user_page.delete_account()
        assert user_page.delete_account_window() == 'Are you sure you want to delete this account?', '未显示删除账号确认弹窗'
        if user_page.platform == 'ios':
            user_page.yes
        else:
            user_page.ok
        assert start_page.is_start_page(), '未返回到登陆界面'

        start_page.into_login()
        start_page.login_email(data.get_account('sign'), data.get_account('pw'))
        assert start_page.text_display('Incorrect email login or password.'), '已注销账号登陆异常'

    @pytest.mark.app
    @pytest.mark.run(order=8)
    @pytest.mark.parametrize('phone,pw,expect', [('135341739', '12345678', 'Incorrect phone number format'),
                                                 ('13534173939', '12345789', 'Incorrect email login or password')])
    @pytest.mark.flaky(reruns=1, reruns_delay=20)
    def test_login_error_phone(self, phone, pw, expect, not_login):
        """
        输入错误手机号不能登陆:
        1. 进入登陆页面，国家选择中国
        【checkpoint】区域=中国
        2.输入错误账号：135341739，密码：12345678，点击登录
        【checkpoint】登陆失败，toast提示手机号错误：incorrect phone number format.
        输入错误密码不能登陆:
        1. 进入注册页面，国家选择中国
        【checkpoint】区域=中国
        2. 输入账号：13534173939，错误密码：123456，点击登录
        【checkpoint】登陆失败，toast提示密码错误：Incorrect email login or password
        """
        start_page.into_login()
        start_page.select_country('login', data.get_country('phone'))
        assert start_page.check_country(data.get_country('phone')), '账号登录国家选择错误'
        start_page.login_phone(phone, pw)
        if start_page.platform == 'ios':
            assert start_page.is_toast_exist(expect, True, True), '错误手机号/密码登陆的提示信息错误'
        else:
            assert start_page.text_display(expect), '错误手机号/密码登陆的提示信息错误'

    @pytest.mark.app
    @pytest.mark.run(order=9)
    @pytest.mark.flaky(reruns=1, reruns_delay=20)
    def test_login_phone_success(self, not_login):
        """
        输入正确手机号及正确的手机密码可正常登陆:
        1. 进入登陆页面，国家选择中国
        【checkpoint】区域=中国
        2. 输入账号：13534173939，密码：12345678，点击登录
        【checkpoint】登陆成功进入app首页
        3.进入用户中心界面
        【checkpoint】用户中心账号为：13534173939
        """
        start_page.into_login()
        start_page.select_country('login', data.get_country('phone'))
        assert start_page.check_country(data.get_country('phone')), '账号登录国家选择错误'
        start_page.login_phone(data.get_account('phone'), data.get_account('pw'))  # data.get_account('pw')
        assert home_page.is_welcome(), '登陆失败，未进入app主页'
        home_page.into_system()
        system_page.view_account()
        assert user_page.is_user_id(data.get_account('phone')), '手机登陆后账号显示错误'

    @pytest.mark.app
    @pytest.mark.run(order=10)
    @pytest.mark.parametrize('email,pw,expect', [('test@test', '12345678',
                                                  'Please enter a valid email address'),
                                                 ('robotic@test.com', '987654321',
                                                  'Incorrect email login or password. Please try again.')])
    @pytest.mark.flaky(reruns=1, reruns_delay=20)
    def test_login_error_email(self, email, pw, expect, not_login):
        """
        输入错误邮箱不能登陆:
        1. 进入注册页面，国家选择UK
        【checkpoint】区域=UK
        2. 输入账号：YI@aaa.com，错误密码：123456，点击登录
        【checkpoint】登陆失败，文本提密码错误：Please enter a valid email address (Example: name@domain.com).
        输入错误密码不能登陆：
        1. 进入注册页面，国家选择UK
        【checkpoint】区域=UK
        2. 输入账号：YI@aaa.com，错误密码：123456，点击登录
        【checkpoint】登陆失败，文本提密码错误：Incorrect email login or password. Please try again.
        """
        start_page.into_login()
        start_page.select_country('login', data.get_country('email'))
        assert start_page.check_country(data.get_country('email'))
        start_page.login_email(email, pw)
        assert start_page.text_display(expect), '错误邮箱/密码登陆提示信息错误'

    @pytest.mark.app
    @pytest.mark.run(order=11)
    @pytest.mark.flaky(reruns=1, reruns_delay=20)
    def test_login_email_success(self, not_login):
        """
        输入正确邮箱及正确的邮箱密码可正常登陆:
        1. 进入注册页面，国家选择UK
        【checkpoint】区域=UK
        2. 输入账号：YI@aaa. com，密码：12345678，点击登录
        【checkpoint】登陆成功进入app，显示welcome
        3.进入用户中心界面
        【checkpoint】用户中心账号为：YI@aaa. com
        """
        start_page.into_login()
        start_page.select_country('login', data.get_country('email'))
        assert start_page.check_country(data.get_country('email'))
        start_page.login_email(data.get_account('share'), data.get_account('pw'))
        assert home_page.is_welcome(), '登陆失败，未进入app主页'
        home_page.into_system()
        system_page.view_account()
        assert user_page.is_user_id(data.get_account('share')), '邮箱登陆后账号显示错误'

    @pytest.mark.app
    @pytest.mark.run(order=12)
    @pytest.mark.parametrize('check_account', ['share'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=20)
    def test_change_timezone(self, check_account):
        """
        检查是否可以切换时区: 【ios的定位有问题】
        1. 点击timezone进入时区列表界面
        #【checkpoint】默认选择香港时区 （考虑到用例可能失败，无法保证默认值，故去掉此验证）
        2.选择北京时区，退出时区界面再次进入
        【checkpoint】当前选择时区变更为北京
        """
        home_page.into_system()
        system_page.into_timezone()
        flag = time_zone_page.is_beijing()
        if flag:
            time_zone_page.select_timezone('beijing')
        else:
            time_zone_page.select_timezone('hongkong')
        time_zone_page.back_system()
        system_page.into_timezone()
        if flag:
            assert time_zone_page.is_beijing(), '时区切换失败'
        else:
            assert time_zone_page.is_hongkong(), '时区切换失败'

    @pytest.mark.app
    @pytest.mark.run(order=13)
    @pytest.mark.parametrize('check_account', ['share'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=20)
    def test_count_timezone(self, check_account):
        """
        检查时区总数:
        1. 点击timezone进入时区列表界面，将列表滑动到第一个
        【checkpoint】检查第一个是否为 Midway island,Samoa
        2. 滑动列表统计时区总数
        【checkpoint】时区总数=76
        """
        home_page.into_system()
        system_page.into_timezone()
        if time_zone_page.platform == 'android':
            time_zone_page.move_top()

        assert len(time_zone_page.read_time_list()) == 76, '时区列表总数错误'

    @pytest.mark.app
    @pytest.mark.run(order=14)
    @pytest.mark.parametrize('check_account', ['share'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=20)
    def faq_list(self, check_account):
        """
        首页进入检查help设备类别显示是否正常:
        1. 点击app主页入口进入FAQ页面，遍历所有设备名称
        【checkpoint】查看所有设别类型是否全部显示
        侧边栏help能进入FAQ（检查入口）：
        1. 进入侧边栏，点击help进入FAQ界面
        【checkpoint】检查FAQ模块是否存在
        """
        home_page.into_help()
        products = help_faq_page.read_product_list()
        faq_list = eval(data.get_faq('product'))
        flag1 = len(products) == len(faq_list)
        _faq = ''
        for faq in faq_list:
            if faq not in products:
                _faq = _faq + ',' + faq
        assert flag1 and len(_faq) == 0, 'FAQ列表的设备显示不全,缺少：' + _faq

    @pytest.mark.debug
    @pytest.mark.run(order=15)
    @pytest.mark.parametrize('check_account', ['share'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=20)
    def Help_Page(self, check_account):
        """
        侧边栏help能进入FAQ（检查入口）:
        1. 进入侧边栏，点击help进入FAQ界面
        【checkpoint】检查FAQ页面标题
        :param check_account:
        :return:
        """
        home_page.into_system()
        system_page.into_help()
        assert help_faq_page.is_faq_page(), 'Help页面进入失败'

    @pytest.mark.app
    @pytest.mark.run(order=16)
    @pytest.mark.parametrize('check_account', ['share'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=20)
    def devices_list(self, check_account):
        """
        添加设备列表的扫地机设备类别:
        1. 点击app主页添加按钮进入设备类型界面
        【checkpoint】共有五种设备类型
        2. 点击扫地机进入扫地机列表，遍历扫地机类别
        【checkpoint】共有11款扫地机
        """
        home_page.click_add_device()

        device_type = add_device_page.read_device_type()
        flag1 = True
        device_text = ''
        add_device_page.add_check_image('设备种类')
        for ele1 in data.get_device_type('device_type'):
            if ele1 not in device_type:
                flag1 = False
                device_text = ele1 + ';' + device_text
        add_device_page.add_check_image('设备类型')
        add_device_page.click_robotic()

        robotic_type = add_device_page.read_robotic_list()
        flag2 = True
        robotic_text = ''
        for ele2 in data.get_device_type('robotic_type'):
            if ele2 not in robotic_type:
                flag2 = False
                robotic_text = ele2 + ';' + robotic_text

        assert flag1 and flag2, '设备类型缺失：' + device_text + ' & 扫地机类型缺失：' + robotic_text

    @pytest.mark.app
    @pytest.mark.run(order=17)
    @pytest.mark.parametrize('check_account', ['share'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=20)
    def test_logout(self, check_account):
        """
        正常退出登录:
        1. 进入个人中心界面，点击sign out按钮
        【checkpoint】显示退出确认弹窗
        2.点击 ok 按钮
        【checkpoint】回到登陆界面：安卓显示账号密码输入框，ios显示登陆注册入口
        """
        home_page.into_system()
        system_page.view_account()
        user_page.click_logout()
        assert user_page.is_logout_window(), '未显示退出登陆确认弹窗'
        if user_page.platform == 'ios':
            user_page.yes
        else:
            user_page.ok
        assert start_page.logout_back_page(), '退出登录未回到登陆界面'
