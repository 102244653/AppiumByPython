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

from src.eufyhome.method.switch.SwitchHome_Page import SwitchHomePage
from src.eufyhome.method.switch.SwitchSchedule_Page import SwitchSchedulePage
from src.eufyhome.method.switch.SwitchSetting_Page import SwitchSettingPage
from src.eufyhome.method.switch.SwitchTimer_Page import SwitchTimerPage
from src.eufyhome.method.switch.SwitchUpdate_Page import SwitchUpdatePage

global base_page, start_page, user_page, time_zone_page, system_page, news_page, change_pw_page, home_page, \
            all_share_page,  help_faq_page, share_setting_page, add_device_page, device_help_page, switch_home_page, \
            switch_setting_page,switch_timer_page, switch_schedule_page, switch_update_page


# @pytest.mark.flaky(reruns=0)  # 失败重跑
@pytest.mark.repeat(0)  # 重复执行次数
@pytest.mark.usefixtures('driver_setup')  # 引用conftest.py中的driver_setup方法，创建会话
@pytest.mark.usefixtures('appium_setup')  # 引用conftest.py中的appium_setup方法，启动appium服务
class TestSwitch(object):
    @pytest.fixture(scope='function')
    def init_setup(self):
        """
        使用 @pytest.fixture(scope='function') 装饰器的方法可以看做是setup方法
        scope指定级别，取值可以是"function"(default),"class","module","package" or "session"
        :return:
        """
        global base_page, start_page, user_page, time_zone_page, system_page, news_page, change_pw_page, home_page, \
            all_share_page,  help_faq_page, share_setting_page, add_device_page, device_help_page, switch_home_page, \
            switch_setting_page,switch_timer_page, switch_schedule_page, switch_update_page

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

        switch_home_page = SwitchHomePage(self.driver)
        switch_setting_page = SwitchSettingPage(self.driver)
        switch_timer_page = SwitchTimerPage(self.driver)
        switch_schedule_page = SwitchSchedulePage(self.driver)
        switch_update_page = SwitchUpdatePage(self.driver)

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
                TestSwitch.change_account(account)
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
    def switch_ready():
        switch_home_page.skip_switch_guide()
        if switch_home_page.is_offline:
            switch_home_page.ok
            if switch_home_page.switch_is_offline() is False:
                assert False, 'switch 设备处于离线状态'
        switch_home_page.ignore_update()

    # ********************开关用例************************** #
    @pytest.mark.switch
    @pytest.mark.run(order=500)
    @pytest.mark.parametrize('check_account', ['switch'], indirect=True)
    def switch_check_update_icon(self, check_account):
        """
        设备升级提示图标检查:
        1. app首页点击进入设备主页
        【checkpoint】首页设备列表是否显示升级图标
        :param check_account:
        :return:
        """
        home_page.swipe_page('down')
        assert home_page.have_update_icon(data.get_device('switch')), 'random_robotic 未显示升级图标'

        home_page.click_update_icon(data.get_device('switch'))
        assert home_page.text_display('Firmware Update'), 'switch OTA升级快捷入口进入失败'

    @pytest.fixture(scope='function')
    def switch_off(self):
        """
        关闭开关
        :return:
        """
        yield 1
        if home_page.is_welcome():
            home_page.into_device_home_page()
        if switch_home_page.read_deivce_status() == 'ON':
            switch_home_page.click_switch_btn()
            time.sleep(2)

    @pytest.mark.switch
    @pytest.mark.run(order=502)
    @pytest.mark.parametrize('check_account', ['switch'], indirect=True)
    @pytest.mark.flaky(reruns=2, reruns_delay=40)
    def test_switch_play(self, check_account, switch_off):
        """
        app设备列表操作开关:
        1. app首页点击进入设备主页，点击设备开关
        【checkpoint】首页列表的插座开关显示on
        2. 返回设备列表，检查开关状态
        【checkpoint】开关状态为on
        3.点击列表的设备开关
        【checkpoint】开关状态为off
        4.进入设备主页，检查开关状态
        【checkpoint】设备状态显示off
        :param check_account:
        :return:
        """
        home_page.into_device_home_page(data.get_device('switch'))

        TestSwitch.switch_ready()
        # switch_home_page.skip_switch_guide()
        # if switch_home_page.is_offline:
        #     switch_home_page.ok
        #     if switch_home_page.switch_is_offline() is False:
        #         assert False, 'switch 设备处于离线状态'
        #
        # switch_home_page.ignore_update()

        switch_home_page.click_switch_btn()
        status_1 = switch_home_page.read_deivce_status()

        switch_home_page.back_home()
        status_2 = home_page.read_device_status(data.get_device('switch'))

        assert status_1 == status_2 == 'ON', 'switch 打开设备后状态显示错误，设备列表：'+str(status_2)+' 设备主页：'+str(status_1)

        home_page.click_device_btn(data.get_device('switch'))
        time.sleep(2.5)
        status_3 = home_page.read_device_status(data.get_device('switch'))

        home_page.into_device_home_page(data.get_device('switch'))
        status_4 = switch_home_page.read_deivce_status()

        assert status_3 == status_4 == 'OFF', 'switch 关闭设备后状态显示错误，设备列表：'+str(status_3)+' 设备主页：'+str(status_4)

    @pytest.mark.switch
    @pytest.mark.run(order=503)
    @pytest.mark.parametrize('check_account', ['switch'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def test_switch_add_and_delete_schedule(self, check_account):
        """
        新增和删除一个定时任务:
        1. 进入app首页，点击设备开关
        2.点击shecdule进入设备定时任务界面，新增定时任务，日期选择当天
        3.点击save保存
        【checkpoint】提示新增成功确认弹窗
        【checkpoint】返回定时任务列表显示定时任务，时间为当天
        4.在列表左滑删除定时任务
        【checkpoint】定时任务列表显示为空
        :param check_account:
        :param switch_off:
        :return:
        """
        home_page.into_device_home_page(data.get_device('switch'))

        TestSwitch.switch_ready()

        switch_home_page.into_schedules()
        if switch_schedule_page.count_schedule()>0:
            switch_schedule_page.delete_schedule()

        switch_schedule_page.add_new_schedule()
        time.sleep(3)
        assert switch_schedule_page.count_schedule() == 1, 'switch 添加定时任务失败'
        week = data.get_week_by_id(str(switch_schedule_page.week_id))
        assert switch_schedule_page.text_display(week), 'switch 定时任务日期显示错误'

        switch_schedule_page.delete_schedule()
        time.sleep(2.5)
        assert switch_schedule_page.count_schedule() == 0, 'switch 删除定时任务失败'

    @pytest.mark.switch
    @pytest.mark.run(order=504)
    @pytest.mark.parametrize('desc,yt', [('ON', 2), ('OFF', 1)])
    @pytest.mark.parametrize('check_account', ['switch'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def test_switch_add_timer(self, desc, yt, check_account, switch_off):
        """
        新增一个倒计时任务:(默认一分钟)
        1.进入设备主页，点击定时器新增一个开启快关的倒计时，默认为1min
        【checkpoint】1分钟后检查设备状态
        2.新增一个关闭快关的倒计时，默认为1min
        【checkpoint】1分钟后检查设备状态
        :param check_account:
        :return:
        """
        home_page.into_device_home_page(data.get_device('switch'))

        TestSwitch.switch_ready()

        if desc == 'OFF' and switch_home_page.read_deivce_status() == 'OFF':
            switch_home_page.click_switch_btn()
            time.sleep(2.5)

        switch_home_page.into_timer()
        switch_timer_page.set_timer(desc, yt)
        switch_timer_page.start_timer()
        switch_timer_page.loading()

        switch_timer_page.long_wait(yt*60+10)
        switch_timer_page.back_switch()
        assert desc in switch_home_page.read_deivce_status(), 'switch 倒计时结束后状态显示错误'

    @pytest.mark.switch
    @pytest.mark.run(order=505)
    @pytest.mark.parametrize('email,expect', [('a@a', 'Please enter a valid')])
    @pytest.mark.parametrize('check_account', ['switch'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def test_switch_share_error_email(self, check_account, email, expect):
        """
        智能开关分享给错误格式账号：
        1. 点击智能开关进入扫地机主页，点击 more进入设置界面，点击share setting进入分享列表
        2. 点击 add 按钮进入添加界面，输入分享账号：a@a并提交
        【checkpoint】分享失败，toast提示：Please enter a vailed email adress
        :param check_account:
        :return:
        """
        home_page.into_device_home_page(data.get_device('switch'))

        TestSwitch.switch_ready()

        switch_home_page.into_setting()
        switch_setting_page.into_share()

        share_setting_page.add_share()
        share_setting_page.commit_share(email)

        if share_setting_page.platform == 'ios':
            flag = share_setting_page.text_display('Add Member')
        else:
            flag = share_setting_page.text_display(expect)
        assert flag, 'switch 分享错误邮箱的结果异常'

    @pytest.mark.switch
    @pytest.mark.run(order=506)
    @pytest.mark.parametrize('check_account', ['switch'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def test_switch_share_nosign_email(self, check_account):
        """
        智能开关分享给未注册的账号:
        1. 点击智能开关进入扫地机主页，点击 more进入设置界面，点击share setting进入分享列表
        2. 点击 add 按钮进入添加界面，输入分享账号：a@a.com并提交
        【checkpoint】分享失败，弹窗提示：Failed to share
        :return:
        """
        home_page.into_device_home_page(data.get_device('switch'))

        TestSwitch.switch_ready()

        switch_home_page.into_setting()
        switch_setting_page.into_share()

        share_setting_page.add_share()
        share_setting_page.commit_share('abc@test.com')
        assert share_setting_page.share_result() is False, 'switch 分享失败的提示错误'

    @pytest.fixture(scope='function')
    def delete_refuse_share_account(self):
        """
        先删除refuseshare账号分享列表
        :return:
        """
        home_page.into_system()
        system_page.into_sharing()
        all_share_page.into_device(data.get_device('switch'))
        share_setting_page.delete_share()
        all_share_page.kill
        time.sleep(2)
        all_share_page.open

    @pytest.mark.switch
    @pytest.mark.run(order=507)
    @pytest.mark.parametrize('check_account', ['switch'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def test_switch_share_email(self, check_account, delete_refuse_share_account):
        """
        智能开关分享给已注册的账号：
        1. 点击智能开关进入扫地机主页，点击 more进入设置界面，点击share setting进入分享列表
        2. 点击 add 按钮进入添加界面，输入分享账号：Yi@aa.com并提交
        【checkpoint】 分享邀请发送成功，弹窗提示：Successed to share
        【checkpoint】页面返回到分享列表并显示分享人，状态为：待确认
        :param check_account:
        :return:
        """
        home_page.into_device_home_page(data.get_device('switch'))

        TestSwitch.switch_ready()

        switch_home_page.into_setting()
        switch_setting_page.into_share()
        share_setting_page.add_share()
        share_setting_page.commit_share(data.get_account('share'))

        assert share_setting_page.share_result(), 'switch 正确账号分享失败'
        share_setting_page.ok
        share_setting_page.loading()
        status = share_setting_page.read_share_status(data.get_username('share'))
        assert status == 'Awaiting Confirmation' or status == 'Pending Confirmation', '分享列表被分享者状态显示错误'

    @pytest.mark.switch
    @pytest.mark.run(order=508)
    @pytest.mark.parametrize('check_account', ['switch'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def test_switch_agree_share(self, check_account, delete_share_news):
        """
        智能开关被分享者接受分享:
        1. 登陆账号Yi@aa.com/12345678
        【checkpoint】登陆账号为Yi@aa.com
        2. 点击进入侧边栏界面
        【checkpoint】消息通知显示分享通知红点标识
        3. 点击news进入消息界面
        【checkpoint】显示分享邀请消息记录
        4. 点击最新一条分享邀请通知，点击ok按钮
        【checkpoint】点击ok按钮弹窗提示分享成功
        :param check_account:
        :return:
        """
        home_page.into_device_home_page(data.get_device('switch'))

        TestSwitch.switch_ready()

        switch_home_page.into_setting()
        switch_setting_page.into_share()

        status = share_setting_page.read_share_status(data.get_username('share'))
        if status not in ['Awaiting Confirmation', 'Pending Confirmation']:
            share_setting_page.add_share()
            share_setting_page.commit_share(data.get_account('share'))
            assert share_setting_page.share_result(), 'switch 正确账号分享失败,无法执行用例:[test_bulbs_agree_share]'
            share_setting_page.ok
            share_setting_page.loading()

        share_setting_page.back_setting()
        switch_setting_page.back_switch()
        switch_home_page.back_home()
        TestSwitch.change_account('share')
        home_page.into_system()

        system_page.into_sharing()
        assert all_share_page.text_display(data.get_device('switch')), '被分享列表未显示分享设备信息'
        GlobalVar.set_test_flag('t')  # 到这里后需要执行 tear_down
        all_share_page.into_device(data.get_device('switch'))
        all_share_page.yes
        all_share_page.loading()

        assert all_share_page.text_display('Request Accepted. You may now use this device.'), '被分享者确认接受分享失败'
        all_share_page.ok
        assert all_share_page.text_display('switch shared a ' + data.get_device('switch').strip()), '被分享者显示的分享设备名称错误'

        news_page.back_system()
        news_page.back_system()
        system_page.back_home()
        home_page.swipe_page('down')
        assert home_page.find_device(data.get_device('switch')), '被分享者未显示分享的switch设备'

    @pytest.fixture(scope='function')
    def switch_close_yellow_tip(self):
        """
        关闭小黄条提示
        :return:
        """
        yield 1
        if GlobalVar.get_test_flag():
            switch_schedule_page.close_yellow_tip()

    @pytest.mark.switch
    @pytest.mark.run(order=509)
    @pytest.mark.parametrize('check_account', ['share'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def switch_close_yellow_tip(self, switch_close_yellow_tip, check_account):
        """
        智能开关被分享者修改设备名及小黄条显示:
        1. app首页点击进入设备主页，修改一个定时任务
        2.切换账号 Yi@aaa.com，查看智能开关设备
        【checkpoint】显示设备名称修改小黄条
        :return:
        """
        if home_page.find_device(data.get_device('switch')) is False:
            assert False, '未查找到分享设备，无法执行用:[test_switch_close_yellow_tip]'

        home_page.into_device_home_page(data.get_device('switch'))

        TestSwitch.switch_ready()

        switch_home_page.into_schedules()
        switch_schedule_page.click_away_mode()
        switch_schedule_page.back_switch()
        switch_home_page.back_home()

        TestSwitch.change_account('switch')

        home_page.into_device_home_page(data.get_device('switch'))
        switch_home_page.skip_switch_guide()
        if switch_home_page.is_offline:
            switch_home_page.ok
            if switch_home_page.switch_is_offline() is False:
                assert False, 'switch 设备处于离线状态'

        switch_home_page.into_schedules()
        GlobalVar.set_test_flag('t')

        assert switch_schedule_page.text_display('share modified the schedule'), '被分享人修改了定时任务未显示小黄条提示'

    @pytest.mark.switch
    @pytest.mark.run(order=510)
    @pytest.mark.parametrize('check_account', ['share'], indirect=True)
    def test_switch_delete_share(self, check_account):
        """
        智能开关被分享者移除分享设备:
        1. app首页点击进入设备主页，点击更多，点击删除设备
        【checkpoint】弹窗提示确认移除
        2.点击 ok 按钮
        【checkpoint】分享者列表不显示被分享人信息
        3.切换账号Yi@aaa.com，查看设备分享列表
        【checkpoint】分享者列表不显示被分享人信息
        :return:
        """
        home_page.swipe_page('down')
        assert home_page.find_device(data.get_device('switch')), '为查找到分享设备，无法执行用:[test_switch_delete_share]'

        home_page.into_device_home_page(data.get_device('switch'))

        TestSwitch.switch_ready()

        switch_home_page.into_setting()
        switch_setting_page.click_remove()
        assert switch_setting_page.text_display('Are you sure you want to remove this device?'), '未显示移除确认弹窗'
        switch_setting_page.commit_remove()
        home_page.swipe_page('down')
        assert home_page.find_device(data.get_device('switch')) is False, '被分享着移除后设备未删除'

        TestSwitch.change_account('switch')

        home_page.into_device_home_page(data.get_device('switch'))
        switch_home_page.skip_switch_guide()
        if switch_home_page.is_offline:
            switch_home_page.ok
            if switch_home_page.switch_is_offline() is False:
                assert False, 'switch 设备处于离线状态'

        switch_home_page.into_setting()
        switch_setting_page.into_share()
        assert data.get_username('share') not in share_setting_page.read_share_to_me_list(), '分享列表显示已移除的分享者信息'

    @pytest.mark.switch
    @pytest.mark.run(order=511)
    @pytest.mark.parametrize('check_account', ['switch'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def test_switch_refuse_share(self, delete_share_news, check_account, delete_refuse_share_account):
        """
        智能开关被分享者拒绝接受分享：
        1. 点击智能开关进入扫地机主页，点击 more进入设置界面，点击share setting进入分享列表
        2. 点击 add 按钮进入添加界面，输入分享账号：Yi@aa.com并提交
        【checkpoint】 分享邀请发送成功，弹窗提示：Successed to share
        3.重启app切换账号Yi@aa.com，进入分享消息记录
        4.点击拒绝接受分享按钮
        【checkpoint】显示已拒绝分享弹窗
        【chenckpoint】app首页不显示分享设备
        5.切换至分享者账号，检查分享列表
        【checkpoint】不显示已拒绝的分享人
        :param check_account:
        :return:
        """
        home_page.into_device_home_page(data.get_device('switch'))

        TestSwitch.switch_ready()

        switch_home_page.into_setting()
        switch_setting_page.into_share()
        share_setting_page.add_share()
        share_setting_page.commit_share(data.get_account('refuseshare'))
        assert share_setting_page.share_result(), 'switch 正确账号分享失败'
        share_setting_page.ok
        share_setting_page.loading()

        share_setting_page.back_setting()
        switch_setting_page.back_switch()
        switch_home_page.back_home()

        TestSwitch.change_account('refuseshare')
        GlobalVar.set_test_flag('t')

        home_page.into_system()
        system_page.into_sharing()
        all_share_page.into_device(data.get_device('switch'))
        all_share_page.no
        assert all_share_page.text_display('Request Declined. This device will be removed.'), 'switch 被分享者拒绝接受分享失败'
        all_share_page.ok
        all_share_page.loading()

        all_share_page.back_system()
        system_page.back_home()
        home_page.swipe_page('down')
        assert home_page.find_device(data.get_device('switch')) is False, 'app首页被分享者拒绝分享后显示分享了扫地机设备'

    @pytest.mark.switch
    @pytest.mark.run(order=511)
    @pytest.mark.parametrize('check_account', ['switch'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def test_switch_check_schedule_icon(self, check_account):
        """
        检查定时任务图标是否显示：
        1.进入app主页，检查是否显示定时任务图标
        2.如果未显示则去开启一个定时任务，并返回app首页
        【checkpoint】检查设备是否显示定时任务图标
        :return:
        """
        home_page.swipe_page('down')
        status = home_page.have_schedule_icon(data.get_device('switch'))

        if not status:
            home_page.into_device_home_page(data.get_device('switch'))

            TestSwitch.switch_ready()

            switch_home_page.into_schedules()
            if not switch_schedule_page.read_away_mode_status():
                switch_schedule_page.click_away_mode()
            switch_schedule_page.back_switch()
            switch_home_page.back_home()
            home_page.swipe_page('down')
            status = home_page.have_schedule_icon(data.get_device('switch'))

        assert status, 'switch 未显示定时任务图标'

        home_page.click_schedule_icon(data.get_device('switch'))
        assert home_page.text_display('Schedules'), 'switch 定时任务快捷图标进入失败'

    @pytest.fixture(scope='function')
    def close_switch_schedule(self):
        """
        关闭扫地机及定时任务
        :return:
        """
        yield 1
        if GlobalVar.get_test_flag():
            if switch_home_page.read_deivce_status() == 'ON':
                switch_home_page.click_switch_btn()
            switch_home_page.into_schedules()
        switch_schedule_page.delete_schedule()

    @pytest.mark.run(order=512)
    @pytest.mark.switch
    @pytest.mark.parametrize('check_account', ['switch'], indirect=True)
    def test_switch_schedule_time(self, check_account, close_switch_schedule):
        """
        智能开关设置定时任务：
        1.设置一个基于当前时间5min后的定时任务
        【checklist】检查定时任务列表的时间是否设置正确
        2.等待定时任务启动
        【checklist】检查定时任务启动后灯泡的状态
        :param check_account:
        :return:
        """
        home_page.into_device_home_page(data.get_device('switch'))
        TestSwitch.switch_ready()

        if switch_home_page.read_deivce_status() == 'ON':
            switch_home_page.click_switch_btn()
        switch_home_page.into_schedules()
        _t = switch_schedule_page.add_new_schedule(data.get_device('switch'), 5)

        assert _t == switch_home_page.read_schedule_time(switch_schedule_page.week_simple_name), '定时任务设置正确'
        switch_schedule_page.back_switch()

        GlobalVar.set_test_flag('t')  # 此处需要判断设备状态了

        switch_home_page.long_wait(320)
        assert 'ON' in switch_home_page.read_deivce_status(), '定时任务执行启动成功'

    @pytest.mark.debug
    @pytest.mark.run(order=513)
    @pytest.mark.parametrize('check_account', ['switch'], indirect=True)
    def test_switch_away_mode(self, check_account):
        """
        插座离家模式：
        1.开启离家模式，设置启动时间2分钟之后开始，时间5min
        2.判断在5分钟之内是否有开启和关闭操作
        :return:
        """
        home_page.into_device_home_page(data.get_device('switch'))
        TestSwitch.switch_ready()

        status = switch_home_page.read_deivce_status()
        if status == 'ON':
            switch_home_page.click_switch_btn()
            status == 'OFF'
        switch_home_page.into_schedules()

        switch_schedule_page.edit_switch_away_mode(3)

        switch_schedule_page.swipe_page('down')
        assert switch_schedule_page.read_away_mode_status(), '离家模式开启失败'

        switch_schedule_page.back_switch()
        switch_home_page.long_wait(60)

        kk = 0  # 状态变化两次则算成功
        for i in range(11):
            text = switch_home_page.read_deivce_status()
            if text != status:
                status = text
                kk += 1
            else:
                switch_home_page.long_wait(20)
            if kk == 2:
                break

        assert kk == 2, '离家模式开启后 180S 未监测到插座开启和关闭'

    @pytest.mark.switch
    @pytest.mark.run(order=513)
    @pytest.mark.parametrize('check_account', ['switch'], indirect=True)
    def switch_help_title(self, check_account):
        """
        智能开关help列表数量统计:
        1. app首页点击进入设备主页，点击more进入设置界面，点击help
        2. 遍历help页面的问答列表
        【checkpoint】 统计help列表总数=
        【checkpoint】遍历help列表的标题是否正确
        :return:
        """
        home_page.into_device_home_page(data.get_device('switch'))
        switch_home_page.skip_switch_guide()
        if switch_home_page.is_offline:
            switch_home_page.ok

        switch_home_page.ignore_update()
        switch_home_page.into_setting()
        switch_setting_page.into_help()

        title_list = device_help_page.read_help_title()
        assert len(title_list) != 0, 'switch help列表显示为空'
        # expect_list = data.read_json(data.get_device('switch'))
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
        # assert num and flag, 'switch help列表总数：' + str(num) + ',与预期相比缺少：' + str(expect_titles) + ',与实际相比多出：' + str(actual_titles)

    @pytest.mark.switch
    @pytest.mark.run(order=514)
    @pytest.mark.parametrize('check_account', ['switch'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def switch_help_feedback(self, check_account):
        """
        插座help的反馈界面：
        1. app首页点击进入设备主页，点击more进入设置界面，点击help
        2.点击进入feedback页面，点击submit按钮
        【checkpoint】检查是否有toast提示：feedback field cannot be blank
        :param check_account:
        :return:
        """
        home_page.into_device_home_page(data.get_device('switch'))
        switch_home_page.skip_switch_guide()
        if switch_home_page.is_offline:
            switch_home_page.ok

        switch_home_page.ignore_update()
        switch_home_page.into_setting()
        switch_setting_page.into_help()

        device_help_page.into_feed_back()
        device_help_page.submit_feed_back('switch test feedback')
        assert device_help_page.is_help_page(), 'switch 提交反馈失败'

    @pytest.mark.switch
    @pytest.mark.run(order=515)
    @pytest.mark.parametrize('check_account', ['switch'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def switch_help_chat(self, check_account):
        """
        插座help的chat界面:
        1. app首页点击进入设备主页，点击more进入设置界面，点击help
        2.进入chat界面，发送一条消息
        【checkpoint】页面显示是否正常
        :param check_account:
        :return:
        """
        home_page.into_device_home_page(data.get_device('switch'))
        switch_home_page.skip_switch_guide()
        if switch_home_page.is_offline:
            switch_home_page.ok

        switch_home_page.into_setting()
        switch_setting_page.into_help()
        device_help_page.into_chat()
        assert device_help_page.text_display('Chat With Eufy'), 'switch 进入chat聊天界面无响应'

    @pytest.mark.switch
    @pytest.mark.run(order=516)
    @pytest.mark.parametrize('check_account', ['switch'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def _switch_help_telphone(self, check_account):
        """
        插座help的电话界面：
        :param check_account:
        :return:
        """
        home_page.into_device_home_page(data.get_device('switch'))
        switch_home_page.skip_switch_guide()
        if switch_home_page.is_offline:
            switch_home_page.ok

        switch_home_page.ignore_update()
        switch_home_page.into_setting()
        switch_setting_page.into_help()
        device_help_page.into_call_us()

        us = data.get_phone('us') in device_help_page.read_phone_number('us')
        uk = data.get_phone('uk') in device_help_page.read_phone_number('uk')
        de = data.get_phone('de') in device_help_page.read_phone_number('de')
        jp = data.get_phone('jp') in device_help_page.read_phone_number('jp')
        assert us and uk and de and jp, 'switch 客服联系电话显示错误：us=' + str(us) + ';uk=' + str(uk) + ';de=' + str(
            de) + ';jp=' + str(jp)

    @pytest.fixture(scope='function')
    def set_switch_name(self):
        """
        恢复设备名
        :return:
        """
        yield 1
        if GlobalVar.get_test_flag():
            if home_page.is_welcome():
                home_page.into_device_home_page(data.get_device('switch'))
            if switch_home_page.is_switch_home():
                switch_home_page.into_setting()
            switch_setting_page.change_switch_name(data.get_device('switch'))
            time.sleep(1.5)

    @pytest.mark.switch
    @pytest.mark.run(order=517)
    @pytest.mark.parametrize('check_account', ['switch'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def test_switch_change_name(self, check_account, set_switch_name):
        """
        修改开关的设备名：
        1. app首页点击进入设备主页，点击more进入设置界面
        2.修改设备名称
        【checkpoint】检查设置界面的昵称是否修改正确
        3。返回设备主页
        【checkpoint】检查设备主页界面的昵称是否修改正确
        4。返回app主页
        【checkpoint】检查app列表界面的昵称是否修改正确
        :return:
        """
        home_page.into_device_home_page(data.get_device('switch'))

        TestSwitch.switch_ready()

        new_name = data.get_device('switch') + switch_home_page.get_str()
        switch_home_page.into_setting()
        switch_setting_page.change_switch_name(new_name)

        GlobalVar.set_test_flag('t')

        assert new_name in switch_setting_page.read_switch_name(), 'switch 修改昵称后设置界面名称错误'

        switch_setting_page.back_switch()
        time.sleep(3)
        assert new_name in switch_home_page.read_switch_name(), 'switch 修改昵称后设备主页界面名称错误'

        switch_home_page.back_home()
        assert home_page.find_device(new_name), 'switch 修改昵称后设备列表名称错误'

    @pytest.mark.switch
    @pytest.mark.run(order=518)
    @pytest.mark.parametrize('check_account', ['switch'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def test_switch_remove(self, check_account):
        """
        移除智能开关：
        1. app首页点击进入设备主页，点击more进入设置界面
        2. 点击remove
        【checkpoint】弹出移除成功确认弹窗
        【checkpoint】返回app首页，设备列表不显示switch
        :return:
        """
        if GlobalVar.get_remove_add() == 0:
            pytest.skip('本次指定不执行词条用例')

        home_page.into_device_home_page(data.get_device('switch'))

        TestSwitch.switch_ready()

        switch_home_page.into_setting()
        switch_setting_page.click_remove()

        assert switch_setting_page.text_display('Are you sure you want to remove this device?'), 'switch 移除未显示确认弹窗'
        switch_setting_page.commit_remove()
        switch_setting_page.loading()
        assert home_page.is_welcome(), 'switch 移除后未返回app首页'
        home_page.swipe_page('down')
        assert home_page.find_device(data.get_device('switch')) is False, 'switch 移除后设备列表未删除设备'

    @pytest.fixture(scope='function')
    def reset_phone_network(self):
        """
        检查并重置手机网络，防止配网失败影响网络
        :return:
        """
        yield 1
        if GlobalVar.get_test_flag():
            add_device_page.set_system_wifi(data.get_wifi('phone')[0])

    @pytest.mark.switch
    @pytest.mark.run(order=519)
    @pytest.mark.parametrize('check_account', ['switch'], indirect=True)
    def test_switch_add_device(self, check_account, reset_phone_network):
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
        if home_page.find_device(data.get_device('switch')):
            home_page.into_device_home_page(data.get_device('switch'))

            TestSwitch.switch_ready()

            switch_home_page.into_setting()
            switch_setting_page.click_remove()
            switch_setting_page.commit_remove()
            switch_setting_page.loading()

        home_page.click_add_device()
        add_device_page.click_switch()
        add_device_page.skip_switch_guide()
        add_device_page.select_switch_by_udid(data.get_device_udid('switch'))
        wifi_date = data.get_wifi('switch')
        add_device_page.select_wifi_with_switch(wifi_date[0], wifi_date[1])

        add_device_page.wait_connect()
        assert add_device_page.connect_result(), 'switch 配网连接失败'
        add_device_page.set_device_name(data.get_device('switch'))
        add_device_page.ok
        add_device_page.loading()

        home_page.swipe_page('down')
        assert home_page.find_device(data.get_device('switch')), 'switch 配网成功后首页未查找到设备'
