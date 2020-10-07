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

from src.eufyhome.method.bulbs.BulbsHome_Page import BulbsHomePage
from src.eufyhome.method.bulbs.BulbsEffect_Page import BulbsEffectPage
from src.eufyhome.method.bulbs.BulbsFavorite_Page import BulbsFavoritePage
from src.eufyhome.method.bulbs.BulbsSetting_Page import BulbsSettingPage
from src.eufyhome.method.bulbs.BulbsGroup_Page import BulbsGroupPage
from src.eufyhome.method.bulbs.BulbsDefaultLight_Page import BulbsDefaultLightPage
from src.eufyhome.method.bulbs.BulbsSchedule_Page import BulbsSchedulePage
from src.eufyhome.method.bulbs.BulbsGroupHome_Page import BulbsGroupHomePage
from src.eufyhome.method.bulbs.BulbsUpdate_Page import BulbsUpdatePage

global base_page, start_page, user_page, time_zone_page, system_page, news_page, change_pw_page, home_page, \
            all_share_page,  help_faq_page, share_setting_page, add_device_page, bulbs_default_light_page, device_help_page, \
            bulbs_schedule_page, bulbs_group_home_page, bulbs_update_page, bulbs_home_page, bulbs_effect_page, bulbs_favorite_page,\
            bulbs_setting_page, bulbs_group_page


# @pytest.mark.flaky(reruns=0)  # 失败重跑
@pytest.mark.repeat(0)  # 重复执行次数
@pytest.mark.usefixtures('driver_setup')  # 引用conftest.py中的driver_setup方法，创建会话
@pytest.mark.usefixtures('appium_setup')  # 引用conftest.py中的appium_setup方法，启动appium服务
class TestBulbs(object):

    @pytest.fixture(scope='function')
    def init_setup(self):
        """
        使用 @pytest.fixture(scope='function') 装饰器的方法可以看做是setup方法
        scope指定级别，取值可以是"function"(default),"class","module","package" or "session"
        :return:
        """
        global base_page, start_page, user_page, time_zone_page, system_page, news_page, change_pw_page, home_page, \
            all_share_page,  help_faq_page, share_setting_page, add_device_page, bulbs_default_light_page, device_help_page, \
            bulbs_schedule_page, bulbs_group_home_page, bulbs_update_page, bulbs_home_page, bulbs_effect_page, bulbs_favorite_page,\
            bulbs_setting_page, bulbs_group_page

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

        bulbs_home_page = BulbsHomePage(self.driver)
        bulbs_effect_page = BulbsEffectPage(self.driver)
        bulbs_favorite_page = BulbsFavoritePage(self.driver)
        bulbs_setting_page = BulbsSettingPage(self.driver)
        bulbs_group_page = BulbsGroupPage(self.driver)
        bulbs_default_light_page = BulbsDefaultLightPage(self.driver)
        bulbs_schedule_page = BulbsSchedulePage(self.driver)
        bulbs_group_home_page = BulbsGroupHomePage(self.driver)
        bulbs_update_page = BulbsUpdatePage(self.driver)

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
                TestBulbs.change_account(account)
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
    def bulbs_ready():
        bulbs_home_page.skip_bulbs_guide()
        if bulbs_home_page.is_offline:
            bulbs_home_page.ok
            if bulbs_home_page.bulbs_is_offline() is False:
                assert False, 'bulb设备处于离线状态'
        bulbs_home_page.ignore_update()

    # ********************灯泡用例************************** #

    @pytest.mark.bulbs
    @pytest.mark.run(order=700)
    @pytest.mark.parametrize('check_account', ['bulbs'], indirect=True)
    def _white_bulbs_check_update_icon(self, check_account):
        """
        设备升级提示图标检查:
        1. app首页点击进入设备主页
        【checkpoint】首页设备列表是否显示升级图标
        :param check_account:
        :param bulb:
        :return:
        """
        home_page.swipe_page('down')
        assert home_page.have_update_icon(data.get_device('white_bulbs')), 'white_bulbs 未显示升级图标'

        home_page.click_update_icon(data.get_device('white_bulbs'))
        assert home_page.text_display('Firmware Update'), 'white_bulbs OTA升级快捷入口进入失败'

    @pytest.fixture(scope='function')
    def bulbs_off(self):
        """
        灯泡后置操作：关闭灯泡
        :return:
        """
        yield 1
        if home_page.is_welcome():
            if home_page.read_device_status(data.get_device('white_bulbs')) == 'ON':
                home_page.click_device_btn(data.get_device('white_bulbs'))
        elif bulbs_home_page.bulb_status(False):
            bulbs_home_page.click_bulbs()

    @pytest.mark.bulbs
    @pytest.mark.run(order=701)
    @pytest.mark.parametrize('check_account', ['bulbs'], indirect=True)
    @pytest.mark.flaky(reruns=2, reruns_delay=60)
    def test_white_bulbs_on_off(self, check_account, bulbs_off):
        """
        智能灯泡的点亮/熄灭：
        1. 点击灯泡进入设备主页,检查灯泡状态并记录，点击灯泡
        【checkpoint】检查灯泡状态
        2.返回app首页
        【checkpoint】检查灯泡开关状态是否显示正确
        3. 点击灯泡开关按钮
        【checkpoint】检查灯泡开关状态是否改变
        4. 点击灯泡进入设备主页
        【checkpoint】灯泡主页的状态显示是否正确
        :return:
        """
        home_page.into_device_home_page(data.get_device('white_bulbs'))

        TestBulbs.bulbs_ready()
        # bulbs_home_page.skip_bulbs_guide()
        # if bulbs_home_page.is_offline:
        #     bulbs_home_page.ok
        #     if bulbs_home_page.bulbs_is_offline() is False:
        #         assert False, 'bulb设备处于离线状态'
        # bulbs_home_page.ignore_update()

        bulbs_home_page.click_bulbs()
        time.sleep(4)
        status_1 = bulbs_home_page.bulb_status(False)
        bulbs_home_page.add_check_image('灯泡主页灯泡开启状态')
        bulbs_home_page.back_home()
        status_2 = home_page.read_device_status(data.get_device('white_bulbs'))
        bulbs_home_page.add_check_image('设备列表灯泡开启状态')

        assert status_1 and (status_2 == 'ON'), '灯泡点亮后开关状态显示错误'

        home_page.click_device_btn(data.get_device('white_bulbs'))
        time.sleep(4)
        status_3 = home_page.read_device_status(data.get_device('white_bulbs'))
        bulbs_home_page.add_check_image('设备列表灯泡关闭状态')
        home_page.into_device_home_page(data.get_device('white_bulbs'))
        status_4 = bulbs_home_page.bulb_status(False)
        bulbs_home_page.add_check_image('设备列表灯泡关闭状态')

        assert ('OFF' == status_3) and status_4 is False, '灯泡熄灭后开关状态显示错误'

    @pytest.mark.bulbs
    @pytest.mark.run(order=702)
    @pytest.mark.parametrize('check_account', ['bulbs'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def test_white_bulbs_change_lightness(self, check_account, bulbs_off):
        """
        调节灯泡亮度及默认亮度设置：
        1. app首页点击灯泡进入设备主页，点击effect设置灯泡效果white
        2.点击设置灯光亮度为上次灯光亮度
        3.向下滑动灯泡调节亮度到最低
        【checkpoint】检查亮度值 是否为1%
        4. 向上滑动调节灯泡亮度到最高，3s后再次按压灯泡，读取新的亮度值
        【checkpoint】检查亮度值是否为100%
        :return:
        """
        home_page.into_device_home_page(data.get_device('white_bulbs'))

        TestBulbs.bulbs_ready()

        if bulbs_home_page.bulb_status(False) is False:
            bulbs_home_page.click_bulbs()
            time.sleep(5)

        bulbs_home_page.change_lightness('down')
        time.sleep(5)
        assert bulbs_home_page.check_lightness_img('bulbs_min'), '灯泡调至最小亮度失败'

        bulbs_home_page.change_lightness('up')
        time.sleep(5)
        assert bulbs_home_page.check_lightness_img('bulbs_max'), '灯泡调至最大亮度失败'

    @pytest.mark.bulbs
    @pytest.mark.run(order=703)
    @pytest.mark.parametrize('check_account', ['bulbs'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def test_white_bulbs_schedule_add_and_delete(self, check_account):
        """
        新增和删除定时任务：
        1. app首页点击灯泡进入设备主页，点击schedule
        2. 点击 add 新增一个定时任务，星期几选择当前日期，点击save保存
        【checkpoint】返回定时任务列表，定时任务数量增加1
        【checkpoint】显示新增定时任务，日期为今天
        3.长按左滑在列表删除定时任务，点击ok
        # 【checkpoint】提示删除成功确认弹窗 封装在方法内部无法校验
        【checkpoint】定时任务列表任务清空
        :param check_account:
        :return:
        """
        home_page.into_device_home_page(data.get_device('white_bulbs'))

        TestBulbs.bulbs_ready()

        bulbs_home_page.into_schedules(False)
        time.sleep(2.5)
        if bulbs_schedule_page.count_schedule() > 0:
            bulbs_schedule_page.delete_schedule()
        bulbs_schedule_page.add_new_schedule()
        time.sleep(2.5)

        assert bulbs_schedule_page.count_schedule() == 1, 'bulbs添加定时任务失败'
        week = data.get_week_by_id(str(bulbs_schedule_page.week_id))
        assert bulbs_schedule_page.text_display(week), '定时任务日期显示错误'

        bulbs_schedule_page.delete_schedule()
        time.sleep(2.5)
        assert bulbs_schedule_page.count_schedule() == 0, '删除定时任务失败'

    @pytest.mark.bulbs
    @pytest.mark.run(order=704)
    @pytest.mark.parametrize('check_account', ['bulbs'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=40)
    def test_white_bulbs_delete_favorite(self, check_account):
        """
        删除灯效列表：
        1. app首页进入收藏列表，统计列表总数，小于1则新增一条
            2.灯泡主页点击灯泡进入设备主页，点击effect
            3. 点击white模式，点击收藏，输入收藏名字f_white，点击保存
        4.左滑删除列表，推出后再进来检查是否生效
        :return:
        """
        home_page.into_device_home_page(data.get_device('white_bulbs'))

        TestBulbs.bulbs_ready()

        bulbs_home_page.into_favorites(False)
        if bulbs_favorite_page.count_favorite_title() < 1:
            bulbs_favorite_page.back_bulbs()
            if bulbs_home_page.bulb_status(False) is False:
                bulbs_home_page.click_bulbs()
                time.sleep(5)

            bulbs_effect_page.add_favorite_effect('delete')
            if bulbs_home_page.bulb_status(False):
                bulbs_home_page.click_bulbs()
            bulbs_home_page.into_favorites(False)
        bulbs_favorite_page.delete_favorite()

        bulbs_favorite_page.back_bulbs()
        bulbs_home_page.into_favorites(False)
        assert bulbs_favorite_page.count_favorite_title() == 0, 'bulbs 灯效收藏列表删除失败'

    @pytest.fixture(scope='function')
    def delete_effect_favorite(self):
        """
        添加灯效收藏的后置操作：
        1.删除收藏
        2.关闭灯泡
        :return:
        """
        yield 1
        if GlobalVar.get_test_flag():
            if bulbs_home_page.is_bulbs_home_page():
                bulbs_home_page.into_favorites(False)
            bulbs_favorite_page.delete_favorite()
            bulbs_favorite_page.back_bulbs()
            if bulbs_home_page.bulb_status(False):
                bulbs_home_page.click_bulbs()

    @pytest.mark.bulbs
    @pytest.mark.run(order=705)
    @pytest.mark.parametrize('check_account', ['bulbs'], indirect=True)
    @pytest.mark.flaky(reruns=2, reruns_delay=40)
    def test_white_bulbs_add_effect_favorite(self, check_account, delete_effect_favorite):
        """
        添加white模式的favorite:
        1. app首页点击灯泡进入设备主页
        2. 点击white模式，点击收藏，输入收藏名字f_white，点击保存
        【checkpoint]】toast=Successfully Add
        3.退出effect，点击favorite进入收藏列表，遍历列表
        【checkpoint】列表显示f_white
        4.点击f_white，返回灯泡主页
        【checkpoint】灯效显示white
        :param check_account:
        :param effect:灯效
        :return:
        """
        home_page.into_device_home_page(data.get_device('white_bulbs'))

        TestBulbs.bulbs_ready()

        if bulbs_home_page.bulb_status(False) is False:
            bulbs_home_page.click_bulbs()
        time.sleep(4)

        bulbs_effect_page.add_favorite_effect('favorite')
        bulbs_effect_page.add_check_image('添加灯效收藏')
        GlobalVar.set_test_flag('t')

        bulbs_home_page.click_bulbs()
        bulbs_home_page.into_favorites(False)
        assert bulbs_favorite_page.find_favorite('favorite'), '未找到新添加的effect收藏'

    @pytest.mark.bulbs
    @pytest.mark.run(order=706)
    @pytest.mark.parametrize('check_account', ['bulbs'], indirect=True)
    @pytest.mark.flaky(reruns=2, reruns_delay=40)
    def test_white_bulbs_set_custom_light_status(self, check_account, bulbs_off):
        """
        修改灯光默认设置为自定义灯效：
        1. app首页点击灯泡进入设备主页设置灯效flow，点击more,点击defult light state进入编辑界面
        2.默认灯效改为自定义设置，选择color，点击done
        【checkpoint】当前选择custom light status
        3. 返回灯泡主页，点亮灯泡
        【checkpoint】灯效显示为color
        :return:
        """
        home_page.into_device_home_page(data.get_device('white_bulbs'))

        TestBulbs.bulbs_ready()

        bulbs_home_page.into_setting()
        bulbs_setting_page.into_default_light()
        bulbs_default_light_page.min_custom_lightness()
        bulbs_default_light_page.add_check_image('自定义灯效设置')

        bulbs_default_light_page.back_setting()
        bulbs_setting_page.back_bulbs_home()

        if bulbs_home_page.bulb_status(False) is False:
            bulbs_home_page.click_bulbs()
        time.sleep(4)
        assert bulbs_home_page.check_lightness_img('bulbs_min'), '灯泡自定义亮度设置失败'

    @pytest.mark.bulbs
    @pytest.mark.run(order=707)
    @pytest.mark.parametrize('check_account', ['bulbs'], indirect=True)
    @pytest.mark.flaky(reruns=2, reruns_delay=40)
    def test_white_bulbs_set_last_light_status(self, check_account, bulbs_off):
        """
        修改灯光默认设置为最后一次灯效：
        1. app首页点击灯泡进入设备主页，点击more,点击defult light state进入编辑界面
        2.修改默认设置为上一次灯效
        【checkpoint】当前选择 Last On Status
        3.修改灯泡模式为flow, 返回灯泡主页再次点亮灯泡读取灯效
        【checkpoint】灯效显示为flow
        :param check_account:
        :return:
        """
        home_page.into_device_home_page(data.get_device('white_bulbs'))

        TestBulbs.bulbs_ready()

        # 灯泡调到最亮
        if bulbs_home_page.bulb_status(False) is False:
            bulbs_home_page.click_bulbs()
            time.sleep(4)
        bulbs_home_page.change_lightness('up')
        bulbs_home_page.click_bulbs()

        bulbs_home_page.into_setting()
        bulbs_setting_page.into_default_light()
        bulbs_default_light_page.click_last_status()
        bulbs_default_light_page.loading()
        bulbs_default_light_page.add_check_image('记录最后一次灯效设置')

        bulbs_default_light_page.back_setting()
        bulbs_setting_page.back_bulbs_home()

        bulbs_home_page.click_bulbs()
        assert bulbs_home_page.check_lightness_img('bulbs_max'), '灯泡使用最后一次亮度设置失败'

    @pytest.fixture(scope='function')
    def delete_refuse_share_account(self):
        """
        先删除refuseshare账号分享列表
        :return:
        """
        home_page.into_system()
        system_page.into_sharing()
        all_share_page.into_device(data.get_device('white_bulbs'))
        share_setting_page.delete_share()
        all_share_page.kill
        time.sleep(2)
        all_share_page.open

    @pytest.mark.bulbs
    @pytest.mark.run(order=708)
    @pytest.mark.parametrize('check_account', ['bulbs'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def test_white_bulbs_share_email(self, check_account, delete_refuse_share_account):
        """
        灯泡球分享给未注册的账号：
        1. 点击灯泡球进入扫地机主页，点击 more进入设置界面，点击share setting进入分享列表
        2. 点击 add 按钮进入添加界面，输入分享账号：Yi@aa.com并提交
        【checkpoint】 分享邀请发送成功，弹窗提示：Successed to share
        【checkpoint】页面返回到分享列表并显示分享人，状态为：待确认
        :param check_account:
        :return:
        """

        home_page.into_device_home_page(data.get_device('white_bulbs'))

        TestBulbs.bulbs_ready()

        bulbs_home_page.into_setting()
        bulbs_setting_page.into_share()
        share_setting_page.add_share()
        share_setting_page.commit_share(data.get_account('share'))

        assert share_setting_page.share_result(), 'bulbs正确账号分享失败'
        share_setting_page.ok
        share_setting_page.loading()
        status = share_setting_page.read_share_status(data.get_username('share'))
        assert status == 'Awaiting Confirmation' or status == 'Pending Confirmation', '分享列表被分享者状态显示错误'

    @pytest.mark.bulbs
    @pytest.mark.run(order=709)
    @pytest.mark.parametrize('check_account', ['bulbs'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def test_white_bulbs_agree_share(self, check_account, delete_share_news):
        """
        灯泡球被分享者接受分享:
        1. 登陆账号Yi@aa.com/12345678
        【checkpoint】登陆账号为Yi@aa.com
        2. 点击进入侧边栏界面
        【checkpoint】消息通知显示分享通知红点标识
        3. 点击news进入消息界面
        【checkpoint】显示分享邀请消息记录
        4. 点击最新一条分享邀请通知，点击ok按钮
        【checkpoint】进入消息通知显示拒绝/确认两个按钮
        【checkpoint】点击ok按钮弹窗提示分享成功
        :param check_account:
        :return:
        """
        home_page.into_device_home_page(data.get_device('white_bulbs'))

        TestBulbs.bulbs_ready()

        bulbs_home_page.into_setting()
        bulbs_setting_page.into_share()

        status = share_setting_page.read_share_status(data.get_username('share'))
        if status not in ['Awaiting Confirmation', 'Pending Confirmation']:
            share_setting_page.add_share()
            share_setting_page.commit_share(data.get_account('share'))
            assert share_setting_page.share_result(), 'bulbs正确账号分享失败,无法执行用例:[test_bulbs_agree_share]'
            share_setting_page.ok
            share_setting_page.loading()

        share_setting_page.back_setting()
        bulbs_setting_page.back_bulbs_home()
        bulbs_home_page.back_home()
        TestBulbs.change_account('share')
        home_page.into_system()

        system_page.into_sharing()
        assert all_share_page.text_display(data.get_device('white_bulbs')), '被分享列表未显示分享设备信息'
        GlobalVar.set_test_flag('t')  # 到这里后需要执行 tear_down
        all_share_page.into_device(data.get_device('white_bulbs'))
        all_share_page.yes
        all_share_page.loading()

        assert news_page.text_display('Request Accepted. You may now use this device.'), '被分享者确认接受分享失败'
        news_page.ok
        assert news_page.text_display('bulbs shared a ' + data.get_device('white_bulbs').strip()), '被分享者显示的分享设备名称错误'

        news_page.back_system()
        news_page.back_system()
        system_page.back_home()
        home_page.swipe_page('down')
        assert home_page.find_device(data.get_device('white_bulbs')), '被分享者未显示分享的灯泡设备'

    @pytest.mark.bulbs
    @pytest.mark.run(order=710)
    @pytest.mark.parametrize('check_account', ['share'], indirect=True)
    def test_white_bulbs_delete_share(self, check_account):
        """
        灯泡球被分享者移除分享设备:
        1. app首页点击进入设备主页，点击更多，点击删除设备
        【checkpoint】弹窗提示确认移除
        2.点击 ok 按钮
        【checkpoint】分享者列表不显示被分享人信息
        3.切换账号Yi@aaa.com，查看设备分享列表
        【checkpoint】分享者列表不显示被分享人信息
        :return:
        """
        home_page.swipe_page('down')
        assert home_page.find_device(data.get_device('white_bulbs')), '为查找到分享设备，无法执行用:[test_bulbs_delete_share]'

        home_page.into_device_home_page(data.get_device('white_bulbs'))

        TestBulbs.bulbs_ready()

        bulbs_home_page.into_setting()
        bulbs_home_page.swipe_page('up')
        bulbs_setting_page.click_remove()
        assert bulbs_setting_page.text_display('Are you sure you want to remove this device?'), '未显示移除确认弹窗'
        bulbs_setting_page.commit_remove()
        home_page.swipe_page('down')
        assert home_page.find_device(data.get_device('white_bulbs')) is False, '被分享着移除后设备未删除'

        TestBulbs.change_account('bulbs')

        home_page.into_device_home_page(data.get_device('white_bulbs'))
        if bulbs_home_page.is_offline:
            bulbs_home_page.ok
            if bulbs_home_page.bulbs_is_offline() is False:
                assert False, 'bulbs设备处于离线状态'

        bulbs_home_page.into_setting()
        bulbs_setting_page.into_share()
        assert data.get_username('share') not in share_setting_page.read_share_to_me_list(), '分享列表显示已移除的分享者信息'

    @pytest.mark.bulbs
    @pytest.mark.run(order=711)
    @pytest.mark.parametrize('check_account', ['bulbs'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def test_white_bulbs_refuse_share(self, delete_share_news, check_account, delete_refuse_share_account):
        """
        随机扫地机被分享者拒绝接受分享：
        1. 点击随机扫地机进入扫地机主页，点击 more进入设置界面，点击share setting进入分享列表
        2. 点击 add 按钮进入添加界面，输入分享账号：Yi@aa.com并提交
        【checkpoint】 分享邀请发送成功，弹窗提示：Successed to share
        3.重启app切换账号Yi@aa.com，进入分享消息记录
        4.点击拒绝接受分享按钮
        【checkpoint】显示已拒绝分享弹窗
        【chenckpoint】app首页不显示分享设备
        :param check_account:
        :return:
        """
        home_page.into_device_home_page(data.get_device('white_bulbs'))

        TestBulbs.bulbs_ready()

        bulbs_home_page.into_setting()
        bulbs_setting_page.into_share()
        share_setting_page.add_share()
        share_setting_page.commit_share(data.get_account('refuseshare'))
        assert share_setting_page.share_result(), 'inertia_robotic正确账号分享失败'
        share_setting_page.ok
        share_setting_page.loading()

        share_setting_page.back_setting()
        bulbs_setting_page.back_bulbs_home()
        bulbs_home_page.back_home()

        TestBulbs.change_account('refuseshare')
        GlobalVar.set_test_flag('t')

        home_page.into_system()
        system_page.into_sharing()
        all_share_page.into_device(data.get_device('white_bulbs'))
        all_share_page.no
        assert all_share_page.text_display('Request Declined. This device will be removed.'), 'bulbs被分享者拒绝接受分享失败'
        all_share_page.ok
        all_share_page.loading()

        all_share_page.back_system()
        system_page.back_home()
        home_page.swipe_page('down')
        assert home_page.find_device(data.get_device('white_bulbs')) is False, 'app首页被分享者拒绝分享后显示分享了扫地机设备'

    @pytest.mark.bulbs
    @pytest.mark.run(order=712)
    @pytest.mark.parametrize('check_account', ['bulbs'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def white_bulbs_add_group(self, check_account):
        """
        将两个设备添加到一个分组:
        1. app首页点击进入设备主页，点击更多
        2. 点击 group，点击add group，选择 卧室，点击next
        3. 设置分组名称 group1，点击save
        【checkpoint】分组名称显示为 group1
        4. 点击 V 选择两个灯泡球，点击保存
        【checkpoint】分组列表显示新增分组
        5.回到app首页
        【checkpoint】页面显示新增分组
        :return:
        """
        home_page.into_device_home_page(data.get_device('color_bulbs'))

        TestBulbs.bulbs_ready()

        if bulbs_home_page.bulb_status(False):
            bulbs_home_page.click_bulbs()
        bulbs_home_page.into_setting()
        bulbs_setting_page.into_group()
        bulbs_group_page.click_add_group()
        bulbs_group_page.select_room_type()

        bulbs_group_page.set_group_name(data.get_bulbs_group('bulbs'))
        bulbs_group_page.selct_device(data.get_device('color_bulbs'))
        bulbs_group_page.selct_device(data.get_device('bulbs2'))
        bulbs_group_page.save_group()

        assert bulbs_group_page.find_group_list(data.get_bulbs_group('bulbs')), '添加分组后列表未找到分组'

        bulbs_group_page.back_setting()
        bulbs_setting_page.back_bulbs_home()
        bulbs_home_page.back_home()

        home_page.swipe_page('down')
        assert home_page.find_group(data.get_bulbs_group('bulbs')), 'app首页未显示灯泡分组'

    @pytest.fixture(scope='function')
    def bulbs_group_off(self):
        """
        分组关闭
        :return:
        """
        yield 1
        if home_page.is_welcome():
            home_page.into_group_page(data.get_bulbs_group('bulbs'))
        if bulbs_group_home_page.group_is_on():
            bulbs_group_home_page.click_group_bulbs()
            time.sleep(3)

    @pytest.mark.bulbs
    @pytest.mark.run(order=713)
    @pytest.mark.parametrize('check_account', ['bulbs'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def white_bulbs_group_on_off(self, check_account, bulbs_group_off):
        """
        开启、关闭灯泡分组：
        1. app首页点击进入分组主页
        2.点击打开分组打开分组
        【checkpoint】检查灯组是否已开启，记录灯组状态
        3.返回首页列表
        【checkpoint】检查灯组的状态
        4.点击灯组开关关闭分组
        【checkpoint】检查灯组的状态
        5.点击进入灯组主页
        【checkpoint】检查灯组的状态显示是否正确
        :param check_account:
        :return:
        """
        home_page.swipe_page('down')
        home_page.into_group_page(data.get_bulbs_group('bulbs'))
        time.sleep(5)
        bulbs_group_home_page.click_group_bulbs()
        time.sleep(5)
        assert bulbs_group_home_page.group_is_on(), '分组主页开启灯组失败'
        status0 = bulbs_group_home_page.read_group_status()

        bulbs_group_home_page.back_home()
        assert home_page.read_group_status().replace(' ', '').replace('/', '') in status0.replace(' ', ''), '列表的灯组状态开启后显示错误'

        home_page.click_group_btn()
        time.sleep(5)
        status1 = home_page.read_group_status()
        assert 'OFF' in status1.strip(), '列表的灯组关闭后状态显示错误'
        home_page.into_group_page(data.get_bulbs_group('bulbs'))
        assert status1.replace(' ', '').replace('/', '') in bulbs_group_home_page.read_group_status().replace(' ', ''), '列表的灯组关闭后分组主页状态显示错误'

    @pytest.fixture(scope='function')
    def bulbs_white_group_effect_off(self):
        """
        灯组模式切换后关闭灯组
        :return:
        """
        yield 1
        bulbs_group_home_page.close_effect()
        bulbs_group_home_page.click_group_bulbs()
        time.sleep(3)

    @pytest.fixture(scope='function')
    def set_default_group_name(self):
        """
        将组名恢复为默认名称
        :return:
        """
        yield 1
        if GlobalVar.get_test_flag():
            if home_page.is_welcome():
                home_page.into_group_page(data.get_bulbs_group('bulbs'))
            try:
                bulbs_group_home_page.into_group_setting()
            except Exception as e:
                print(e)
                pass
            bulbs_group_home_page.change_group_name(data.get_bulbs_group('bulbs'))

    @pytest.mark.bulbs
    @pytest.mark.run(order=714)
    @pytest.mark.parametrize('check_account', ['bulbs'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def white_bulbs_change_group_name(self, check_account):
        """
        修改分组名称：
        1. app首页点击进入分组主页，点击设置
        2. 点击分组group_***修改名称为group_随机数，点击save
        【checkpoint】分组名称显示group_随机数
        :param check_account:
        :return:
        """
        home_page.into_group_page(data.get_bulbs_group('bulbs'))
        bulbs_group_home_page.into_group_setting()

        new_name = data.get_bulbs_group('bulbs')+bulbs_group_home_page.get_str()
        print(new_name)
        bulbs_group_home_page.change_group_name(new_name)
        assert bulbs_group_home_page.text_display(new_name), '分组名称修改后设置界面显示错误'
        GlobalVar.set_test_flag('t')

        bulbs_group_home_page.back_group()
        assert new_name in bulbs_group_home_page.read_home_group_name(), '分组名称修改后分组首页显示名称错误'

        bulbs_group_home_page.back_home()
        home_page.swipe_page('down')
        assert home_page.find_group(new_name), '分组名称修改后app首页显示名称错误'

    @pytest.mark.bulbs
    @pytest.mark.run(order=715)
    @pytest.mark.parametrize('check_account', ['bulbs'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def white_bulbs_delete_group(self, check_account):
        """
        删除新增的分组：
        1. app首页点击进入分组主页，点击设置
        2.点击进入设置界面，点击删除
        【checkpoint】分组列表不显示分组
        :param check_account:
        :return:
        """
        home_page.into_group_page(data.get_bulbs_group('bulbs'))
        bulbs_group_home_page.into_group_setting()

        bulbs_group_home_page.delete_this_group()
        bulbs_group_home_page.yes

        home_page.swipe_page('down')
        assert home_page.find_group(data.get_bulbs_group('bulbs')) is False, '删除bulbs分组失败'

    @pytest.mark.bulbs
    @pytest.mark.run(order=716)
    @pytest.mark.parametrize('check_account', ['bulbs'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def test_white_bulbs_check_schedule_icon(self, check_account):
        """
        检查定时任务图标是否显示：
        1.进入app主页，检查是否显示定时任务图标
        2.如果未显示则去开启一个定时任务，并返回app首页
        【checkpoint】检查设备是否显示定时任务图标
        :return:
        """
        home_page.swipe_page('down')
        status = home_page.have_schedule_icon(data.get_device('white_bulbs'))

        if not status:
            home_page.into_device_home_page(data.get_device('white_bulbs'))
            bulbs_home_page.skip_bulbs_guide()
            if bulbs_home_page.is_offline:
                bulbs_home_page.ok
            bulbs_home_page.ignore_update()

            bulbs_home_page.into_schedules(False)
            if not bulbs_schedule_page.read_away_mode_status():
                bulbs_schedule_page.click_away_mode()
            bulbs_schedule_page.back_bulbs()
            bulbs_home_page.back_home()
            home_page.swipe_page('down')
            status = home_page.have_schedule_icon(data.get_device('white_bulbs'))

        assert status, 'bulbs 未显示定时任务图标'

        home_page.click_schedule_icon(data.get_device('white_bulbs'))
        assert home_page.text_display('Schedules'), 'bulbs 定时任务快捷图标进入失败'

    @pytest.fixture(scope='function')
    def close_bulbs_schedule(self):
        """
        关闭扫地机及定时任务
        :return:
        """
        yield 1
        if GlobalVar.get_test_flag():
            if bulbs_home_page.bulb_status(False):
                bulbs_home_page.click_bulbs()
            bulbs_home_page.into_schedules(False)
        bulbs_schedule_page.delete_schedule()

    @pytest.mark.bulbs
    @pytest.mark.run(order=717)
    @pytest.mark.parametrize('check_account', ['bulbs'], indirect=True)
    def test_white_bulbs_schedule_time(self, check_account, close_bulbs_schedule):
        """
        球泡灯设置定时任务：
        1.设置一个基于当前时间5min后的定时任务
        【checklist】检查定时任务列表的时间是否设置正确
        2.等待定时任务启动
        【checklist】检查定时任务启动后灯泡的状态
        :param check_account:
        :return:
        """
        home_page.into_device_home_page(data.get_device('white_bulbs'))
        TestBulbs.bulbs_ready()

        if bulbs_home_page.bulb_status(False):
            bulbs_home_page.click_bulbs()
        bulbs_home_page.into_schedules(False)
        _t = bulbs_schedule_page.add_new_schedule(data.get_device('white_bulbs'), 5)

        assert _t == bulbs_schedule_page.read_schedule_time(bulbs_schedule_page.week_simple_name), '定时任务设置正确'
        bulbs_schedule_page.back_bulbs()

        GlobalVar.set_test_flag('t')  # 此处需要判断设备状态了

        bulbs_home_page.long_wait(320)
        assert bulbs_home_page.bulb_status(False), '定时任务执行启动成功'

    @pytest.mark.bulbs
    @pytest.mark.run(order=718)
    @pytest.mark.parametrize('check_account', ['bulbs'], indirect=True)
    @pytest.mark.flaky(reruns=1, reruns_delay=60)
    def bulbs_remove(self, check_account):
        """
        移除灯泡球产品:
        1. app首页点击进入设备主页，点击more进入设置界面
        2. 点击remove
        【checkpoint】弹出移除成功确认弹窗
        【checkpoint】返回app首页，设备列表不显示light
        :param check_account:
        :return:
        """
        if GlobalVar.get_remove_add() == 0:
            pytest.skip('本次指定不执行词条用例')

        home_page.into_device_home_page(data.get_device('white_bulbs'))

        TestBulbs.bulbs_ready()

        bulbs_home_page.into_setting()
        bulbs_setting_page.swipe_page('up')
        bulbs_setting_page.click_remove()

        assert bulbs_setting_page.text_display('Are you sure you want to remove this device?'), '未显示移除确认弹窗'
        bulbs_setting_page.commit_remove()
        bulbs_setting_page.loading()
        assert home_page.is_welcome(), '移除设备后未返回app首页'
        home_page.swipe_page('down')
        assert home_page.find_device(data.get_device('white_bulbs')) is False, 'bulbs 删除后首页仍然显示'

    @pytest.fixture(scope='function')
    def reset_phone_network(self):
        """
        检查并重置手机网络，防止配网失败影响网络
        :return:
        """
        yield 1
        add_device_page.set_system_wifi(data.get_wifi('phone')[0])

    @pytest.mark.bulbs
    @pytest.mark.run(order=430)
    @pytest.mark.parametrize('check_account', ['bulbs'], indirect=True)
    def bulbs_add_device(self, check_account, bulbs_off, reset_phone_network):
        """
        添加灯泡:
        1. app首页点击+，选择bulbs
        2. 点击Next，勾选 Status Confirmed，点击 next, 勾选 Status Confirmed，点击 next
        3. 选择亚添加的设备id
        4. 连接中，等待conecting消失
        【checkpoint】判断是否显示添加成功（文本校验）
        5. 修改设备昵称未T1013，点击保存
        6. 返回设备主页查看设备列表
        【checkpoint】首页列表刷新后显示灯泡1013
        :param check_account:
        :return:
        """
        if GlobalVar.get_remove_add() == 0:
            GlobalVar.set_test_flag('f')
            pytest.skip('本次指定不执行词条用例')

        home_page.swipe_page('down')
        if home_page.find_device(data.get_device('white_bulbs')):
            home_page.into_device_home_page(data.get_device('white_bulbs'))

            TestBulbs.bulbs_ready()

            bulbs_home_page.into_setting()
            bulbs_setting_page.swipe_page('up')
            bulbs_setting_page.click_remove()
            bulbs_setting_page.commit_remove()
            bulbs_setting_page.loading()

        home_page.click_add_device()
        add_device_page.click_bulds()
        wifi = data.get_wifi('white_bulbs')
        add_device_page.set_wifi(wifi[0], wifi[1])
        add_device_page.confirm_bulbs_status()
        add_device_page.bulbs_next()
        add_device_page.confirm_bulbs_status()
        add_device_page.bulbs_next()
        add_device_page.select_robotic_by_id(data.get_device_udid('white_bulbs'))
        add_device_page.loading()

        add_device_page.wait_connect()
        assert add_device_page.connect_result(), 'bulbs 配网连接失败'
        add_device_page.set_device_name(data.get_device('white_bulbs'))
        add_device_page.ok
        add_device_page.loading()

        home_page.swipe_page('down')
        assert home_page.find_device(data.get_device('white_bulbs')), 'bulbs 配网成功后首页未查找到设备'


