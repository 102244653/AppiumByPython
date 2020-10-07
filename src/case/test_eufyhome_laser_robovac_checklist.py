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
from src.eufyhome.method.robotic.RoboticCleanHistory_Page import RoboticCleanHistoryPage

global base_page, start_page, user_page, time_zone_page, system_page, news_page, change_pw_page, home_page, \
            all_share_page, robotic_find_page, robotic_home_page, robotic_setting_page, robotic_suction_page,\
            robotic_voice_page, help_faq_page, robotic_clean_model_page, share_setting_page, add_device_page, \
            device_help_page, robotic_schedule_page, robotic_update_page, robotic_maintence_page, robotic_cleansetting_Page, \
            robotic_unit_page, robotic_zone_clean_page, robotic_manual_page, robotic_clean_history_page


# @pytest.mark.flaky(reruns=0)  # 失败重跑
@pytest.mark.repeat(0)  # 重复执行次数
@pytest.mark.usefixtures('driver_setup')  # 引用conftest.py中的driver_setup方法，创建会话
@pytest.mark.usefixtures('appium_setup')  # 引用conftest.py中的appium_setup方法，启动appium服务
class TestLaserRoboVac(object):
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
            robotic_unit_page, robotic_zone_clean_page, robotic_manual_page, robotic_clean_history_page

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
        robotic_clean_history_page = RoboticCleanHistoryPage(self.driver)

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
        start_page.login_phone(data.get_account(account),
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
                start_page.login_phone(data.get_account(account),
                                       data.get_account('pw'))
            else:
                raise Exception('登陆账号为空')
        else:
            if data.get_username(account) in home_page.read_username():
                return
            if account is not None:
                TestLaserRoboVac.change_account(account)
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
    def laser_ready():
        robotic_home_page.skip_robotic_guide()
        if robotic_home_page.is_offline:
            robotic_home_page.ok
            if robotic_home_page.robovac_is_offline() is False:
                assert False, 'laser_robotic 设备处于离线状态'

        robotic_home_page.ingore_update_languge()

    # ********************激光扫地机用例************************** #

    @pytest.mark.robovac
    @pytest.mark.laserrobotic
    @pytest.mark.run(order=200)
    @pytest.mark.parametrize('check_account', ['laser_robotic'], indirect=True)
    def laser_robotic_check_update_icon(self, check_account):
        """
        设备升级提示图标检查:
        1. app首页点击进入设备主页
        【checkpoint】首页设备列表是否显示升级图标
        :param check_account:
        :return:
        """
        home_page.swipe_page('down')
        assert home_page.have_update_icon(data.get_device('laser_robotic')), 'laser_robotic 未显示升级图标'

        home_page.click_update_icon(data.get_device('laser_robotic'))
        assert home_page.text_display('Firmware Update'), 'laser_robotic OTA升级快捷入口进入失败'

    @pytest.fixture(scope='function')
    def stop_laser_robovac(self):
        yield 1
        if home_page.is_welcome():
            home_page.into_device_home_page('laser_robotic')
        if robotic_home_page.read_robovac_status() == data.get_robotic_status('cleanning'):
            robotic_home_page.t2190_play()

    @pytest.mark.robovac
    @pytest.mark.laserrobotic
    @pytest.mark.run(order=202)
    @pytest.mark.parametrize('check_account', ['laser_robotic'], indirect=True)
    @pytest.mark.flaky(reruns=2, reruns_delay=40)
    def test_laser_robotic_play(self, check_account, stop_laser_robovac):
        """
        激光扫地机清扫启动/暂停:
        1. 点击激光扫地机进入扫地机主页
        2. 点击清扫按钮，检查扫地机状态
        【checkpoint】启动扫地机后设备状态变更为：Cleaning  （添加按钮图片的判断）
        3. 再次点击清扫按钮，检查扫地机状态
        【checkpoint】停止清扫后扫地机状态变为：standard  （添加按钮图片的判断）
        :param check_account:
        :return:
        """
        home_page.into_device_home_page(data.get_device('laser_robotic'))

        TestLaserRoboVac.laser_ready()

        # robotic_home_page.skip_robotic_guide()
        # if robotic_home_page.is_offline:
        #     robotic_home_page.ok
        #     if robotic_home_page.robovac_is_offline() is False:
        #         assert False, 'laser_robotic 设备处于离线状态'
        #
        # robotic_home_page.ingore_update_languge()

        robotic_home_page.t2190_play()
        time.sleep(8)
        robotic_home_page.swipe_page('down')
        assert data.get_robotic_status('cleaning') == robotic_home_page.read_robovac_status(), 'laser_robotic 扫地机启动清扫失败'
        assert 'Pause' in robotic_home_page.read_clean_btn_status(), 'laser_robotic 扫地机清扫按钮启动状态未切换'
        robotic_home_page.back_home()
        assert home_page.read_device_status(data.get_device('laser_robotic')) == 'Cleaning', 'laser_robotic 扫地机启动清扫后列表开关状态显示错误'

        home_page.click_device_btn(data.get_device('laser_robotic'))
        time.sleep(8)
        robotic_home_page.swipe_page('down')
        assert home_page.read_device_status(
            data.get_device('laser_robotic')) == 'Standby', 'laser_robotic 扫地机停止清扫后列表开关状态显示错误'
        home_page.into_device_home_page(data.get_device('laser_robotic'))
        assert robotic_home_page.read_robovac_status() == data.get_robotic_status('standard'), 'laser_robotic 扫地机暂停清扫失败'
        assert 'Clean' in robotic_home_page.read_clean_btn_status(), 'laser_robotic 扫地机清扫按钮启动状态未切换'

    @pytest.mark.robovac
    @pytest.mark.laserrobotic
    @pytest.mark.run(order=203)
    @pytest.mark.parametrize('check_account', ['laser_robotic'], indirect=True)
    @pytest.mark.flaky(reruns=2, reruns_delay=40)
    def test_laser_robotic_change_quite_suction(self, check_account):
        """
        激光扫地机quiet吸力模式修改:
        1. 点击激光扫地机进入扫地机主页，点击suctions进入吸力设置
        2. 点击选择 quiet ，在点击 boostiq开关检查开关状态
        【checkpoint】quiet吸力等级选择成功，检查v的位置
        3.在点击 boostiq开关检查开关状态
        【checkpoint】standard模式开关boostiq正常
        :param check_account:
        :return:
        """
        home_page.into_device_home_page(data.get_device('laser_robotic'))

        TestLaserRoboVac.laser_ready()

        robotic_home_page.t2190_suction()
        robotic_suction_page.t2190_quiet()
        assert robotic_suction_page.t2190_is_quiet(), 'laser_robotic quiet吸力模式切换失败'

        flag1 = robotic_suction_page.read_t2190_boostiq_status()
        robotic_suction_page.t2190_click_boostiq()
        time.sleep(5)
        flag2 = robotic_suction_page.read_t2190_boostiq_status()
        robotic_suction_page.t2190_click_boostiq()
        time.sleep(5)
        flag3 = robotic_suction_page.read_t2190_boostiq_status()

        assert flag1 != flag2 and flag1 == flag3, 'laser_robotic quiet档位boostiq开启/关闭失败'

    @pytest.mark.robovac
    @pytest.mark.laserrobotic
    @pytest.mark.run(order=204)
    @pytest.mark.parametrize('check_account', ['laser_robotic'], indirect=True)
    @pytest.mark.flaky(reruns=2, reruns_delay=40)
    def test_laser_robotic_change_standard_suction(self, check_account):
        """
        激光扫地机standard吸力模式修改:
        1. 点击激光扫地机进入扫地机主页，点击suctions进入吸力设置
        2. 点击选择 standard
        【checkpoint】standard吸力等级选择成功
        3.在点击 boostiq开关检查开关状态
        【checkpoint】standard模式开关boostiq正常
        :param check_account:
        :return:
        """
        home_page.into_device_home_page(data.get_device('laser_robotic'))

        TestLaserRoboVac.laser_ready()

        robotic_home_page.t2190_suction()
        robotic_suction_page.t2190_standard()
        assert robotic_suction_page.t2190_is_standard(), 'laser_robotic standard吸力模式切换失败'

        flag1 = robotic_suction_page.read_t2190_boostiq_status()
        robotic_suction_page.t2190_click_boostiq()
        time.sleep(5)
        flag2 = robotic_suction_page.read_t2190_boostiq_status()
        robotic_suction_page.t2190_click_boostiq()
        time.sleep(5)
        flag3 = robotic_suction_page.read_t2190_boostiq_status()

        assert flag1 != flag2 and flag1 == flag3, 'laser_robotic standard档位boostiq开启/关闭失败'

    @pytest.mark.robovac
    @pytest.mark.laserrobotic
    @pytest.mark.run(order=205)
    @pytest.mark.parametrize('check_account', ['laser_robotic'], indirect=True)
    @pytest.mark.flaky(reruns=2, reruns_delay=40)
    def test_laser_robotic_change_turbo_suction(self, check_account):
        """
        激光扫地机turbo吸力模式修改:
        1. 点击激光扫地机进入扫地机主页，点击suctions进入吸力设置
        2.点击选择 turbo
        【checkpoint】turbo吸力等级选择成功
        3.在点击 boostiq开关检查开关状态
        【checkpoint】turbo模式开关boostiq正常
        :param self:
        :param check_account:
        :return:
        """
        home_page.into_device_home_page(data.get_device('laser_robotic'))

        TestLaserRoboVac.laser_ready()

        robotic_home_page.t2190_suction()
        robotic_suction_page.t2190_turbo()
        assert robotic_suction_page.t2190_is_turbo(), 'laser_robotic turbo吸力模式切换失败'

        flag1 = robotic_suction_page.read_t2190_boostiq_status()
        robotic_suction_page.t2190_click_boostiq()
        time.sleep(5)
        flag2 = robotic_suction_page.read_t2190_boostiq_status()
        robotic_suction_page.t2190_click_boostiq()
        time.sleep(5)
        flag3 = robotic_suction_page.read_t2190_boostiq_status()

        assert flag1 != flag2 and flag1 == flag3, 'laser_robotic turbo档位boostiq开启/关闭失败'

    @pytest.mark.robovac
    @pytest.mark.laserrobotic
    @pytest.mark.run(order=206)
    @pytest.mark.parametrize('check_account', ['laser_robotic'], indirect=True)
    @pytest.mark.flaky(reruns=2, reruns_delay=40)
    def test_laser_robotic_change_max_suction(self, check_account):
        """
        激光扫地机max吸力模式修改:
        1. 点击激光扫地机进入扫地机主页，点击suctions进入吸力设置
        2.点击选择 max
        【checkpoint】max吸力等级选择成功
        3.在点击 boostiq开关检查开关状态
        【checkpoint】max模式不能开关boostiq
        :param check_account:
        :return:
        """
        home_page.into_device_home_page(data.get_device('laser_robotic'))

        TestLaserRoboVac.laser_ready()

        robotic_home_page.t2190_suction()
        robotic_suction_page.t2190_max()
        assert robotic_suction_page.t2190_is_max(), 'laser_robotic max吸力模式切换失败'

        flag1 = robotic_suction_page.read_t2190_boostiq_status()
        robotic_suction_page.t2190_click_boostiq()
        time.sleep(5)
        flag2 = robotic_suction_page.read_t2190_boostiq_status()

        assert flag1 == flag2, 'laser_robotic max 档位boostiq开启/关闭会生效'

    @pytest.mark.robovac
    @pytest.mark.laserrobotic
    @pytest.mark.run(order=207)
    @pytest.mark.parametrize('check_account', ['laser_robotic'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def test_laser_robotic_change_util(self, check_account):
        """
        激光扫地机修改面积单位和面积单位换算：
        1. 点击激光扫地机进入扫地机主页，记录当前面积，单位 为area1， unit1，点击more进入设置
        2. 根据 unit1 切换面积单位
        【checkpoint】修改后设备主页显示正常
        3. 读取新的面积 area2
        【checkpoint】修改单位后面积根据公式计算后求差，误差0. 3以内
        :param check_account:
        :return:
        """
        home_page.into_device_home_page(data.get_device('laser_robotic'))

        TestLaserRoboVac.laser_ready()

        area, unit = robotic_home_page.read_clean_area()
        robotic_home_page.into_setting()
        robotic_setting_page.swipe_page('up')
        robotic_setting_page.into_unit()

        if unit == data.get_area_util('m2'):
            robotic_unit_page.click_ft2()
            time.sleep(5)
            assert robotic_unit_page.check_ft2(), 'laser_robotic 切换清扫面积单位ft2失败'
        else:
            robotic_unit_page.click_m2()
            time.sleep(5)
            assert robotic_unit_page.check_m2(), 'laser_robotic 切换清扫面积单位m2失败'

        robotic_unit_page.back_setting()
        robotic_setting_page.back_robovac()
        area0, unit0 = robotic_home_page.read_clean_area()

        if unit == data.get_area_util('m2'):
            assert unit0 == data.get_area_util('ft2'), 'laser_robotic 切换面积单位为ft2后主页显示错误'
            assert abs(0.093 * area0 - area) < 0.5, 'laser_robotic 切换面积单位m2为ft2后主页的面积转换计算错误'
        else:
            assert unit0 == data.get_area_util('m2'), 'laser_robotic 切换面积单位为m2后主页显示错误'
            assert abs(area0 - area * 0.093) < 0.5, 'laser_robotic 切换面积单位ft2为m2后主页的面积转换计算错误'

    @pytest.fixture(scope='function')
    def laser_robotic_charge(self):
        """
        回充的后置操作：
        恢复为standard状态
        :return:
        """
        yield 1
        if GlobalVar.get_test_flag():  # 设备离线时不执行
            status = robotic_home_page.read_robovac_status()
            if status == data.get_robotic_status('cleaning') or status == data.get_robotic_status('backing'):
                robotic_home_page.t2190_play()
                if robotic_home_page.text_display('Are you sure you want to stop cleaning and send RoboVac home?'):
                    robotic_home_page.yes
                if data.get_robotic_status('cleaning') == robotic_home_page.read_robovac_status():
                    robotic_home_page.t2190_play()

    @pytest.mark.robovac
    @pytest.mark.laserrobotic
    @pytest.mark.run(order=208)
    @pytest.mark.parametrize('check_account', ['laser_robotic'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def test_laser_robotic_standard_charge(self, check_account, laser_robotic_charge):
        """
        激光扫地机不再充电座回充:
        1. 点击随机扫地机进入扫地机主页，使扫地机状态为standard
        2. 点击 charge 按钮
        【checkpoint】扫地机回充显示toast：Heading Home
        【checkpoint】扫地机状态显示：Heading Home
        :param check_account:
        :return:
        """
        home_page.into_device_home_page(data.get_device('laser_robotic'))

        TestLaserRoboVac.laser_ready()

        status = robotic_home_page.read_robovac_status()

        if status == data.get_robotic_status('charging'):
            robotic_home_page.t2190_play()
            time.sleep(5)
            robotic_home_page.t2190_play()
        elif status == data.get_robotic_status('cleaning'):
            robotic_home_page.t2190_play()

        GlobalVar.set_test_flag('t')
        time.sleep(5)
        robotic_home_page.t2190_charge()
        # toast = robotic_home_page.is_toast_exist('RoboVac is heading home', True, True)
        status = robotic_home_page.read_robovac_status() in [data.get_robotic_status('backing'), data.get_robotic_status('charging')]
        assert status, 'laser_robotic 在standby状态下回充中状态显示:' + str(status)
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

    @pytest.mark.robovac
    @pytest.mark.laserrobotic
    @pytest.mark.run(order=209)
    @pytest.mark.parametrize('check_account', ['laser_robotic'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def test_laser_robotic_iscleaning_charge(self, check_account, laser_robotic_charge):
        """
        激光扫地机清扫过程中点击回充按钮:
        1. 点击随机扫地机进入扫地机主页，使扫地机状态为cleaning
        2. 点击 charge 按钮
        【checkpoint】提示是否结束清扫开始回充弹窗
        3.点击 ok按钮
        【checkpoint】扫地机回充显示toast：Heading Home
        【checkpoint】等待5min，每分钟检查一次扫地机状态显示：Heading Home
        :param random_robotic_charge:
        :return:
        """
        home_page.into_device_home_page(data.get_device('laser_robotic'))

        TestLaserRoboVac.laser_ready()

        status = robotic_home_page.read_robovac_status()
        GlobalVar.set_test_flag('t')

        if status == data.get_robotic_status('standard') or status == data.get_robotic_status('charging'):
            robotic_home_page.t2190_play()
            time.sleep(5)

        robotic_home_page.t2190_charge()
        # toast = robotic_home_page.is_toast_exist('RoboVac is heading home', True, True)
        status = robotic_home_page.read_robovac_status() in [data.get_robotic_status('backing'), data.get_robotic_status('charging')]
        assert status, 'laser_robotic 在cleaning状态回充中状态显示:' + str(status)

        times = 1
        while times < 10:
            times = times + 1
            _ac = robotic_home_page.read_robovac_status()
            if _ac in [data.get_robotic_status('charging'), data.get_robotic_status('standard')]:
                break
            else:
                time.sleep(10)

    @pytest.mark.robovac
    @pytest.mark.laserrobotic
    @pytest.mark.run(order=210)
    @pytest.mark.parametrize('check_account', ['laser_robotic'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def laser_robotic_ischarging_charge(self, check_account, laser_robotic_charge):
        """
        激光扫地机充电中点击清扫按钮:
        1. 点击激光扫地机进入扫地机主页，使扫地机状态为charging
        2. 点击 charge 按钮
        【checkpoint】toast提示充电中
        :param check_account:
        :param random_robotic_charge:
        :return:
        """
        home_page.into_device_home_page(data.get_device('laser_robotic'))

        TestLaserRoboVac.laser_ready()

        status = robotic_home_page.read_robovac_status()
        GlobalVar.set_test_flag('t')

        if status == data.get_robotic_status('standard') or status == data.get_robotic_status('cleaning'):
            robotic_home_page.t2190_charge()
            times = 1
            flag = False
            while times < 20:
                times = times + 1
                _ac = robotic_home_page.read_robovac_status()
                if _ac in [data.get_robotic_status('charging'), data.get_robotic_status('standard')]:
                    flag = True
                    break
                else:
                    time.sleep(10)
            assert flag, 'laser_robotic 前置条件失败，用例不执行'

        robotic_home_page.t2190_charge()

        assert robotic_home_page.is_toast_exist('Charging', True, True), 'laser_robotic 在charging状态点击回充提示语错误'

    @pytest.mark.robovac
    @pytest.mark.skip(reason='t2190扫地机在充电状态能够下达寻找指令')
    @pytest.mark.laserrobotic
    @pytest.mark.run(order=211)
    @pytest.mark.parametrize('check_account', ['laser_robotic'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def laser_robotic_ischarging_find(self, check_account, laser_robotic_charging):
        """
        充电状态点击find按钮:
        1. 点击激光扫地机进入扫地机主页，点击 find 按钮
        2.点击 start 按钮
        【checkpoint】toast提示：Charging
        :param check_account:
        :return:
        """
        home_page.into_device_home_page(data.get_device('laser_robotic'))

        TestLaserRoboVac.laser_ready()

        status = robotic_home_page.read_status()
        if status in [data.get_robotic_status('standard'), data.get_robotic_status('cleaning')]:
            robotic_home_page.t2190_charge()
            times = 1
            flag = False
            while times < 20:
                times = times + 1
                _ac = robotic_home_page.read_status()
                if data.get_robotic_status('charging') in _ac:
                    flag = True
                    break
                else:
                    time.sleep(10)
            assert flag, 'laser_robotic 前置条件失败，用例不执行'

        robotic_home_page.into_setting()
        robotic_setting_page.into_find()
        robotic_find_page.click_find('laser')

        assert robotic_find_page.check_find_img('laser', 't2190_find_start'), 'laser_robotic 在charging状态点击find不会启动寻找'

    @pytest.mark.robovac
    @pytest.mark.laserrobotic
    @pytest.mark.run(order=212)
    @pytest.mark.parametrize('check_account', ['laser_robotic'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def test_laser_robotic_manual_find(self, check_account):
        """
        激光扫地机find手动开始/停止测试:
        1. 点击激光扫地机进入扫地机主页，点击 find 按钮
        2. 点击 start 按钮
        【checkpoint】点击后按钮文案变为stoped
        3. 点击stop停止蜂鸣
        【checkpoint】点击stoped后按钮变为start
        :param check_account:
        :return:
        """
        home_page.into_device_home_page(data.get_device('laser_robotic'))

        TestLaserRoboVac.laser_ready()

        status = robotic_home_page.read_robovac_status()
        if status == data.get_robotic_status('charging'):
            robotic_home_page.t2190_play()
            time.sleep(5)
            robotic_home_page.t2190_play()

        robotic_home_page.into_setting()
        robotic_setting_page.into_find()
        robotic_find_page.click_find('laser')
        time.sleep(3)
        assert robotic_find_page.check_find_img('laser', 't2190_find_stop'), 'laser_robotic 手动启动find me失败'
        robotic_find_page.click_find('laser')
        time.sleep(3)
        assert robotic_find_page.check_find_img('laser', 't2190_find_start'), 'laser_robotic 手动停止find me失败'

    @pytest.mark.robovac
    @pytest.mark.laserrobotic
    @pytest.mark.run(order=213)
    @pytest.mark.parametrize('check_account', ['laser_robotic'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def test_laser_robotic_find_timeout(self, check_account):
        """
        激光扫地机find蜂鸣时间测试：
        1. 点击激光扫地机进入扫地机主页，点击 find 按钮
        2.点击start设备开始蜂鸣
        【checkpoint】点击find启动后按钮变为stoped
        3.等待65s
        【checkpoint】扫地机find蜂鸣i1min后自动结束，按钮变为start
        :param check_account:
        :return:
        """
        home_page.into_device_home_page(data.get_device('laser_robotic'))

        TestLaserRoboVac.laser_ready()

        status = robotic_home_page.read_robovac_status()
        if status == data.get_robotic_status('charging'):
            robotic_home_page.t2190_play()
            time.sleep(5)
            robotic_home_page.t2190_play()

        robotic_home_page.into_setting()
        robotic_setting_page.into_find()
        robotic_find_page.click_find('laser')

        assert robotic_find_page.check_find_img('laser', 't2190_find_stop'), 'laser_robotic 未正常启动find功能'
        robotic_find_page.long_wait(70)
        assert robotic_find_page.check_find_img('laser', 't2190_find_start'), 'laser_robotic 设备find me蜂鸣未在1分钟内结束'

    @pytest.mark.robovac
    @pytest.mark.laserrobotic
    @pytest.mark.run(order=214)
    @pytest.mark.parametrize('check_account', ['laser_robotic'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def test_laser_robotic_share_error_email(self, check_account):
        """
        激光扫地机分享给错误格式账号:
        1. 点击激光扫地机进入扫地机主页，点击 more进入设置界面，点击share setting进入分享列表
        2. 点击 add 按钮进入添加界面，输入分享账号：a@a并提交
        【checkpoint】分享失败，toast提示：Please enter a vailed email adress
        :return:
        """
        home_page.into_device_home_page(data.get_device('laser_robotic'))

        TestLaserRoboVac.laser_ready()

        robotic_home_page.into_setting()
        robotic_setting_page.into_share()
        share_setting_page.add_share()
        share_setting_page.commit_share('1354253')

        if share_setting_page.platform == 'ios':
            flag = share_setting_page.text_display('Add Member')
        else:
            flag = share_setting_page.share_result() is False
        assert flag, 'laser_robotic 分享错误邮箱的结果异常'

    @pytest.mark.robovac
    @pytest.mark.laserrobotic
    @pytest.mark.run(order=215)
    @pytest.mark.parametrize('check_account', ['laser_robotic'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def test_laser_robotic_share_nosign_email(self, check_account):
        """
        激光扫地机分享给未注册的账号:
        1. 点击激光扫地机进入扫地机主页，点击 more进入设置界面，点击share setting进入分享列表
        2. 点击 add 按钮进入添加界面，输入分享账号：a@a. com并提交
        【checkpoint】分享失败，弹窗提示：Failed to share
        :return:
        """
        home_page.into_device_home_page(data.get_device('laser_robotic'))

        TestLaserRoboVac.laser_ready()

        robotic_home_page.into_setting()
        robotic_setting_page.into_share()
        share_setting_page.add_share()
        share_setting_page.commit_share('19900002222')
        assert share_setting_page.share_result() is False, 'laser_robotic 分享失败的提示错误'

    @pytest.fixture(scope='function')
    def delete_refuse_share_account(self):
        """
        先删除refuseshare账号分享列表
        :return:
        """
        home_page.into_system()
        system_page.into_sharing()
        all_share_page.into_device(data.get_device('laser_robotic'))
        share_setting_page.delete_share()
        all_share_page.kill
        time.sleep(2)
        all_share_page.open

    @pytest.mark.robovac
    @pytest.mark.laserrobotic
    @pytest.mark.run(order=216)
    @pytest.mark.parametrize('check_account', ['laser_robotic'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def test_laser_robotic_share_email(self, check_account, delete_refuse_share_account):
        """
        激光扫地机分享给已注册的账号：
        1. 点击激光扫地机进入扫地机主页，点击 more进入设置界面，点击share setting进入分享列表
        2. 点击 add 按钮进入添加界面，输入分享账号：Yi@aa. com并提交
        【checkpoint】 分享邀请发送成功，弹窗提示：Successed to share
        【checkpoint】页面返回到分享列表并显示分享人，状态为：待确认
        :param check_account:
        :return:
        """
        home_page.into_device_home_page(data.get_device('laser_robotic'))

        TestLaserRoboVac.laser_ready()

        robotic_home_page.into_setting()
        robotic_setting_page.into_share()
        share_setting_page.add_share()
        share_setting_page.commit_share(data.get_account('phoneshare'))

        assert share_setting_page.share_result(), 'laser_robotic 正确账号分享失败'
        share_setting_page.ok
        share_setting_page.loading()
        share_setting_page.swipe_page('down')
        status = share_setting_page.read_share_status(data.get_username('phoneshare'))
        assert status == 'Awaiting Confirmation' or status == 'Pending Confirmation', 'laser_robotic 分享列表被分享者状态显示错误'

    @pytest.mark.robovac
    @pytest.mark.laserrobotic
    @pytest.mark.run(order=217)
    @pytest.mark.parametrize('check_account', ['laser_robotic'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def test_laser_robotic_agree_share(self, check_account, delete_share_news):
        """
        激光扫地机被分享者接受分享:
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
        home_page.into_device_home_page(data.get_device('laser_robotic'))

        TestLaserRoboVac.laser_ready()

        robotic_home_page.into_setting()
        robotic_setting_page.into_share()
        status = share_setting_page.read_share_status(data.get_username('phoneshare'))
        if status not in ['Awaiting Confirmation', 'Pending Confirmation']:
            share_setting_page.add_share()
            share_setting_page.commit_share(data.get_account('phoneshare'))

            assert share_setting_page.share_result(), 'laser_robotic 正确账号分享失败,无法执行用例:[id=35]'
            share_setting_page.ok
            share_setting_page.loading()
        share_setting_page.back_setting()
        robotic_setting_page.back_robovac()
        robotic_home_page.back_home()

        TestLaserRoboVac.change_account('phoneshare')

        home_page.into_system()

        system_page.into_sharing()
        assert all_share_page.text_display(data.get_device('laser_robotic')), '被分享列表未显示分享设备信息'
        GlobalVar.set_test_flag('t')  # 到这里后需要执行 tear_down
        all_share_page.into_device(data.get_device('laser_robotic'))
        all_share_page.yes
        all_share_page.loading()

        assert news_page.text_display('Request Accepted. You may now use this device.'), 'laser_robotic 被分享者确认接受分享失败'
        news_page.ok
        assert news_page.text_display(
            'shared a ' + data.get_device('laser_robotic')), 'laser_robotic 被分享者显示的分享设备名称错误'

        news_page.back_system()
        news_page.back_system()
        system_page.back_home()
        home_page.swipe_page('down')
        assert home_page.find_device(data.get_device('laser_robotic')), '被分享者未显示分享的扫地机设备'

    @pytest.fixture(scope='function')
    def t2190_close_yellow_tip(self):
        """
        关闭小黄条提示
        :return:
        """
        yield 1
        if GlobalVar.get_test_flag():
            robotic_schedule_page.close_yellow_tip()

    @pytest.mark.robovac
    @pytest.mark.laserrobotic
    @pytest.mark.run(order=218)
    @pytest.mark.parametrize('check_account', ['phoneshare'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def laser_robotic_yellow_tip(self, t2190_close_yellow_tip, check_account):
        """
        随机扫地机被分享者修改设备名及小黄条显示:
        1. app首页点击进入设备主页，修改一个定时任务
        2.切换账号 Yi@aaa.com，查看随机扫地机设备
        【checkpoint】显示设备名称修改小黄条
        :return:
        """
        if home_page.find_device(data.get_device('laser_robotic')) is False:
            assert False, '为查找到分享设备，无法执行用:[test_laser_robotic_yellow_tip]'

        home_page.into_device_home_page(data.get_device('laser_robotic'))
        robotic_home_page.skip_robotic_guide()

        if robotic_home_page.is_offline:
            assert False, 'laser_robotic 设备处于离线状态'

        robotic_home_page.ingore_update_languge()
        robotic_home_page.t2190_schedule()
        if robotic_schedule_page.t2190_count_schedule() < 1:
            robotic_schedule_page.t2190_creat_new_schedule()
        robotic_schedule_page.t2190_click_schedule_btn()
        robotic_schedule_page.back_robotic()
        robotic_home_page.back_home()

        TestLaserRoboVac.change_account('laser_robotic')

        home_page.into_device_home_page(data.get_device('laser_robotic'))
        if robotic_home_page.is_offline:
            robotic_home_page.ok
            if robotic_home_page.robovac_is_offline() is False:
                assert False, 'laser_robotic 设备处于离线状态'

        GlobalVar.set_test_flag('t')

        robotic_home_page.ingore_update_languge()
        robotic_home_page.t2190_schedule()
        assert robotic_schedule_page.text_display('modified the schedule'), 'laser_robotic 被分享人修改了定时任务未显示小黄条提示'

    @pytest.mark.robovac
    @pytest.mark.laserrobotic
    @pytest.mark.run(order=219)
    @pytest.mark.parametrize('check_account', ['phoneshare'], indirect=True)
    def test_laser_robotic_delete_share(self, check_account):
        """
        激光扫地机被分享者移除分享设备:
        1. app首页点击进入设备主页，点击更多，点击删除设备
        【checkpoint】弹窗提示确认移除
        2.点击 ok 按钮
        【checkpoint】分享者列表不显示被分享人信息
        3.切换账号Yi@aaa。com，查看设备分享列表
        【checkpoint】分享者列表不显示被分享人信息
        :return:
        """
        time.sleep(5)
        assert home_page.find_device(data.get_device('laser_robotic')), '未查找到分享设备，无法执行用:[test_laser_robotic_delete_share]'

        home_page.into_device_home_page(data.get_device('laser_robotic'))

        TestLaserRoboVac.laser_ready()

        robotic_home_page.into_setting()
        time.sleep(2)
        robotic_setting_page.swipe_page('up')
        robotic_setting_page.click_remove()
        assert robotic_setting_page.text_display('Are you sure you want to remove this device?'), '未显示移除确认弹窗'
        robotic_setting_page.commit_remove()
        home_page.swipe_page('down')
        assert home_page.find_device(data.get_device('laser_robotic')) is False, 'laser_robotic 被分享着移除后设备未删除'

        TestLaserRoboVac.change_account('laser_robotic')

        home_page.into_device_home_page(data.get_device('laser_robotic'))
        if robotic_home_page.is_offline:
            robotic_home_page.ok
            if robotic_home_page.robovac_is_offline() is False:
                assert False, 'laser_robotic 设备处于离线状态'

        robotic_home_page.ingore_update_languge()
        robotic_home_page.into_setting()
        robotic_setting_page.into_share()
        assert data.get_username('phoneshare') not in share_setting_page.read_share_to_me_list(), 'laser_robotic 分享列表显示已移除的分享者信息'

    @pytest.mark.robovac
    @pytest.mark.laserrobotic
    @pytest.mark.run(order=220)
    @pytest.mark.parametrize('check_account', ['laser_robotic'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def test_laser_robotic_refuse_share(self, delete_share_news, check_account, delete_refuse_share_account):
        """
        激光扫地机被分享者拒绝接受分享：
        1. 点击激光扫地机进入扫地机主页，点击 more进入设置界面，点击share setting进入分享列表
        2. 点击 add 按钮进入添加界面，输入分享账号：Yi@aa.com并提交
        【checkpoint】 分享邀请发送成功，弹窗提示：Successed to share
        3.重启app切换账号Yi@aa.com，进入分享消息记录
        4.点击拒绝接受分享按钮
        【checkpoint】显示已拒绝分享弹窗
        【chenckpoint】app首页不显示分享设备
        :param check_account:
        :return:
        """
        home_page.into_device_home_page(data.get_device('laser_robotic'))

        TestLaserRoboVac.laser_ready()

        robotic_home_page.into_setting()
        robotic_setting_page.into_share()
        share_setting_page.add_share()
        share_setting_page.commit_share(data.get_account('phoneshare'))
        assert share_setting_page.share_result(), 'laser_robotic 正确账号分享失败'
        share_setting_page.ok
        share_setting_page.loading()

        share_setting_page.back_setting()
        robotic_setting_page.back_robovac()
        robotic_home_page.back_home()

        TestLaserRoboVac.change_account('phoneshare')
        GlobalVar.set_test_flag('t')

        home_page.into_system()
        system_page.into_sharing()
        all_share_page.into_device(data.get_device('laser_robotic'))
        all_share_page.no
        assert all_share_page.text_display(
            'Request Declined. This device will be removed.'), 'laser_robotic 被分享者拒绝接受分享失败'
        all_share_page.ok
        all_share_page.loading()

        all_share_page.back_system()
        system_page.back_home()
        home_page.swipe_page('down')
        assert home_page.find_device(data.get_device('laser_robotic')) is False, 'app首页被分享者拒绝分享后显示分享了扫地机设备'

    @pytest.fixture(scope='function')
    def stop_laser_robovac(self):
        """
        停止扫地机工作
        :return:
        """
        yield 1
        if GlobalVar.get_test_flag() and data.get_robotic_status('cleaning') in robotic_home_page.read_robovac_status():
                robotic_home_page.t2190_play()

    @pytest.mark.robovac
    @pytest.mark.laserrobotic
    @pytest.mark.run(order=221)
    @pytest.mark.parametrize('check_account', ['laser_robotic'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def test_laser_robotic_zone_clean(self, stop_laser_robovac, check_account):
        """
        激光启动指定区域清扫:
        1. app首页点击进入设备主页，点击zone clean
        2. 点击add添加一个区域，点击保存
        【checkpoint】检查是否启动清扫，状态：cleaning
        【checkpoint】检查按钮对应的状态文案
        :param delete_share_news:
        :param check_account:
        :return:
        """
        home_page.into_device_home_page(data.get_device('laser_robotic'))

        TestLaserRoboVac.laser_ready()

        robotic_home_page.t2190_zone_clean()
        robotic_zone_clean_page.close_tip()
        robotic_zone_clean_page.add_zone()
        assert robotic_zone_clean_page.is_toast_exist('No maps added.', True, True) is False, '激光扫地机当前无地图无法开始指定区域清扫'
        robotic_zone_clean_page.start_zone_clean()

        GlobalVar.set_test_flag('t')

        time.sleep(5)
        assert data.get_robotic_status('cleaning') in robotic_home_page.read_robovac_status(), 'laser_robotic 扫地机指定区域清扫失败'

    @pytest.mark.robovac
    @pytest.mark.run(order=222)
    @pytest.mark.parametrize('check_account', ['laser_robotic'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def test_laser_robotic_add_delete_schedule(self, check_account):
        """
        激光扫地机添加和删除定时任务:
        1. app首页点击进入设备主页，点击schedule
        2. 激光添加一个定时任务，内容不做限制
        【checkpoint】 列表增加一个定时任务
        【checkpoint】新增扫地机任务状态变为开启
        3. 长按修改记录左滑删除
        【checkpoint】不显示定时任务修改记录
        :return:
        """
        home_page.into_device_home_page(data.get_device('laser_robotic'))

        TestLaserRoboVac.laser_ready()

        robotic_home_page.t2190_schedule()
        robotic_schedule_page.t2190_delete_schedule()
        robotic_schedule_page.t2190_creat_new_schedule()
        w = robotic_schedule_page.week_id
        assert robotic_schedule_page.text_display(data.get_week_by_id(str(w))), 'laser_robotic 添加定时任务后列表未显示'
        assert robotic_schedule_page.t2190_read_btn_status() == 'on', '定时任务开关默认状态显示错误'

        robotic_schedule_page.t2190_delete_schedule()
        time.sleep(2)
        assert robotic_schedule_page.t2190_count_schedule() == 0, 'laser_robotic 定时任务删除失败'

    @pytest.mark.robovac
    @pytest.mark.laserrobotic
    @pytest.mark.run(order=222)
    @pytest.mark.parametrize('check_account', ['laser_robotic'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def test_laser_robotic_check_schedule_icon(self, check_account):
        """
        检查定时任务图标是否显示：
        1.进入app主页，检查是否显示定时任务图标
        2.如果未显示则去开启一个定时任务，并返回app首页
        【checkpoint】检查设备是否显示定时任务图标
        :return:
        """
        home_page.swipe_page('down')
        status = home_page.have_schedule_icon(data.get_device('laser_robotic'))

        if not status:
            home_page.into_device_home_page(data.get_device('laser_robotic'))

            TestLaserRoboVac.laser_ready()

            robotic_home_page.t2190_schedule()
            robotic_schedule_page.t2190_creat_new_schedule()
            robotic_schedule_page.back_robotic()
            robotic_home_page.back_home()
            home_page.swipe_page('down')
            status = home_page.have_schedule_icon(data.get_device('laser_robotic'))

        assert status, 'laser_robotic 未显示定时任务图标'

        home_page.click_schedule_icon(data.get_device('laser_robotic'))
        assert home_page.text_display('Schedules'), 'laser_robotic 定时任务快捷图标进入失败'

    @pytest.mark.robovac
    @pytest.mark.laserrobotic
    @pytest.mark.run(order=223)
    @pytest.mark.parametrize('check_account', ['laser_robotic'], indirect=True)
    def laser_robotic_help_title(self, check_account):
        """
        激光扫地机help列表数量统计:
        1. app首页点击进入设备主页，点击more进入设置界面，点击help
        2. 遍历help页面的问答列表
        【checkpoint】 统计help列表总数=
        【checkpoint】遍历help列表的标题是否正确
        :param check_account:
        :return:
        """
        home_page.into_device_home_page(data.get_device('laser_robotic'))
        robotic_home_page.skip_robotic_guide()
        if robotic_home_page.is_offline:
            robotic_home_page.ok

        robotic_home_page.ingore_update_languge()
        robotic_home_page.into_setting()
        robotic_setting_page.swipe_page('up')
        robotic_setting_page.into_device_help()
        title_list = device_help_page.read_help_title()
        assert len(title_list) != 0, 'laser_robotic help列表显示为空'

        # expect_list = data.read_json(data.get_device('laser_robotic'))
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
        # assert num and flag, 'laser_robotic help列表总数：' + str(num) + ',与预期相比缺少：' + str(expect_titles) + ',与实际相比多出：' + str(
        #     actual_titles)

    @pytest.mark.laserrobotic
    @pytest.mark.run(order=224)
    @pytest.mark.parametrize('check_account', ['laser_robotic'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def laser_robotic_help_feedback(self, check_account):
        """
        激光扫地机help的反馈界面:
        1. app首页点击进入设备主页，点击more进入设置界面，点击help
        2.点击进入feedback页面，点击submit按钮
        【checkpoint】检查是否有toast提示：Feedback field cannot be blank.
        :return:
        """
        home_page.into_device_home_page(data.get_device('laser_robotic'))
        robotic_home_page.skip_robotic_guide()
        if robotic_home_page.is_offline:
            robotic_home_page.ok

        robotic_home_page.ingore_update_languge()
        robotic_home_page.into_setting()
        robotic_setting_page.swipe_page('up')
        robotic_setting_page.into_device_help()
        device_help_page.into_feed_back()
        device_help_page.submit_feed_back('laser test feedback')
        assert device_help_page.is_help_page(), 'laser_robotic 提交反馈失败'

    @pytest.mark.robovac
    @pytest.mark.laserrobotic
    @pytest.mark.run(order=225)
    @pytest.mark.parametrize('check_account', ['laser_robotic'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def laser_robotic_help_chat(self, check_account):
        """
        激光扫地机help的chat界面：
        1. app首页点击进入设备主页，点击more进入设置界面，点击help
        2.进入chat界面，发送一条消息
        【checkpoint】检查消息回复
        :param check_account:
        :return:
        """
        home_page.into_device_home_page(data.get_device('laser_robotic'))
        robotic_home_page.skip_robotic_guide()
        if robotic_home_page.is_offline:
            robotic_home_page.ok

        robotic_home_page.ingore_update_languge()
        robotic_home_page.into_setting()
        robotic_setting_page.swipe_page('up')
        robotic_setting_page.into_device_help()
        device_help_page.into_chat()
        assert device_help_page.text_display('Chat With Eufy'), 'laser_robotic 进入chat聊天界面无响应'

    @pytest.mark.robovac
    @pytest.mark.laserrobotic
    @pytest.mark.run(order=226)
    @pytest.mark.parametrize('check_account', ['laser_robotic'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def _laser_robotic_help_telphone(self, check_account):
        """
        激光扫地机help的电话界面：
        1. app首页点击进入设备主页，点击more进入设置界面，点击help
        2.进入call us 界面，检查页面的联系电话
        【checkpoint】遍历电话号码是否显示正确
        :param check_account:
        :return:
        """
        home_page.into_device_home_page(data.get_device('laser_robotic'))
        robotic_home_page.skip_robotic_guide()
        if robotic_home_page.is_offline:
            robotic_home_page.ok

        robotic_home_page.ingore_update_languge()
        robotic_home_page.into_setting()
        robotic_setting_page.swipe_page('up')
        robotic_setting_page.into_device_help()
        device_help_page.into_call_us()

        us = data.get_phone('us') in device_help_page.read_phone_number('us')
        uk = data.get_phone('uk') in device_help_page.read_phone_number('uk')
        de = data.get_phone('de') in device_help_page.read_phone_number('de')
        jp = data.get_phone('jp') in device_help_page.read_phone_number('jp')
        assert us and uk and de and jp, 'laser_robotic 客服联系电话显示错误：us=' + str(us) + ';uk=' + str(uk) + ';de=' + str(
            de) + ';jp=' + str(jp)

    @pytest.mark.robovac
    @pytest.mark.laserrobotic
    @pytest.mark.run(order=227)
    @pytest.mark.parametrize('check_account', ['laser_robotic'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def test_laser_robotic_manual_controls(self, check_account):
        """
        激光扫地机手动控制界面操作：
        1. app首页点击进入设备主页，点击more
        2. 点击manual controls进入控制界面，点击spot
        【checkpoint】 按钮开关文字变为：puase
        【checkpoint】扫地机状态变为spot
        3. 点击recharge
        【checkpoint】 回充提示tosat：Heading home. . .
        【checkpoint】扫地机状态：Heading home
        :return:
        """
        home_page.into_device_home_page(data.get_device('laser_robotic'))
        robotic_home_page.skip_robotic_guide()

        TestLaserRoboVac.laser_ready()

        robotic_home_page.into_setting()
        robotic_setting_page.swipe_page('up')
        robotic_setting_page.into_manual()

        robotic_manual_page.click_clean()
        time.sleep(2.5)
        assert robotic_manual_page.check_clean_status('manual_stop'), 'laser_robotic 手动启动清扫失败'

        robotic_manual_page.click_clean()
        time.sleep(2.5)
        assert robotic_manual_page.check_clean_status('manual_start'), 'laser_robotic 手动停止清扫失败'

        robotic_manual_page.click_spot()
        time.sleep(2.5)
        assert robotic_manual_page.check_clean_status('manual_stop'), 'laser_robotic 手动启动定点清扫失败'

        robotic_manual_page.click_recharge()
        flag = False
        times = 1
        while times < 7:
            times = times + 1
            if robotic_manual_page.check_clean_status('manual_start'):
                flag = True
                break
            else:
                time.sleep(10)
        assert flag, 'laser_robotic 手动启动回充失败'

    @pytest.mark.robovac
    @pytest.mark.skip(reason="无有效的判断条件")
    @pytest.mark.laserrobotic
    @pytest.mark.run(order=228)
    @pytest.mark.parametrize('check_account', ['laser_robotic'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def laser_robotic_reset_single_mantenance(self, check_account):
        """
        单个配材重置:
        1. app首页点击进入设备主页，点击more
        2.进入配材重置界面，选择滤网，点击reset
        【checkpoint】弹出重置确认弹窗
        【checkpoint】当前配材主页重置后使用率为100%，使用时间0h
        :param check_account:
        :return:
        """
        home_page.into_device_home_page(data.get_device('laser_robotic'))
        robotic_home_page.skip_robotic_guide()

        TestLaserRoboVac.laser_ready()

        robotic_home_page.into_setting()
        robotic_setting_page.swipe_page('up')
        robotic_setting_page.into_maintenance()
        robotic_maintence_page.clear_filter()

        assert robotic_maintence_page.text_display('Do you want to reset time for the filter?'), '滤网重置未显示弹窗提示'
        if robotic_maintence_page.platform == 'ios':
            robotic_maintence_page.ok
        else:
            robotic_maintence_page.yes

        assert robotic_maintence_page.is_toast_exist('', True, True), 'filter 重置失败，未显示成功toast提示'

    @pytest.mark.robovac
    @pytest.mark.skip(reason="无有效的判断条件")
    @pytest.mark.laserrobotic
    @pytest.mark.run(order=229)
    @pytest.mark.parametrize('check_account', ['laser_robotic'], indirect=True)
    def laser_robotic_reset_all_mantenance(self, check_account):
        """
        全部配材重置:
        1. app首页点击进入设备主页，点击more
        2.进入配材列表界面，点击claer
        【checkpoint】 弹出重置确认弹窗
        【checkpoint】配材列表重置后使用率为100%，使用时间0h
        :param check_account:
        :return:
        """
        home_page.into_device_home_page(data.get_device('laser_robotic'))
        robotic_home_page.skip_robotic_guide()

        TestLaserRoboVac.laser_ready()

        robotic_home_page.into_setting()
        robotic_setting_page.swipe_page('up')
        robotic_setting_page.into_maintenance()

        robotic_maintence_page.clear_all()
        assert robotic_maintence_page.text_display('Do you want to reset time for all of Maintenance?'), '配材重置未显示弹窗提示'

        robotic_maintence_page.yes
        robotic_maintence_page.is_toast_exist('', True, True), '配材一键重置失败，未显示成功toast提示'

    @pytest.mark.parametrize('check_account', ['laser_robotic'], indirect=True)
    def laser_robotic_stop_clean_no_record(self, check_account):
        """
        激光扫地机启动清扫后暂停不生成清扫记录:
        1. app首页点击进入设备主页，点击more进入设置界面，点击help
        2. 点击clean启动清扫，等待30s后点击stop暂停清扫，查看清扫历史记录
        【checkpoint】清扫暂停不显示清扫历史记录
        :return:
        """
        home_page.into_device_home_page(data.get_device('laser_robotic'))

        TestLaserRoboVac.laser_ready()

        robotic_home_page.into_clean_history()
        if robotic_clean_history_page.count_record() > 0:
            robotic_clean_history_page.clear_all()
            robotic_clean_history_page.commit_clear()
            robotic_clean_history_page.loading()
        robotic_clean_history_page.back_robovac()

        robotic_home_page.t2190_play()
        time.sleep(3)
        assert robotic_home_page.text_display('Pause'), 'laser_robotic 启动清扫失败'

        robotic_home_page.long_wait(20)
        robotic_home_page.t2190_play()
        robotic_home_page.into_clean_history()
        assert robotic_clean_history_page.count_record() == 0, 'laser_robotic 暂停清扫也生成了清扫记录'

    @pytest.mark.robovac
    @pytest.mark.laserrobotic
    @pytest.mark.run(order=232)
    @pytest.mark.parametrize('check_account', ['laser_robotic'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def test_laser_robotic_spot_make_record(self, check_account):
        """
        激光扫地机回充成功生成清扫记录:
        1. app首页点击进入设备主页，点击清扫按钮
        【checkpoint】扫地机状态为cleaning
        2. 点击recharge按钮，等待扫地机状态变为standard，查看清扫记录列表
        【checkpoint】检查历史记录列表是否新增清扫记录
        :return:
        """
        home_page.into_device_home_page(data.get_device('laser_robotic'))

        TestLaserRoboVac.laser_ready()

        robotic_home_page.into_clean_history()
        if robotic_clean_history_page.count_record() > 0:
            robotic_clean_history_page.clear_all()
            robotic_clean_history_page.commit_clear()
        robotic_clean_history_page.back_robovac()

        robotic_home_page.into_setting()
        robotic_setting_page.into_manual()
        robotic_manual_page.click_spot()
        time.sleep(3)
        robotic_manual_page.back_setting()
        robotic_setting_page.back_robovac()
        assert robotic_home_page.read_robovac_status() == data.get_robotic_status('cleaning'), '扫地机定点清扫失败'

        robotic_home_page.long_wait(30)
        robotic_home_page.t2190_play()
        robotic_home_page.t2190_stop_spot_clean()
        robotic_home_page.long_wait(60)
        robotic_home_page.into_clean_history()
        assert robotic_clean_history_page.count_record() == 1, 'laser_robotic 清扫回充成功后未生成清扫记录'

    @pytest.mark.robovac
    @pytest.mark.laserrobotic
    @pytest.mark.run(order=233)
    @pytest.mark.parametrize('desc', ['all', 'single'])
    @pytest.mark.parametrize('check_account', ['laser_robotic'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def test_laser_robotic_delete_clean_history(self, desc, check_account):
        """
        激光扫地机删除单条清扫记录:
        1. app首页点击进入设备主页，生成一条清扫记录
        2.点击clear全部清除
        【checkpoint】历史记录列表显示为空
        :return:
        """
        home_page.into_device_home_page(data.get_device('laser_robotic'))

        TestLaserRoboVac.laser_ready()

        robotic_home_page.into_clean_history()
        time.sleep(3)
        num = robotic_clean_history_page.count_record()
        if num == 0:
            robotic_clean_history_page.back_robovac()
            robotic_home_page.into_setting()
            robotic_setting_page.into_manual()
            robotic_manual_page.click_spot()
            time.sleep(5)
            robotic_manual_page.back_setting()
            robotic_setting_page.back_robovac()
            robotic_home_page.t2190_play()
            robotic_home_page.t2190_stop_spot_clean()
            robotic_home_page.long_wait(60)
            robotic_home_page.into_clean_history()

            if robotic_clean_history_page.count_record() == 0:
                assert False, 'laser_robotic 生成清扫历史记录失败'

        if desc == 'all':
            robotic_clean_history_page.clear_all()
            robotic_clean_history_page.commit_clear()
        elif desc == 'single':
            robotic_clean_history_page.delete_one_by_one()
        robotic_clean_history_page.back_robovac()
        robotic_home_page.into_clean_history()

        time.sleep(3)
        num_1 = robotic_clean_history_page.count_record()

        assert num_1 == 0, 'laser_robotic ' + desc + ' 删除清扫记录失败'

    @pytest.fixture(scope='function')
    def close_laser_schedule(self):
        """
        关闭扫地机及定时任务
        :return:
        """
        yield 1
        if GlobalVar.get_test_flag():
            if data.get_robotic_status('cleaning') == robotic_home_page.read_robovac_status():
                robotic_home_page.t2190_play()
            robotic_home_page.t2190_schedule()
        robotic_schedule_page.t2190_delete_schedule()

    @pytest.mark.run(order=234)
    @pytest.mark.robovac
    @pytest.mark.parametrize('check_account', ['laser_robotic'], indirect=True)
    def test_laser_robotic_schedule_time(self, check_account, close_laser_schedule):
        """
        激光扫地机设置定时任务：
        1.设置一个基于当前时间5min后的定时任务
        【checklist】检查定时任务列表的时间是否设置正确
        2.等待定时任务启动
        【checklist】检查定时任务启动后扫地机的状态
        :param check_account:
        :return:
        """
        home_page.into_device_home_page(data.get_device('laser_robotic'))
        TestLaserRoboVac.laser_ready()

        # 开启定点清扫，然后让扫地机为默认状态而不是暂停清扫状态
        robotic_home_page.into_setting()
        robotic_setting_page.into_manual()
        robotic_manual_page.click_spot()
        robotic_manual_page.back_setting()
        robotic_setting_page.back_robovac()
        time.sleep(5)

        if robotic_home_page.read_robovac_status() == data.get_robotic_status('cleaning'):
            robotic_home_page.t2190_play()
        robotic_home_page.t2190_schedule()
        robotic_schedule_page.t2190_delete_schedule()
        _t = robotic_schedule_page.t2190_creat_new_schedule(data.get_device('laser_robotic'), 5)

        assert _t == robotic_schedule_page.t2190_read_schedule_time(robotic_schedule_page.week_simple_name), '定时任务设置正确'
        robotic_schedule_page.back_robotic()

        GlobalVar.set_test_flag('t')  # 此处需要判断扫地机状态了

        robotic_home_page.long_wait(320)
        assert data.get_robotic_status('cleaning') in robotic_home_page.read_robovac_status(), '定时任务执行启动成功'

    @pytest.fixture(scope='function')
    def set_laser_robotic_name(self):
        """
        恢复设备名称
        :return:
        """
        yield 1
        if home_page.is_welcome():
            home_page.into_device_home_page(data.get_device('laser_robotic'))
        if robotic_home_page.text_display('T2190'):
            robotic_home_page.into_setting()
        if robotic_setting_page.read_device_name() != data.get_device('laser_robotic'):
            robotic_setting_page.change_device_name(data.get_device('laser_robotic'))
        robotic_setting_page.back_robovac()
        robotic_home_page.t2190_charge()
        robotic_home_page.long_wait(30)

    @pytest.mark.robovac
    @pytest.mark.laserrobotic
    @pytest.mark.run(order=235)
    @pytest.mark.parametrize('check_account', ['laser_robotic'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def test_laser_robotic_change_device_name(self, check_account, set_laser_robotic_name):
        """
        修改扫地机设备名称:
        1. app首页点击进入设备主页，点击更多，修改设备名称T2190_随机数
        【checkpoint】设备控制页名称显示正确
        【checkpoint】设备主页显示名称正确
        【checkpoint】app主页设备名显示正确
        :param check_account:
        :return:
        """
        home_page.into_device_home_page(data.get_device('laser_robotic'))

        TestLaserRoboVac.laser_ready()

        robotic_home_page.into_setting()
        _name = data.get_device('laser_robotic') + robotic_setting_page.get_str()

        robotic_setting_page.change_device_name(_name)
        assert _name in robotic_setting_page.read_device_name(), 'laser_robotic 扫地机修改名称后设置页面显示的名称不对'

        robotic_setting_page.back_robovac()
        assert _name in robotic_home_page.read_t2190_name(), 'laser_robotic 扫地机修改名称后设备主页面显示的名称不对'

        robotic_home_page.back_home()
        home_page.swipe_page('down')
        assert home_page.find_device(_name), 'laser_robotic 扫地机修改名称后app主页面显示的名称不对'

    @pytest.mark.robovac
    @pytest.mark.laserrobotic
    @pytest.mark.run(order=236)
    @pytest.mark.parametrize('check_account', ['laser_robotic'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def test_laser_robotic_remove(self, check_account):
        """
        移除激光扫地机设备：
        1. app首页点击进入设备主页，点击more进入设置界面
        2. 点击remove
        【checkpoint】弹出移除成功确认弹窗
        【checkpoint】返回app首页，设备列表不显示T2250
        :param check_account:
        :return:
        """
        if GlobalVar.get_remove_add() == 0:
            pytest.skip('本次指定不执行词条用例')

        home_page.into_device_home_page(data.get_device('laser_robotic'))

        TestLaserRoboVac.laser_ready()

        robotic_home_page.into_setting()
        robotic_setting_page.swipe_page('up')
        robotic_setting_page.click_remove()
        assert robotic_setting_page.text_display(
            'Are you sure you want to remove this device?'), 'laser_robotic 未显示删除设备提示弹窗'
        robotic_setting_page.commit_remove()
        robotic_setting_page.loading()
        home_page.swipe_page('down')
        assert home_page.find_device(data.get_device('laser_robotic')) is False, 'laser_robotic 扫地机移除之后主页还未删除'

    @pytest.fixture(scope='function')
    def reset_phone_network(self):
        """
        检查并重置手机网络，防止配网失败影响网络
        :return:
        """
        yield 1
        add_device_page.set_system_wifi(data.get_wifi('phone')[0])

    @pytest.mark.robovac
    @pytest.mark.laserrobotic
    @pytest.mark.run(order=237)
    @pytest.mark.parametrize('check_account', ['laser_robotic'], indirect=True)
    def test_laser_robotic_add_device(self, check_account, reset_phone_network):
        """
        添加激光扫地机:
        1. app首页点击+，选择robotic，选择 RoboVac 30C max
        2. 点击Next，勾选 Status Confirmed，点击 next
        3. 选择亚添加的设备id
        4. 连接中，等待conecting消失
        【checkpoint】判断是否显示添加成功（文本校验）
        5. 修改设备昵称未T2150，点击保存
        6. 返回设备主页查看设备列表
        【checkpoint】首页列表刷新后显示扫地机T2190
        :param check_account:
        :return:
        """
        if GlobalVar.get_remove_add() == 0:
            GlobalVar.set_test_flag('f')
            pytest.skip('本次指定不执行词条用例')

        home_page.swipe_page('down')
        if home_page.find_device(data.get_device('laser_robotic')):
            home_page.into_device_home_page(data.get_device('laser_robotic'))

            TestLaserRoboVac.laser_ready()

            robotic_home_page.into_setting()
            robotic_setting_page.swipe_page('up')
            robotic_setting_page.click_remove()
            robotic_setting_page.commit_remove()
            robotic_setting_page.loading()

        home_page.click_add_device()
        add_device_page.click_robotic()
        add_device_page.select_robotic('L70 Hybrid')
        wifi_data = data.get_wifi('laser_robotic')
        add_device_page.set_wifi(wifi_data[0], wifi_data[1])
        add_device_page.confirm_status()
        add_device_page.select_robotic_by_id(data.get_device_udid('laser_robotic'))
        add_device_page.loading()

        add_device_page.wait_connect()
        assert add_device_page.connect_result(), 'inertia_robotic 配网连接失败'
        add_device_page.set_device_name(data.get_device('laser_robotic'))
        add_device_page.ok
        add_device_page.loading()

        home_page.swipe_page('down')
        assert home_page.find_device(data.get_device('laser_robotic')), 'laser_robotic 配网成功后首页未查找到T2190设备'
