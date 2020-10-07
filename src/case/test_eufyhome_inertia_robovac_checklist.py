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
from src.eufyhome.method.app.User_Page import UserPage
from src.eufyhome.method.app.TimeZone_page import TimeZonePage
from src.eufyhome.method.app.System_Page import SystemPage
from src.eufyhome.method.app.Start_page import StartPage
from src.eufyhome.method.app.News_Page import NewsPage
from src.eufyhome.method.app.ChangePW_Page import ChangePWPage
from src.eufyhome.method.app.AllShare_Page import AllSharePage

from src.eufyhome.method.robotic.RoboticCleanModel_Page import RoboticCleanModelPage
from src.eufyhome.method.robotic.RoboticFind_Page import RoboticFindPage
from src.eufyhome.method.robotic.RoboticHome_Page import RoboticHomePage
from src.eufyhome.method.robotic.RoboticSetting_Page import RoboticSettingPage
from src.eufyhome.method.robotic.RoboticSuction_Page import RoboticSuctionPage
from src.eufyhome.method.robotic.RoboticVoice_Page import RoboticVoicePage
from src.eufyhome.method.robotic.RoboticSchedule_Page import RoboticSchedulePage
from src.eufyhome.method.robotic.RoboticUpdate_Page import RoboticUpdatePage
from src.eufyhome.method.robotic.RoboticMaintence_Page import RoboticMaintencePage
from src.eufyhome.method.robotic.RoboticCleanSetting_Page import RoboticCleanSettingPage
from src.eufyhome.method.robotic.RoboticUnit_Page import RoboticUnitPage
from src.eufyhome.method.robotic.RoboticZoneClean_Page import RoboticZoneCleanPage
from src.eufyhome.method.robotic.RoboticManual_Page import RoboticManualPage

global base_page, start_page, user_page, time_zone_page, system_page, news_page, change_pw_page, home_page, \
            all_share_page, robotic_find_page, robotic_home_page, robotic_setting_page, robotic_suction_page,\
            robotic_voice_page, help_faq_page, robotic_clean_model_page, share_setting_page, add_device_page, \
            device_help_page, robotic_schedule_page, robotic_update_page, robotic_maintence_page, robotic_cleansetting_Page, \
            robotic_unit_page, robotic_zone_clean_page, robotic_manual_page


# @pytest.mark.flaky(reruns=0)  # 失败重跑
@pytest.mark.repeat(0)  # 重复执行次数
@pytest.mark.usefixtures('driver_setup')  # 引用conftest.py中的driver_setup方法，创建会话
@pytest.mark.usefixtures('appium_setup')  # 引用conftest.py中的appium_setup方法，启动appium服务
class TestInertiaRoBoVac(object):
    @pytest.fixture(scope='function')
    def init_setup(self):
        """
        使用 @pytest.fixture(scope='function') 装饰器的方法可以看做是setup方法
        scope指定级别，取值可以是"function"(default),"class","module","package" or "session"
        :return:
        """
        global base_page, start_page, user_page, time_zone_page, system_page, news_page, change_pw_page, home_page, \
            all_share_page, robotic_find_page, robotic_home_page, robotic_setting_page, robotic_suction_page,\
            robotic_voice_page, help_faq_page, robotic_clean_model_page, share_setting_page, add_device_page, \
            device_help_page, robotic_schedule_page, robotic_update_page, robotic_maintence_page, robotic_cleansetting_Page, \
            robotic_unit_page, robotic_zone_clean_page, robotic_manual_page

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

        robotic_find_page = RoboticFindPage(self.driver)
        robotic_home_page = RoboticHomePage(self.driver)
        robotic_setting_page = RoboticSettingPage(self.driver)
        robotic_suction_page = RoboticSuctionPage(self.driver)
        robotic_voice_page = RoboticVoicePage(self.driver)
        robotic_clean_model_page = RoboticCleanModelPage(self.driver)
        robotic_schedule_page = RoboticSchedulePage(self.driver)
        robotic_update_page = RoboticUpdatePage(self.driver)
        robotic_maintence_page = RoboticMaintencePage(self.driver)
        robotic_cleansetting_Page = RoboticCleanSettingPage(self.driver)
        robotic_unit_page = RoboticUnitPage(self.driver)
        robotic_zone_clean_page = RoboticZoneCleanPage(self.driver)
        robotic_manual_page = RoboticManualPage(self.driver)

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
                TestInertiaRoBoVac.change_account(account)
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

    @pytest.fixture(scope='function')
    def delete_share_news(self):
        """
        删除被分享人消息列表的通知
        :return:
        """
        yield 1
        if GlobalVar.get_test_flag():
            base_page.kill_app()
            base_page.open_app()
            home_page.into_system()
            system_page.into_news()
            news_page.clear_all()
            news_page.yes
            time.sleep(2.5)

    @staticmethod
    def inertia_ready():
        robotic_home_page.skip_robotic_guide()
        if robotic_home_page.is_offline:
            robotic_home_page.ok
            if robotic_home_page.robovac_is_offline() is False:
                assert False, 'inertia_robotic 设备处于离线状态'
        robotic_home_page.ingore_update_languge()

    # ********************惯导扫地机用例************************** #
    @pytest.mark.robovac
    @pytest.mark.inertiarobotic
    @pytest.mark.run(order=300)
    @pytest.mark.parametrize('check_account', ['inertia_robotic'], indirect=True)
    def inertia_robotic_check_update_icon(self, check_account):
        """
        设备升级提示图标检查:
        1. app首页点击进入设备主页
        【checkpoint】首页设备列表是否显示升级图标
        :param check_account:
        :return:
        """
        home_page.swipe_page('down')
        assert home_page.have_update_icon(data.get_device('inertia_robotic')), 'inertia_robotic 未显示升级图标'

        home_page.click_update_icon(data.get_device('inertia_robotic'))
        assert home_page.text_display('Firmware Update'), 'inertia_robotic OTA升级快捷入口进入失败'

    @pytest.fixture(scope='function')
    def stop_inertia_robotic(self):
        """
        停止清扫
        :return:
        """
        yield 1
        try:
            robotic_home_page.ok
        except Exception as e:
            print(e)
            pass
        if data.get_robotic_status('standard') != robotic_home_page.read_robovac_status():
            robotic_home_page.t2250_play()

    @pytest.mark.robovac
    @pytest.mark.inertiarobotic
    @pytest.mark.run(order=302)
    @pytest.mark.parametrize('check_account', ['inertia_robotic'], indirect=True)
    @pytest.mark.flaky(reruns=2, reruns_delay=40)
    def test_inertia_robotic_play(self, check_account, stop_inertia_robotic):
        """
        惯性扫地机清扫启动/暂停：
        1. 点击激光扫地机进入扫地机主页
        2. 点击清扫按钮，检查扫地机状态
        【checkpoint】启动扫地机后设备状态变更为：Cleaning   （添加按钮图片的判断）
        3. 再次点击清扫按钮，检查扫地机状态
        【checkpoint】停止清扫后扫地机状态变为：standard   （添加按钮图片的判断）
        :param check_account:
        :return:
        """

        home_page.into_device_home_page(data.get_device('inertia_robotic'))

        TestInertiaRoBoVac.inertia_ready()

        # robotic_home_page.skip_robotic_guide()
        # if robotic_home_page.is_offline:
        #     robotic_home_page.ok
        #     if robotic_home_page.robovac_is_offline() is False:
        #         assert False, 'inertia_robotic 设备处于离线状态'
        #
        # robotic_home_page.ingore_update_languge()

        # 解决首次进入无法操作问题
        robotic_home_page.back_home()
        home_page.into_device_home_page(data.get_device('inertia_robotic'))

        robotic_home_page.t2250_play()
        time.sleep(8)
        robotic_home_page.swipe_page('down')
        assert robotic_home_page.read_robovac_status() == data.get_robotic_status('cleaning'), 'inertia_robotic 扫地机启动清扫失败'
        assert 'Pause' in robotic_home_page.read_clean_btn_status(), 'inertia_robotic 扫地机清扫按钮启动状态未切换'
        robotic_home_page.back_home()
        home_page.swipe_page('down')
        assert home_page.read_device_status(data.get_device('inertia_robotic')) == 'Cleaning', 'inertia_robotic 扫地机启动清扫后列表开关状态显示错误'

        home_page.click_device_btn(data.get_device('inertia_robotic'))
        time.sleep(8)
        robotic_home_page.swipe_page('down')
        assert home_page.read_device_status(data.get_device('inertia_robotic')) == 'Standby', 'inertia_robotic 扫地机停止清扫后列表开关状态显示错误'
        home_page.into_device_home_page(data.get_device('inertia_robotic'))
        assert 'Clean' in robotic_home_page.read_clean_btn_status(), 'inertia_robotic 扫地机清扫按钮暂停状态未切换'
        assert robotic_home_page.read_robovac_status() == data.get_robotic_status('standard'), 'inertia_robotic随机扫地机暂停清扫失败'

    @pytest.mark.robovac
    @pytest.mark.inertiarobotic
    @pytest.mark.run(order=303)
    @pytest.mark.parametrize('check_account', ['inertia_robotic'], indirect=True)
    @pytest.mark.flaky(reruns=2, reruns_delay=40)
    def test_inertia_robotic_standby_spot(self, check_account, stop_inertia_robotic):
        """
        惯性扫地机定点清扫:
        1. 点击惯性扫地机进入扫地机主页
        2. 点击spot按钮
        【checkpoint】设备状态变为spot
        【checkpoint】开始清扫按钮文案变为pause
        3. 点击charging ，等待回充完毕，点击 spot
        【checkpoint】弹窗提示设备充电中无法启动定点清扫
        :param check_account:
        :return:
        """
        home_page.into_device_home_page(data.get_device('inertia_robotic'))

        TestInertiaRoBoVac.inertia_ready()

        if robotic_home_page.read_robovac_status() == data.get_robotic_status('charging'):
            robotic_home_page.t2250_play()
            time.sleep(5)
            robotic_home_page.t2250_play()

        robotic_home_page.t2250_spot()
        time.sleep(10)
        status = data.get_robotic_status('cleaning') in robotic_home_page.read_robovac_status()
        btn = 'Stop' in robotic_home_page.read_clean_btn_status()
        assert status and btn, 'inertia_robotic扫地机定点清扫状态显示:'+str(status)+',定点清扫开启后开关状态显示:'+str(btn)

    @pytest.mark.robovac
    @pytest.mark.inertiarobotic
    @pytest.mark.run(order=304)
    @pytest.mark.parametrize('check_account', ['inertia_robotic'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def test_inertia_robotic_ischarging_spot(self, check_account, stop_inertia_robotic):
        """
        惯性扫地机充电中定点清扫：
        1. 点击惯性扫地机进入扫地机主页
        2. 点击charging ，等待回充完毕，点击 spot
        【checkpoint】弹窗提示设备充电中无法启动定点清扫
        :param check_account:
        :param end_spot:
        :return:
        """
        home_page.into_device_home_page(data.get_device('inertia_robotic'))

        TestInertiaRoBoVac.inertia_ready()

        status = robotic_home_page.read_robovac_status()
        GlobalVar.set_test_flag('t')

        if status == data.get_robotic_status('standard') or status == data.get_robotic_status('cleaning'):
            robotic_home_page.t2250_charge()
            times = 1
            flag = False
            while times <= 20:
                times = times + 1
                _ac = robotic_home_page.read_robovac_status()
                if data.get_robotic_status('charging') in _ac:
                    flag = True
                    break
                else:
                    robotic_home_page.long_wait(10)
            assert flag, 'inertia_robotic前置条件失败，用例不执行'

        robotic_home_page.t2250_spot()
        assert robotic_home_page.text_display('Please place the RoboVac outside the charging base to start Spot cleaning.'), \
        'inertia_robotic设备充电中点击spot未显示正确提示'

    @pytest.mark.robovac
    @pytest.mark.inertiarobotic
    @pytest.mark.run(order=305)
    @pytest.mark.parametrize('check_account', ['inertia_robotic'], indirect=True)
    @pytest.mark.flaky(reruns=2, reruns_delay=40)
    def test_inertia_robotic_change_suctions(self, check_account):
        """
        惯性扫地机4种吸力模式修改:
        1. 点击惯性扫地机进入扫地机主页，点击 clean
        2. 分别点击选择stangard、max、turbo、boostiq
        【checkpoint】根据元素相对位置检查勾的位置
        :param check_account:
        :return:
        """
        home_page.into_device_home_page(data.get_device('inertia_robotic'))

        TestInertiaRoBoVac.inertia_ready()

        robotic_home_page.t2250_suction()

        robotic_suction_page.t2250_standard()
        standard = robotic_suction_page.t2250_is_standard()
        robotic_suction_page.add_check_image('standard吸力模式')

        robotic_suction_page.t2250_turbo()
        turbo = robotic_suction_page.t2250_is_turbo()
        robotic_suction_page.add_check_image('turbo吸力模式')

        robotic_suction_page.t2250_max()
        max = robotic_suction_page.t2250_is_max()
        robotic_suction_page.add_check_image('max吸力模式')

        robotic_suction_page.t2250_boostiq()
        boostiq = robotic_suction_page.t2250_is_boostiq()
        robotic_suction_page.add_check_image('boostiq吸力模式')

        assert standard and turbo and max and boostiq, 'inertia_robotic 吸力修改失败::standard='+str(standard)+' turbo='+str(turbo)+' max='+str(max)+' boostiq='+str(boostiq)

    @pytest.fixture(scope='function')
    def inertia_robotic_charging(self):
        """
        回充的后置操作：恢复为standard状态
        :return:
        """
        yield 1
        if GlobalVar.get_test_flag():  # 设备离线时不执行
            status = robotic_home_page.read_robovac_status()
            if status in [data.get_robotic_status('cleaning'), data.get_robotic_status('backing')]:
                robotic_home_page.t2250_play()

    @pytest.mark.robovac
    @pytest.mark.inertiarobotic
    @pytest.mark.run(order=308)
    @pytest.mark.parametrize('check_account', ['inertia_robotic'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def test_inertia_robotic_standard_recharge(self, check_account, inertia_robotic_charging):
        """
        惯导扫地机不再充电座回充：
        1. 点击惯性扫地机进入扫地机主页
        2. 点击 charge 按钮
        【checkpoint】扫地机回充显示toast：Heading Home
        【checkpoint】扫地机状态显示：状态显示为 Heading Home 或者 Charging
        :return:
        """
        home_page.into_device_home_page(data.get_device('inertia_robotic'))

        TestInertiaRoBoVac.inertia_ready()

        status0 = robotic_home_page.read_robovac_status()
        GlobalVar.set_test_flag('t')

        if status0 == data.get_robotic_status('charging'):
            robotic_home_page.t2250_play()
            time.sleep(3)
            robotic_home_page.t2250_play()
        elif status0 == data.get_robotic_status('cleaning'):
            robotic_home_page.t2250_play()

        robotic_home_page.t2250_charge()
        robotic_home_page.add_check_image('standard模式回充')
        # toast = robotic_home_page.is_toast_exist('Heading Home', True, True)
        status = robotic_home_page.read_robovac_status() in [data.get_robotic_status('backing'), data.get_robotic_status('charging')]
        assert status, 'inertia_robotic 在standby状态下回充中状态显示:' + str(status)
        if status == data.get_robotic_status('charging'):
            return
        times = 1
        while times < 10:
            times = times + 1
            _ac = robotic_home_page.read_robovac_status()
            if _ac in [data.get_robotic_status('charging'), data.get_robotic_status('standard')]:
                break
            else:
                time.sleep(10)
        robotic_home_page.add_check_image('standard模式回充结果')

    @pytest.mark.robovac
    @pytest.mark.inertiarobotic
    @pytest.mark.run(order=309)
    @pytest.mark.parametrize('check_account', ['inertia_robotic'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def test_inertia_robotic_iscleaning_recharge(self, check_account, inertia_robotic_charging):
        """
        惯性扫地机清扫过程中点击回充按钮:
        1. 点击惯性扫地机进入扫地机主页,点击清扫使扫地机状态为cleaning
        2. 点击 charge 按钮
        【checkpoint】扫地机回充显示toast：Heading Home  #  android无法读取
        【checkpoint】等待5min，每分钟检查一次扫地机状态显示：Heading Home
        :param random_robotic_charge:
        :return:
        """
        home_page.into_device_home_page(data.get_device('inertia_robotic'))

        TestInertiaRoBoVac.inertia_ready()

        for k in range(3):
            if robotic_home_page.read_robovac_status() == data.get_robotic_status('cleaning'):
                GlobalVar.set_test_flag('t')
                break
            else:
                robotic_home_page.t2250_play()
                time.sleep(5)
            if k == 3:
                assert False, 'inertia_robotic 启动清扫失败'

        robotic_home_page.t2250_charge()
        time.sleep(5)
        assert robotic_home_page.text_display('Stop cleaning and head home?'), 'inertia_robotic 没有显示终断清扫的弹窗'
        robotic_home_page.sure_charge()
        robotic_home_page.add_check_image('cleaning模式回充')
        status = robotic_home_page.read_robovac_status() in [data.get_robotic_status('backing'), data.get_robotic_status('charging')]
        assert status, 'inertia_robotic 在cleaning状态回充状态显示:' + str(status)
        if status == data.get_robotic_status('charging'):
            return
        times = 1
        while times < 10:
            times = times + 1
            _ac = robotic_home_page.read_robovac_status()
            if data.get_robotic_status('charging') in _ac:
                break
            else:
                time.sleep(10)
        robotic_home_page.add_check_image('cleaning模式回充结果')

    @pytest.mark.robovac
    @pytest.mark.inertiarobotic
    @pytest.mark.run(order=310)
    @pytest.mark.parametrize('check_account', ['inertia_robotic'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def test_inertia_robotic_ischarging_recharge(self, check_account, inertia_robotic_charging):
        """
        惯性扫地机充电中点击回充按钮:
        1. 点击随机扫地机进入扫地机主页
        【checkpoint】扫地机状态为charging
        2. 点击 charge 按钮
        【checkpoint】toast提示充电中
        :param check_account:
        :param random_robotic_charge:
        :return:
        """
        home_page.into_device_home_page(data.get_device('inertia_robotic'))

        TestInertiaRoBoVac.inertia_ready()

        status = robotic_home_page.read_robovac_status()
        GlobalVar.set_test_flag('t')

        if status in [data.get_robotic_status('standard'), data.get_robotic_status('cleaning')]:
            times = 1
            flag = False
            while times < 20:
                times = times + 1
                _ac = robotic_home_page.read_robovac_status()
                if data.get_robotic_status('charging') in _ac:
                    flag = True
                    break
                else:
                    robotic_home_page.t2250_charge()
                    time.sleep(10)
            assert flag, 'inertia_robotic前置条件失败，用例不执行'

        robotic_home_page.t2250_charge()
        assert robotic_home_page.is_toast_exist('Charging', True, True), 'inertia_robotic在charging状态点击回充未显示toast'

    @pytest.mark.robovac
    @pytest.mark.inertiarobotic
    @pytest.mark.run(order=311)
    @pytest.mark.parametrize('check_account', ['inertia_robotic'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def test_inertia_robotic_ischarging_find(self, check_account, inertia_robotic_charging):
        """
        充电状态点击find按钮:
        1. 点击随机扫地机进入扫地机主页，进入setting界面，点击 find 按钮
        2.点击 start 按钮
        【checkpoint】toast提示：Charging
        :param check_account:
        :return:
        """
        home_page.into_device_home_page(data.get_device('inertia_robotic'))

        TestInertiaRoBoVac.inertia_ready()

        status = robotic_home_page.read_robovac_status()
        if status in [data.get_robotic_status('standard'), data.get_robotic_status('cleaning')]:
            robotic_home_page.t2250_charge()
            times = 1
            flag = False
            while times < 20:
                times = times + 1
                _ac = robotic_home_page.read_robovac_status()
                if data.get_robotic_status('charging') in _ac:
                    flag = True
                    break
                else:
                    time.sleep(10)
            assert flag, 'inertia_robotic 前置条件失败，用例不执行'

        robotic_home_page.into_setting(True)
        robotic_setting_page.into_find()
        robotic_find_page.click_find('inertia')
        assert robotic_find_page.check_find_img('inertia', 't2250_find_start'), 'inertia_robotic 在charging状态点击find不会启动寻找'

    @pytest.mark.robovac
    @pytest.mark.inertiarobotic
    @pytest.mark.run(order=312)
    @pytest.mark.parametrize('check_account', ['inertia_robotic'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def test_inertia_robotic_manual_find(self, check_account):
        """
        惯性扫地机find手动开始/停止测试:
        1. 点击随机扫地机进入扫地机主页，点击 find 按钮
        2. 点击 start 按钮
        【checkpoint】点击后按钮文案变为stoped
        3. 点击stop停止蜂鸣
        【checkpoint】点击stoped后按钮变为start
        :param check_account:
        :return:
        """
        home_page.into_device_home_page(data.get_device('inertia_robotic'))

        TestInertiaRoBoVac.inertia_ready()

        status = robotic_home_page.read_robovac_status()
        if status == data.get_robotic_status('charging'):
            robotic_home_page.t2250_play()
            time.sleep(5)
            robotic_home_page.t2250_play()

        robotic_home_page.into_setting(True)
        robotic_setting_page.into_find()
        robotic_find_page.click_find('inertia')
        time.sleep(3)
        assert robotic_find_page.check_find_img('inertia', 't2250_find_stop'), 'inertia_robotic 手动启动find me失败'
        robotic_find_page.click_find('inertia')
        time.sleep(3)
        assert robotic_find_page.check_find_img('inertia', 't2250_find_start'), 'inertia_robotic 手动停止find me失败'

    @pytest.mark.robovac
    @pytest.mark.inertiarobotic
    @pytest.mark.run(order=313)
    @pytest.mark.parametrize('check_account', ['inertia_robotic'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def test_inertia_robotic_find_timeout(self, check_account):
        """
        惯性扫地机find蜂鸣时间测试：
        1. 点击惯性扫地机进入扫地机主页，点击 find 按钮
        2.点击start设备开始蜂鸣
        【checkpoint】点击find启动后按钮变为stoped
        3.等待65s
        【checkpoint】扫地机find蜂鸣i1min后自动结束，按钮变为start
        :param check_account:
        :return:
        """
        home_page.into_device_home_page(data.get_device('inertia_robotic'))

        TestInertiaRoBoVac.inertia_ready()

        status = robotic_home_page.read_robovac_status()
        if status == data.get_robotic_status('charging'):
            robotic_home_page.t2250_play()
            time.sleep(5)
            robotic_home_page.t2250_play()

        robotic_home_page.into_setting(True)
        robotic_setting_page.into_find()
        robotic_find_page.click_find('inertia')

        assert robotic_find_page.check_find_img('inertia', 't2250_find_stop'), 'inertia_robotic未正常启动find功能'
        robotic_find_page.long_wait(70)
        assert robotic_find_page.check_find_img('inertia', 't2250_find_start'), 'inertia_robotic 设备find me蜂鸣未在1分钟内结束'

    @pytest.mark.robovac
    @pytest.mark.inertiarobotic
    @pytest.mark.run(order=314)
    @pytest.mark.parametrize('check_account', ['inertia_robotic'], indirect=True)
    @pytest.mark.parametrize('email,expect', [('a@a', 'Please enter a valid email address')])
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def test_inertia_robotic_share_error_email(self, email, expect, check_account):
        """
        惯性扫地机分享给错误格式账号:
        1. 点击惯性扫地机进入扫地机主页，点击 more进入设置界面，点击share setting进入分享列表
        2. 点击 add 按钮进入添加界面，输入分享账号：a@a并提交
        【checkpoint】分享失败，toast提示：Please enter a vailed email adress
        :return:
        """
        home_page.into_device_home_page(data.get_device('inertia_robotic'))

        TestInertiaRoBoVac.inertia_ready()

        robotic_home_page.into_setting(True)
        robotic_setting_page.into_share()
        share_setting_page.add_share()
        share_setting_page.commit_share(email)

        if share_setting_page.platform == 'ios':
            flag = share_setting_page.text_display('Add Member')
        else:
            flag = share_setting_page.text_display(expect)
        assert flag, 'inertia_robotic 分享错误邮箱的结果异常'

    @pytest.mark.robovac
    @pytest.mark.inertiarobotic
    @pytest.mark.run(order=315)
    @pytest.mark.parametrize('check_account', ['inertia_robotic'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def test_inertia_robotic_share_nosign_email(self, check_account):
        """
        惯性扫地机分享给未注册的账号:
        1. 点击惯性扫地机进入扫地机主页，点击 more进入设置界面，点击share setting进入分享列表
        2. 点击 add 按钮进入添加界面，输入分享账号：a@a.com并提交
        【checkpoint】分享失败，弹窗提示：Failed to share
        :return:
        """
        home_page.into_device_home_page(data.get_device('inertia_robotic'))

        TestInertiaRoBoVac.inertia_ready()

        robotic_home_page.into_setting(True)
        robotic_setting_page.into_share()
        share_setting_page.add_share()
        share_setting_page.commit_share('abc@test.com')
        assert share_setting_page.share_result() is False, 'inertia_robotic分享失败的提示错误'

    @pytest.fixture(scope='function')
    def delete_refuse_share_account(self):
        """
        先删除refuseshare账号分享列表
        :return:
        """
        home_page.into_system()
        system_page.into_sharing()
        all_share_page.into_device(data.get_device('inertia_robotic'))
        share_setting_page.delete_share()
        all_share_page.kill
        time.sleep(2)
        all_share_page.open

    @pytest.mark.robovac
    @pytest.mark.inertiarobotic
    @pytest.mark.run(order=316)
    @pytest.mark.parametrize('check_account', ['inertia_robotic'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def test_inertia_robotic_share_email(self, check_account, delete_refuse_share_account):
        """
        惯性扫地机分享给已注册的账号：
        1. 点击惯性扫地机进入扫地机主页，点击 more进入设置界面，点击share setting进入分享列表
        2. 点击 add 按钮进入添加界面，输入分享账号：Yi@aa.com并提交
        【checkpoint】 分享邀请发送成功，弹窗提示：Successed to share
        【checkpoint】页面返回到分享列表并显示分享人，状态为：待确认
        :param check_account:
        :return:
        """
        home_page.into_device_home_page(data.get_device('inertia_robotic'))

        TestInertiaRoBoVac.inertia_ready()

        robotic_home_page.into_setting(True)
        robotic_setting_page.into_share()
        share_setting_page.add_share()
        share_setting_page.commit_share(data.get_account('share'))

        assert share_setting_page.share_result(), 'inertia_robotic正确账号分享失败'
        share_setting_page.ok
        share_setting_page.loading()
        status = share_setting_page.read_share_status(data.get_username('share'))
        assert status == 'Awaiting Confirmation' or status == 'Pending Confirmation', '分享列表被分享者状态显示错误'

    @pytest.mark.robovac
    @pytest.mark.inertiarobotic
    @pytest.mark.run(order=317)
    @pytest.mark.parametrize('check_account', ['inertia_robotic'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def test_inertia_robotic_agree_share(self, check_account, delete_share_news):
        """
        惯导扫地机被分享者接受分享:
        1. 登陆账号Yi@aa. com/12345678
        【checkpoint】检查是否显示了分享设备
        2. 点击进入侧边栏界面
        【checkpoint】android消息通知显示分享通知红点标识
        3. 点击news进入消息界面
        【checkpoint】显示分享邀请消息记录
        4. 点击最新一条分享邀请通知，点击ok按钮
        【checkpoint】确认分享设备名称是否正确
        【checkpoint】进入消息通知显示拒绝/确认两个按钮,点击ok按钮弹窗提示分享成功
        :param check_account:
        :return:
        """
        home_page.into_device_home_page(data.get_device('inertia_robotic'))

        TestInertiaRoBoVac.inertia_ready()

        robotic_home_page.into_setting(True)
        robotic_setting_page.into_share()
        status = share_setting_page.read_share_status(data.get_username('share'))
        if status not in ['Awaiting Confirmation', 'Pending Confirmation']:
            share_setting_page.add_share()
            share_setting_page.commit_share(data.get_account('share'))
            assert share_setting_page.share_result(), 'inertia_robotic正确账号分享失败,无法执行用例:[id=35]'
            share_setting_page.ok
            share_setting_page.loading()

        share_setting_page.back_setting()
        robotic_setting_page.back_robovac()
        robotic_home_page.back_home()
        TestInertiaRoBoVac.change_account('share')
        home_page.into_system()

        system_page.into_sharing()
        assert all_share_page.text_display(data.get_device('inertia_robotic')), '被分享列表未显示分享设备信息'
        GlobalVar.set_test_flag('t')  # 到这里后需要执行 tear_down
        all_share_page.into_device(data.get_device('inertia_robotic'))
        all_share_page.yes
        all_share_page.loading()

        assert news_page.text_display('Request Accepted. You may now use this device.'), '被分享者确认接受分享失败'
        news_page.ok
        assert news_page.text_display('robotic shared a '+data.get_device('inertia_robotic').strip()), '被分享者显示的分享设备名称错误'

        news_page.back_system()
        news_page.back_system()
        system_page.back_home()
        home_page.swipe_page('down')
        assert home_page.find_device(data.get_device('inertia_robotic')), '被分享者未显示分享的扫地机设备'

    @pytest.fixture(scope='function')
    def t2250_close_yellow_tip(self):
        """
        关闭小黄条提示
        :return:
        """
        yield 1
        if GlobalVar.get_test_flag():
            robotic_schedule_page.close_yellow_tip()

    @pytest.mark.robovac
    @pytest.mark.inertiarobotic
    @pytest.mark.run(order=318)
    @pytest.mark.parametrize('check_account', ['share'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def inertia_robotic_yellow_tip(self, t2250_close_yellow_tip, check_account):
        """
        惯导扫地机被分享者修改设备名及小黄条显示:
        1. app首页点击进入设备主页，修改一个定时任务
        2.切换账号 Yi@aaa.com，查看随机扫地机设备
        【checkpoint】显示设备名称修改小黄条
        :return:
        """
        if home_page.find_device(data.get_device('inertia_robotic')) is False:
            assert False, '未查找到分享设备，无法执行用:[test_inertia_robotic_yellow_tip]'

        home_page.into_device_home_page(data.get_device('inertia_robotic'))

        TestInertiaRoBoVac.inertia_ready()

        robotic_home_page.t2250_schedule()
        robotic_schedule_page.t2250_click_schedues_btn()
        robotic_schedule_page.back_robotic()
        robotic_home_page.back_home()

        TestInertiaRoBoVac.change_account('inertia_robotic')

        home_page.into_device_home_page(data.get_device('inertia_robotic'))
        if robotic_home_page.is_offline:
            robotic_home_page.ok
            if robotic_home_page.robovac_is_offline() is False:
                assert False, 'inertia_robotic 设备处于离线状态'

        GlobalVar.set_test_flag('t')
        robotic_home_page.ingore_update_languge()

        robotic_home_page.t2250_schedule()
        assert robotic_schedule_page.text_display('share modified the schedule'), 'inertia_robotic 被分享人修改了定时任务未显示小黄条提示'

    @pytest.mark.robovac
    @pytest.mark.inertiarobotic
    @pytest.mark.run(order=319)
    @pytest.mark.parametrize('check_account', ['share'], indirect=True)
    def test_inertia_robotic_delete_share(self, check_account):
        """
        惯导扫地机被分享者移除分享设备:
        1. app首页点击进入设备主页，点击更多，点击删除设备
        【checkpoint】弹窗提示确认移除
        2.点击 ok 按钮
        【checkpoint】分享者列表不显示被分享人信息
        3.切换账号Yi@aaa。com，查看设备分享列表
        【checkpoint】分享者列表不显示被分享人信息
        :return:
        """
        home_page.swipe_page('down')
        assert home_page.find_device(data.get_device('inertia_robotic')), '未查找到分享设备，无法执行用:[test_inertia_robotic_delete_share]'

        home_page.into_device_home_page(data.get_device('inertia_robotic'))

        TestInertiaRoBoVac.inertia_ready()

        robotic_home_page.into_setting(True)
        robotic_home_page.swipe_page('up')
        robotic_setting_page.click_remove()
        assert robotic_setting_page.text_display('Are you sure you want to remove this device?'), '未显示移除确认弹窗'
        robotic_setting_page.commit_remove()
        home_page.swipe_page('down')
        assert home_page.find_device(data.get_device('inertia_robotic')) is False, '被分享着移除后设备未删除'

        TestInertiaRoBoVac.change_account('inertia_robotic')

        home_page.into_device_home_page(data.get_device('inertia_robotic'))
        if robotic_home_page.is_offline:
            robotic_home_page.ok
            if robotic_home_page.robovac_is_offline() is False:
                assert False, 'inertia_robotic 设备处于离线状态'

        robotic_home_page.ingore_update_languge()
        robotic_home_page.into_setting(True)
        robotic_setting_page.into_share()
        assert data.get_username('share') not in share_setting_page.read_share_to_me_list(), '分享列表显示已移除的分享者信息'

    @pytest.mark.robovac
    @pytest.mark.inertiarobotic
    @pytest.mark.run(order=320)
    @pytest.mark.parametrize('check_account', ['inertia_robotic'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def test_inertia_robotic_refuse_share(self, delete_share_news, check_account, delete_refuse_share_account):
        """
        惯导扫地机被分享者拒绝接受分享：
        1. 点击惯导扫地机进入扫地机主页，点击 more进入设置界面，点击share setting进入分享列表
        2. 点击 add 按钮进入添加界面，输入分享账号：Yi@aa.com并提交
        【checkpoint】 分享邀请发送成功，弹窗提示：Successed to share
        3.重启app切换账号Yi@aa.com，进入分享消息记录
        4.点击拒绝接受分享按钮
        【checkpoint】显示已拒绝分享弹窗
        【chenckpoint】app首页不显示分享设备
        :param check_account:
        :return:
        """
        home_page.into_device_home_page(data.get_device('inertia_robotic'))

        TestInertiaRoBoVac.inertia_ready()

        robotic_home_page.into_setting(True)
        robotic_setting_page.into_share()
        share_setting_page.add_share()
        share_setting_page.commit_share(data.get_account('refuseshare'))
        assert share_setting_page.share_result(), 'inertia_robotic 正确账号分享失败'
        share_setting_page.ok
        share_setting_page.loading()

        share_setting_page.back_setting()
        robotic_setting_page.back_robovac()
        robotic_home_page.back_home()

        TestInertiaRoBoVac.change_account('refuseshare')
        GlobalVar.set_test_flag('t')

        home_page.into_system()
        system_page.into_sharing()
        all_share_page.into_device(data.get_device('inertia_robotic'))
        all_share_page.no
        assert all_share_page.text_display('Request Declined. This device will be removed.'), 'inertia_robotic被分享者拒绝接受分享失败'
        all_share_page.ok
        all_share_page.loading()

        all_share_page.back_system()
        system_page.back_home()
        home_page.swipe_page('down')
        assert home_page.find_device(data.get_device('inertia_robotic')) is False, 'app首页被分享者拒绝分享后显示分享了扫地机设备'

    # @pytest.mark.debug
    # @pytest.mark.inertiarobotic
    # @pytest.mark.run(order=321)
    # @pytest.mark.parametrize('check_account', ['inertia_robotic'], indirect=True)
    # def inertia_robotic_change_voice(self, check_account):
    #     """
    #     1. 点击惯性扫地机进入扫地机主页，点击more进入设置
    #     2. 点击 voice setting进入语音设置，将声音图标滑动到最左侧
    #     【checkpoint】音量显示变为：The device is Muted.
    #     3. 将声音值滑到最右侧
    #     【checkpoint】音量显示变为：100%
    #     :param check_account:
    #     :return:
    #     """
    #     home_page.into_device_home_page(data.get_device('inertia_robotic'))
    #     TestInertiaRoBoVac.inertia_ready()
    #
    #     robotic_home_page.into_setting(True)
    #     robotic_setting_page.into_voice()
    #     robotic_voice_page.change_voice(0.9)
    #     time.sleep(3)
    #     voice0 = robotic_voice_page.read_voice_value()
    #     assert '90%' in voice0, 'inertia_robotic 扫地机音量调节失败'
    #
    #     robotic_voice_page.change_voice(0)
    #     time.sleep(3)
    #     voice1 = robotic_voice_page.read_voice_value()
    #     assert 'The device is Muted.' in voice1, 'inertia_robotic 关闭扫地机声音失败'

    @pytest.mark.robovac
    @pytest.mark.inertiarobotic
    @pytest.mark.run(order=322)
    @pytest.mark.parametrize('check_account', ['inertia_robotic'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def test_inertia_robotic_check_schedule_icon(self, check_account):
        """
        检查定时任务图标是否显示：
        1.进入app主页，检查是否显示定时任务图标
        2.如果未显示则去开启一个定时任务，并返回app首页
        【checkpoint】检查设备是否显示定时任务图标
        :return:
        """
        home_page.swipe_page('down')
        status = home_page.have_schedule_icon(data.get_device('inertia_robotic'))

        if not status:
            home_page.into_device_home_page(data.get_device('inertia_robotic'))
            TestInertiaRoBoVac.inertia_ready()

            robotic_home_page.t2250_schedule()
            robotic_schedule_page.t2250_change_schedule_status('on')
            robotic_schedule_page.back_robotic()
            robotic_home_page.back_home()
            home_page.swipe_page('down')
            status = home_page.have_schedule_icon(data.get_device('inertia_robotic'))

        assert status, 'inertia_robotic 未显示定时任务图标'

        home_page.click_schedule_icon(data.get_device('inertia_robotic'))
        assert home_page.text_display('Schedules'), 'inertia_robotic 定时任务快捷图标进入失败'

    @pytest.fixture(scope='function')
    def close_inertia_schedule(self):
        """
        关闭扫地机及定时任务
        :return:
        """
        yield 1
        if GlobalVar.get_test_flag():
            if data.get_robotic_status('cleaning') == robotic_home_page.read_robovac_status():
                robotic_home_page.t2250_play()
            robotic_home_page.t2250_schedule()
        robotic_schedule_page.t2250_click_schedues_btn(robotic_schedule_page.week_id)

    @pytest.mark.run(order=323)
    @pytest.mark.robovac
    @pytest.mark.parametrize('check_account', ['inertia_robotic'], indirect=True)
    def test_inertia_robotic_schedule_time(self, check_account, close_inertia_schedule):
        """
        惯导扫地机设置定时任务：
        1.设置一个基于当前时间5min后的定时任务
        【checklist】检查定时任务列表的时间是否设置正确
        2.等待定时任务启动
        【checklist】检查定时任务启动后扫地机的状态
        :param check_account:
        :return:
        """
        home_page.into_device_home_page(data.get_device('inertia_robotic'))
        TestInertiaRoBoVac.inertia_ready()

        if robotic_home_page.read_robovac_status() == data.get_robotic_status('cleaning'):
            robotic_home_page.t2250_play()
        robotic_home_page.t2250_schedule()
        robotic_schedule_page.into_schedule_edit()
        _t = robotic_schedule_page.swipe_schedule_time(data.get_device('inertia_robotic'), 5)
        robotic_schedule_page.save_schedule()

        assert _t == robotic_schedule_page.read_schedule_time(robotic_schedule_page.week_name), '定时任务设置正确'
        robotic_schedule_page.back_robotic()

        GlobalVar.set_test_flag('t')  # 此处需要判断扫地机状态了

        robotic_home_page.long_wait(480)
        assert data.get_robotic_status('cleaning') in robotic_home_page.read_robovac_status(), '定时任务执行启动成功'

    @pytest.mark.robovac
    @pytest.mark.inertiarobotic
    @pytest.mark.run(order=324)
    @pytest.mark.parametrize('check_account', ['inertia_robotic'], indirect=True)
    def inertia_robotic_hlep_title(self, check_account):
        """
        惯性扫地机help列表数量统计:
        1. app首页点击进入设备主页，点击more进入设置界面，点击help
        2. 遍历help页面的问答列表
        【checkpoint】 统计help列表总数=
        【checkpoint】遍历help列表的标题是否正确
        :return:
        """
        home_page.into_device_home_page(data.get_device('inertia_robotic'))
        robotic_home_page.skip_robotic_guide()

        if robotic_home_page.is_offline:
            robotic_home_page.ok

        robotic_home_page.ingore_update_languge()
        robotic_home_page.into_setting(True)
        robotic_setting_page.swipe_page('up')
        robotic_setting_page.into_device_help()

        title_list = device_help_page.read_help_title()
        assert len(title_list) != 0, 'inertia_robotic help列表显示为空'

        # expect_list = data.read_json(data.get_device('inertia_robotic'))
        #
        # num = len(title_list) == len(expect_list)
        # flag = True
        # expect_titles = [x for x in expect_list if x not in title_list]
        # print(expect_titles)
        # actual_titles = [x for x in title_list if x not in expect_list]
        # print(actual_titles)
        # if expect_titles or actual_titles:
        #     flag = False
        #
        # assert num and flag, 'inertia_robotic help列表总数：' + str(num) + ',与预期相比缺少：' + str(
        #     expect_titles) + ',与实际相比多出：' + str(actual_titles)

    @pytest.mark.robovac
    @pytest.mark.inertiarobotic
    @pytest.mark.run(order=325)
    @pytest.mark.parametrize('check_account', ['inertia_robotic'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def inertia_robotic_help_feedback(self, check_account):
        """
        惯性扫地机help的反馈界面：
        1. app首页点击进入设备主页，点击more进入设置界面，点击help
        2.点击进入feedback页面，点击submit按钮
        【checkpoint】检查是否有toast提示：feedback field cannot be blank
        :param check_account:
        :return:
        """
        home_page.into_device_home_page(data.get_device('inertia_robotic'))
        robotic_home_page.skip_robotic_guide()

        if robotic_home_page.is_offline:
            robotic_home_page.ok

        robotic_home_page.ingore_update_languge()
        robotic_home_page.into_setting(True)
        robotic_setting_page.swipe_page('up')
        robotic_setting_page.into_device_help()

        device_help_page.into_feed_back()
        device_help_page.submit_feed_back('inertia test feedback')
        assert device_help_page.is_help_page(), 'inertia_robotic 提交反馈失败'

    @pytest.mark.robovac
    @pytest.mark.inertiarobotic
    @pytest.mark.run(order=326)
    @pytest.mark.parametrize('check_account', ['inertia_robotic'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def inertia_robotic_help_chat(self, check_account):
        """
        惯导扫地机help的chat界面:
        1. app首页点击进入设备主页，点击more进入设置界面，点击help
        2.进入chat界面，发送一条消息
        【checkpoint】页面显示是否正常
        :param check_account:
        :return:
        """
        home_page.into_device_home_page(data.get_device('inertia_robotic'))
        robotic_home_page.skip_robotic_guide()

        if robotic_home_page.is_offline:
            robotic_home_page.ok

        robotic_home_page.ingore_update_languge()
        robotic_home_page.into_setting(True)
        robotic_setting_page.swipe_page('up')
        robotic_setting_page.into_device_help()
        device_help_page.into_chat()
        assert device_help_page.text_display('Chat With Eufy'), 'inertiar_obotic 进入chat聊天界面无响应'

    @pytest.mark.robovac
    @pytest.mark.inertiarobotic
    @pytest.mark.run(order=327)
    @pytest.mark.parametrize('check_account', ['inertia_robotic'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def _inertia_robotic_help_telphone(self, check_account):
        """
        惯导扫地机help的电话界面：
        :param check_account:
        :return:
        """
        home_page.into_device_home_page(data.get_device('inertia_robotic'))
        robotic_home_page.skip_robotic_guide()

        if robotic_home_page.is_offline:
            robotic_home_page.ok

        robotic_home_page.ingore_update_languge()
        robotic_home_page.into_setting(True)
        robotic_setting_page.swipe_page('up')
        robotic_setting_page.into_device_help()
        device_help_page.into_call_us()

        us = data.get_phone('us') in device_help_page.read_phone_number('us')
        uk = data.get_phone('uk') in device_help_page.read_phone_number('uk')
        de = data.get_phone('de') in device_help_page.read_phone_number('de')
        jp = data.get_phone('jp') in device_help_page.read_phone_number('jp')
        assert us and uk and de and jp, 'inertiar_obotic 客服联系电话显示错误：us='+str(us)+';uk='+str(uk)+';de='+str(de)+';jp='+str(jp)

    @pytest.mark.robovac
    @pytest.mark.inertiarobotic
    @pytest.mark.run(order=328)
    @pytest.mark.parametrize('check_account', ['inertia_robotic'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def test_inertia_robotic_auto_clean(self, check_account):
        """
        惯性扫地机断点续扫设置：
        1. app首页点击进入设备主页，点击more进入设置界面，读取断点续扫开关状态
        2. 点击断点续扫开关，退出页面重新进入
        【checkpoint】检查断点续扫开/关状态是否变化
        :param check_account:
        :return:
        """
        home_page.into_device_home_page(data.get_device('inertia_robotic'))

        TestInertiaRoBoVac.inertia_ready()

        robotic_home_page.into_setting(True)
        robotic_setting_page.swipe_page('up')
        robotic_setting_page.into_auto_clean()
        flag0 = robotic_cleansetting_Page.check_auto_return()

        robotic_cleansetting_Page.click_auto_return()
        time.sleep(3)
        flag1 = robotic_cleansetting_Page.check_auto_return()
        robotic_cleansetting_Page.click_auto_return()
        time.sleep(3)
        flag2 = robotic_cleansetting_Page.check_auto_return()

        assert flag0 == flag2 and flag0 != flag1, 'inertia_robotic 断点续扫开/关状态显示错误'

    @pytest.fixture(scope='function')
    def set_inertia_robotic_name(self):
        """
        恢复设备名称
        :return:
        """
        yield 1
        if home_page.is_welcome():
            home_page.into_device_home_page(data.get_device('inertia_robotic'))
        if robotic_home_page.text_display('T2250'):
            robotic_home_page.into_setting(True)
        if robotic_setting_page.read_device_name() != data.get_device('inertia_robotic'):
            robotic_setting_page.change_device_name(data.get_device('inertia_robotic'))
        robotic_setting_page.back_robovac()
        robotic_home_page.t2250_charge()
        robotic_home_page.long_wait(30)

    @pytest.mark.robovac
    @pytest.mark.inertiarobotic
    @pytest.mark.run(order=329)
    @pytest.mark.parametrize('check_account', ['inertia_robotic'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def test_inertia_robotic_change_device_name(self, check_account, set_inertia_robotic_name):
        """
        修改扫地机设备名称:
        1. app首页点击进入设备主页，点击更多，修改设备名称T2123_随机数
        【checkpoint】设备控制页名称显示正确
        【checkpoint】设备主页显示名称正确
        【checkpoint】app主页设备名显示正确
        :param check_account:
        :return:
        """
        home_page.into_device_home_page(data.get_device('inertia_robotic'))

        TestInertiaRoBoVac.inertia_ready()

        robotic_home_page.into_setting(True)
        _name = data.get_device('inertia_robotic')+robotic_setting_page.get_str()

        robotic_setting_page.change_device_name(_name)
        assert _name in robotic_setting_page.read_device_name(), 'inertia_robotic 扫地机修改名称后设置页面显示的名称不对'

        robotic_setting_page.back_robovac()
        assert _name in robotic_home_page.read_t2250_name(), 'inertia_robotic 扫地机修改名称后设备主页面显示的名称不对'

        robotic_home_page.back_home()
        home_page.swipe_page('down')
        assert home_page.find_device(_name), 'inertia_robotic 扫地机修改名称后app主页面显示的名称不对'

    @pytest.mark.robovac
    @pytest.mark.inertiarobotic
    @pytest.mark.run(order=330)
    @pytest.mark.parametrize('check_account', ['inertia_robotic'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def test_inertia_robotic_remove(self, check_account):
        """
        移除惯性扫地机设备：
        1. app首页点击进入设备主页，点击more进入设置界面
        2. 点击remove
        【checkpoint】弹出移除成功确认弹窗
        【checkpoint】返回app首页，设备列表不显示T2250
        :param check_account:
        :return:
        """
        if GlobalVar.get_remove_add() == 0:
            pytest.skip('本次指定不执行词条用例')

        home_page.into_device_home_page(data.get_device('inertia_robotic'))

        TestInertiaRoBoVac.inertia_ready()

        robotic_home_page.into_setting(True)
        robotic_setting_page.swipe_page('up')
        robotic_setting_page.click_remove()
        assert robotic_setting_page.text_display('Are you sure you want to remove this device?'), 'inertia_robotic未显示删除设备提示弹窗'
        robotic_setting_page.commit_remove()
        robotic_setting_page.loading()
        home_page.swipe_page('down')
        assert home_page.find_device(data.get_device('inertia_robotic')) is False, 'inertia_robotic扫地机移除之后主页还未删除'

    @pytest.fixture(scope='function')
    def reset_phone_network(self):
        """
        检查并重置手机网络，防止配网失败影响网络
        :return:
        """
        yield 1
        add_device_page.set_system_wifi(data.get_wifi('phone')[0])

    @pytest.mark.robovac
    @pytest.mark.inertiarobotic
    @pytest.mark.run(order=331)
    @pytest.mark.parametrize('check_account', ['inertia_robotic'], indirect=True)
    def test_inertia_robotic_add_device(self, check_account, reset_phone_network):
        """
        添加惯性扫地机:
        1. app首页点击+，选择robotic，选择 RoboVac 30C max
        2. 点击Next，勾选 Status Confirmed，点击 next
        3. 选择亚添加的设备id
        4. 连接中，等待conecting消失
        【checkpoint】判断是否显示添加成功（文本校验）
        5. 修改设备昵称未T2150，点击保存
        6. 返回设备主页查看设备列表
        【checkpoint】首页列表刷新后显示扫地机T2150
        :param check_account:
        :return:
        """
        if GlobalVar.get_remove_add() == 0:
            GlobalVar.set_test_flag('f')
            pytest.skip('本次指定不执行词条用例')

        home_page.swipe_page('down')
        if home_page.find_device(data.get_device('inertia_robotic')):
            home_page.into_device_home_page(data.get_device('inertia_robotic'))

            TestInertiaRoBoVac.inertia_ready()

            robotic_home_page.into_setting(True)
            robotic_setting_page.swipe_page('up')
            robotic_setting_page.click_remove()
            robotic_setting_page.commit_remove()
            robotic_setting_page.loading()

        home_page.click_add_device()
        add_device_page.click_robotic()
        add_device_page.select_robotic('G30 Edge')
        wifi_data = data.get_wifi('inertia_robotic')
        add_device_page.set_wifi(wifi_data[0], wifi_data[1])
        add_device_page.confirm_status()
        add_device_page.select_robotic_by_id(data.get_device_udid('inertia_robotic'))
        add_device_page.loading()

        add_device_page.wait_connect()
        assert add_device_page.connect_result(), 'inertia_robotic 配网连接失败'
        add_device_page.set_device_name(data.get_device('inertia_robotic'))
        add_device_page.ok
        add_device_page.loading()

        home_page.swipe_page('down')
        assert home_page.find_device(data.get_device('inertia_robotic')), 'inertia_robotic 配网成功后首页未查找到T2250设备'
