import os
import shutil
import signal
import subprocess
import sys
import time
import allure
from datetime import datetime
from appium import webdriver
import pytest
import base_path
from src.config.readconfig import data
from src.config.config import GlobalVar
from src.util import util
import logging
from pytest_reportportal import RPLogger, RPLogHandler

server_ip = '127.0.0.1'  # appium服务运行的ip，一般appium服务和脚本都在同一台电脑上执行，使用'127.0.0.1'不需要修改
appium_port = 4723  # appium服务监听的端口，4723是初始值，执行过程中由脚本随机分配一个空闲端口，不需要人工介入
wda_port = 8100  # webdriveragent服务监听的端口，8100是初始值，执行过程中由脚本随机分配一个空闲端口，不需要人工介入
system_port = 8200  # adb转发端口，8200是初始值，执行过程中由脚本随机分配一个空闲端口，不需要人工介入
device_sn = ""  # 手机sn号，脚本从执行命令中读取后重新赋值
appium_log_path = ""  # appium服务端日志保存的文件名，文件名中会带appium端口和时间戳，脚本中会重新赋值
appium_p = None
driver = None
pf = ""  # 设备平台类型
rp_logger = None
# -m debug --cmd_pf=ios --cmd_sn=38d611688295af7a55b6a89ff20af73a30aec319
# -m debug --cmd_pf=android --cmd_sn=HT7AS1A00075 --cmd_ra=true
"""
使用 @pytest.fixture(scope='function') 装饰器的方法可以看做是setup方法
scope指定级别，取值可以是"function"(default),"class","module","package" or "session"
"""


@pytest.fixture(scope='module')
def appium_setup(request):
    """
    启动appium服务
    :param request:
    :return:
    """
    global device_sn, pf, server_ip, appium_port, appium_log_path, device_name, platform_version, wda_port, system_port, appium_p
    device_sn = cmd_sn(request)  # 从执行命令读取测试手机sn号
    pf = cmd_platform(request).lower()
    GlobalVar.set_add_remove(cmd_remove_add(request))
    appium_port = util.create_port(server_ip, 4723, 7999)
    appium_log_path = "{}/src/appium_log/{}_{}.log".format(base_path.get_path(), datetime.now().strftime('%Y-%m-%d_%H.%M.%S'), appium_port)
    if pf == 'ios':
        GlobalVar.set_platform(GlobalVar.IOS)  # 将平台名保存成全局的变量，脚本中通过GlobalVar.get_platform()获取当前执行的平台
        # device_name = util.get_iphone_name(device_sn)
        device_name = 'iPhone eufy'
        platform_version = util.get_iphone_version(device_sn)
        wda_port = util.create_port(server_ip, 8100, 9999)
        appium_p = subprocess.Popen(
            "appium -a {} -p {} --webdriveragent-port {} --relaxed-security --session-override > {} 2>&1 &".format
            (server_ip, appium_port, wda_port, appium_log_path), shell=True)  # 命令行启动appium服务
    elif pf == 'android':
        GlobalVar.set_platform(GlobalVar.ANDROID)  # 将平台名保存成全局的变量，脚本中通过GlobalVar.get_platform()获取当前执行的平台
        util.uninstall_uiautomator2_server()  # 卸载手机上安装的uiautomator2 server两个app
        system_port = util.create_port(server_ip, 8200, 8299)
        appium_p = subprocess.Popen(
            "appium -a {} -p {} --relaxed-security --session-override > {} 2>&1 &"
                .format(server_ip, appium_port, appium_log_path), shell=True)  # 命令行启动appium服务
    else:
        raise EnvironmentError('设备平台类型传参错误：--cmd_pf='+pf)
    time.sleep(10)

    #  新测试报告
    global rp_logger
    rp_logger = logging.getLogger(__name__)
    rp_logger.setLevel(logging.DEBUG)
    # Create handler for Report Portal if the service has been
    # configured and started.
    if hasattr(request.node.config, 'py_test_service'):
        # Import Report Portal logger and handler to the test module.
        logging.setLoggerClass(RPLogger)
        rp_handler = RPLogHandler(request.node.config.py_test_service)
        # Add additional handlers if it is necessary
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        rp_logger.addHandler(console_handler)
    else:
        rp_handler = logging.StreamHandler(sys.stdout)
    # Set INFO level for Report Portal handler.
    rp_handler.setLevel(logging.INFO)
    GlobalVar.set_rp_logger(rp_logger)

    def teardown():
        try:
            os.killpg(os.getegid(appium_p.pid+1), signal.SiGTERM)
        except Exception as e:
            print(e)
            pass

    request.addfinalizer(teardown)


@pytest.fixture(scope='function')
def driver_setup(request):
    """
    创建会话
    scope=class时使用cls，scope=function时使用instance
    :param request:
    :return:
    """
    global driver, device_sn, device_name, platform_version, wda_port, system_port, appium_port
    if GlobalVar.get_platform() == GlobalVar.IOS:
        desired_capabilities = {
            'automationName': 'XCUITest',
            'platformName': 'ios',
            'udid': device_sn,
            'deviceName': device_name,
            'platformVersion': platform_version,
            'wdaLocalPort': wda_port,
            'bundleId': data.get_eufyhome('bundleId'),
            'newCommandTimeout': 600,
            'clearSystemFiles': True,
            'excludeDriverLogs': ['syslog', 'server'],
            'iosInstallPause': 8000,
            'wdaLaunchTimeout': 600000,
            'wdaConnectionTimeout': 600000,
            'wdaStartupRetries': 4,
            'wdaStartupRetryInterval': 60000,
            'orientation': 'PORTRAIT',
            'noReset': True,
            'fullReset': False,
            'autoLaunch': True
        }
    elif GlobalVar.get_platform() == GlobalVar.ANDROID:
        desired_capabilities = {
            'automationName': 'UiAutomator2',
            'uiautomator2ServerInstallTimeout': 120000,  # ms
            'uiautomator2ServerLaunchTimeout': 120000,  # ms
            'platformName': 'Android',
            'platformVersion': '9.0',
            'udid': device_sn,
            'deviceName': 'Android',
            'appPackage': 'com.eufylife.smarthome',
            'appActivity': 'com.oceanwing.eufyhome.main.WelcomeActivity',
            'newCommandTimeout': 600,
            'adbExecTimeout': 120000,  # ms
            'systemPort': system_port,
            'orientation': 'PORTRAIT',
            'noReset': True,  # 是否以初始状态启动app
            'fullReset': False,  # 是否重装app
            'autoLaunch': True  # app自动启动

            # 自动获取元素的配置
            # 'noReset': True,
            # 'fullReset': False,
            # 'autoLaunch': False
        }

    request.instance.driver = webdriver.Remote(command_executor='http://{}:{}/wd/hub'.format('127.0.0.1', appium_port),
                                             desired_capabilities=desired_capabilities)  # 创建会话
    driver = request.instance.driver
    time.sleep(10)

    def teardown():
        try:
            driver.quit()  # 测试结束后结束本次会话
        except Exception as e:
            print(e)
            pass

    request.addfinalizer(teardown)


def pytest_addoption(parser):
    '''
    增加一条命令行选项,在pytest执行命令中可以通过--cmd_sn=xxx配置参数
    :param parser:
    :return:
    '''
    parser.addoption("--cmd_sn", action="store", default="0", help="sn")
    parser.addoption("--cmd_pf", action="store", default="Android", help="pf")
    parser.addoption("--cmd_ra", action="store", default="0", help="remove_add")


def cmd_sn(request):
    '''
    脚本获取命令行参数的接口
    :param request:
    :return:
    '''
    value = request.config.getoption("--cmd_sn")
    return value


def cmd_platform(request):
    """
    读取是否生成报告参数
    :param request:
    :return:
    """
    value = request.config.getoption("--cmd_pf")
    return value


def cmd_remove_add(request):
    """
    是否执行配网,默认传：false/true
    :param request:
    :return:
    """
    value = request.config.getoption("--cmd_ra")
    return str(value)


@pytest.fixture(scope="session")
def rp_logger(request):
    import logging
    from pytest_reportportal import RPLogger, RPLogHandler
    global logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.ERROR)
    # Create handler for Report Portal if the service has been
    # configured and started.
    if hasattr(request.node.config, 'py_test_service'):
        # Import Report Portal logger and handler to the test module.
        logging.setLoggerClass(RPLogger)
        rp_handler = RPLogHandler(request.node.config.py_test_service)
        # Add additional handlers if it is necessary
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.ERROR)
        logger.addHandler(console_handler)
    else:
        rp_handler = logging.StreamHandler(sys.stdout)
    # Set INFO level for Report Portal handler.
    rp_handler.setLevel(logging.ERROR)
    return logger


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    '''
    hook pytest失败
    :param item:
    :param call:
    :return:
    '''
    outcome = yield
    rep = outcome.get_result()

    # we only look at actual failing test calls, not setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            # let's also access a fixture for the fun of it
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
            f.write(rep.nodeid + extra + "\n")
            global driver
            path = make_path()
            name = datetime.now().strftime('%m%d%H%M%S')
            path_name = u'{}/{}.png'.format(path, name)
            driver.get_screenshot_as_file(path_name)
            allure.attach.file(path_name, "【断言失败截图:{}.png】".format(name), allure.attachment_type.PNG)

            with open('{}'.format(path_name), "rb") as image_file:
                # 报错  TypeError: _log() got an unexpected keyword argument 'attachment'
                GlobalVar.get_rp_logger().info("断言失败截图",
                                                extra=dict(attachment={"name": "failure screenshot.png",
                                                                       "data": image_file,
                                                                       "mime": "image/png"}))


def make_path():
    '''
    创建保存失败截图的文件目录
    :param nodeid:
    :return:
    '''
    path = '{}/result_images'.format(base_path.get_path())
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def delete_files(path):
    file_list = os.listdir(path)
    if len(file_list) == 0:
        return
    for f in file_list:
        file_path = os.path.join(path, f)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path, True)

