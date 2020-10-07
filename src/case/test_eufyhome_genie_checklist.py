import time
import pytest
from src.config.readconfig import data
from src.config.config import GlobalVar
from src.eufyhome.method.Genie_Page import GeniePage

from src.eufyhome.method.Home_Page import HomePage
from src.eufyhome.method.AddDevice_Page import AddDevicePage
from src.eufyhome.method.Base_Page import BasePage

from src.eufyhome.method.app.User_Page import UserPage
from src.eufyhome.method.app.System_Page import SystemPage
from src.eufyhome.method.app.Start_page import StartPage

global base_page, start_page, user_page, home_page, system_page, add_device_page, genie_page


@pytest.mark.repeat(0)  # 重复执行次数
@pytest.mark.usefixtures('driver_setup')  # 引用conftest.py中的driver_setup方法，创建会话
@pytest.mark.usefixtures('appium_setup')  # 引用conftest.py中的appium_setup方法，启动appium服务
class TestGenie(object):
    @pytest.fixture(scope='function')
    def init_setup(self):
        """
        使用 @pytest.fixture(scope='function') 装饰器的方法可以看做是setup方法
        scope指定级别，取值可以是"function"(default),"class","module","package" or "session"
        :return:
        """
        global base_page, start_page, user_page, home_page, system_page, add_device_page, genie_page

        GlobalVar.set_test_flag('f')

        base_page = BasePage(self.driver)
        start_page = StartPage(self.driver)
        home_page = HomePage(self.driver)
        user_page = UserPage(self.driver)
        system_page = SystemPage(self.driver)
        add_device_page = AddDevicePage(self.driver)
        genie_page = GeniePage(self.driver)

        # 检查ios升级弹窗
        try:
            start_page.ignore_ios_update()
        except Exception as e:
            print('升级弹窗处理失败：\n' + e)

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
                raise Exception('登陆账号为空')
        else:
            if data.get_username(account) in home_page.read_username():
                return
            if account is not None:
                TestGenie.change_account(account)
            else:
                raise Exception('登陆账号为空')

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

    @pytest.mark.genie
    @pytest.mark.run(order=0)
    @pytest.mark.parametrize('check_account', ['genie'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def genie_remove(self, check_account):
        """
        移除genie：
        1. app首页点击进入设备主页，点击more进入设置界面
        2. 点击remove
        【checkpoint】弹出移除成功确认弹窗
        【checkpoint】返回app首页，设备列表不显示switch
        :return:
        """
        if GlobalVar.get_remove_add() == 0:
            pytest.skip('本次指定不执行词条用例')

        home_page.into_device_home_page(data.get_device('genie'))
        genie_page.into_setting()
        genie_page.click_remove()

        assert genie_page.text_display('Are you sure you want to remove this device?'), 'genie 移除未显示确认弹窗'
        genie_page.commit_remove()
        genie_page.loading()
        genie_page.done()
        assert home_page.is_welcome(), 'genie 移除后未返回app首页'
        home_page.swipe_page('down')
        assert home_page.find_device(data.get_device('genie')) is False, 'genie 移除后设备列表未删除设备'

    @pytest.fixture(scope='function')
    def reset_phone_network(self):
        """
        检查并重置手机网络，防止配网失败影响网络
        :return:
        """
        yield 1
        if GlobalVar.get_test_flag():
            add_device_page.set_system_wifi(data.get_wifi('phone')[0])

    @pytest.mark.genie
    @pytest.mark.run(order=718)
    @pytest.mark.parametrize('check_account', ['genie'], indirect=True)
    def genie_add_device(self, check_account, reset_phone_network):
        """
        添加智能开关：
        1. app首页点击+，选择switch，跳过引导页
        2. 选择亚添加的设备id
        3. 设置wifi，勾选 Status Confirmed，点击 next
        4. 连接中，等待conecting消失
        【checkpoint】判断是否显示添加成功（文本校验）
        5. 修改设备昵称未T1100，点击保存
        6. 返回设备主页查看设备列表
        【checkpoint】首页列表刷新后显示插座T1100
        :param check_account:
        :return:
        """
        if GlobalVar.get_remove_add() == 0:
            GlobalVar.set_test_flag('f')
            pytest.skip('本次指定不执行词条用例')

        home_page.swipe_page('down')
        home_page.click_add_device()
        add_device_page.click_genie()

        add_device_page.select_switch_by_udid(data.get_device_udid('genie'))
        wifi_date = data.get_wifi('genie')
        add_device_page.select_wifi_with_switch(wifi_date[0], wifi_date[1])

        add_device_page.wait_connect()
        assert add_device_page.connect_result(), 'genie 配网连接失败'
        add_device_page.set_device_name(data.get_device('genie'))
        add_device_page.loading()
        genie_page.back_home()

        home_page.swipe_page('down')
        assert home_page.find_device(data.get_device('genie')), 'genie 配网成功后首页未查找到设备'
