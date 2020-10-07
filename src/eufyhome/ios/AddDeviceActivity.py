class RoboticActivity(object):
    # *********************扫地机型号界面************************ #
    # 扫地机型号
    robotic_type = ('xpath', '//XCUIElementTypeCell/XCUIElementTypeStaticText[2]')

    # *********************扫地机添加流程************************ #
    # wifi名输入框
    # robovac_wifi_name = ('xpath', '//*[@name="Network Name"]/../XCUIElementTypeTextField')
    robovac_wifi_name = ('xpath', '//XCUIElementTypeButton[@name="adddevice icon arrow down"]/../XCUIElementTypeTextField')

    # 显示Wi-Fi密码
    robovac_display_pw = ('name', 'signup icon blink')

    # Wi-Fi密码输入框
    robovac_wifi_password = ('xpath', '//XCUIElementTypeButton[@name="signup icon blink"]/../XCUIElementTypeTextField')

    # 记住wifi密码
    robovac_save_network = ('xpath', '//XCUIElementTypeButton[@name="Save Password"]')

    # 下一步按钮
    robotic_wifi_next = ('name', 'Next')

    # 状态确认
    robotic_status_confirm = ('xpath', '//XCUIElementTypeButton')

    # 状态确认next
    robotic_status_next = ('name', 'Next')

    # 选择设备按钮
    robotic_into_setting = ('name', 'Go to Settings')

    # 系统设置的Wifi菜单
    system_wifi_moudle = ('name', 'Wi-Fi')

    # wifi开关
    wifi_btn = ('xpath', '//XCUIElementTypeSwitch[@name="Wi-Fi"]')

    # 返回eufyhome
    # into_eufyhome = ('xpath', '//XCUIElementTypeButton[@name="Return to EufyHome"]')
    into_eufyhome = ('name', 'Return to EufyHome')


class SwitchActivity(RoboticActivity):
    # 跳过
    switch_guide = ('name', 'Skip')

    # 连接wifi
    connect_wifi = ('name', 'Connect to Wi-Fi')

    # 手动添加网络
    manual_connect = ('name', 'Manually Connect to a Network')

    # 等待选择设备
    already_connected = ('name', 'Already Connected')

    # wifi名
    switch_wifi_name = ('xpath', '//XCUIElementTypeImage[@name="adddevice_icon_wify3"]/../XCUIElementTypeTextField')

    # wifi密码
    switch_wifi_pw = ('xpath', '//XCUIElementTypeApplication[@name="EufyHome"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[3]/XCUIElementTypeTextField')

    # wifi密码显示
    switch_wifi_pw_display = ('name', 'signup icon blink')


class AddDeviceActivity(SwitchActivity):

    # 页面关闭按钮
    close = ('name', 'common icon close black2')

    # 设备类型
    device_type = ('xpath', '//XCUIElementTypeCell/XCUIElementTypeStaticText')

    # 扫地机
    robotic = ('xpath', '//XCUIElementTypeStaticText[@name="Robotic Vacuums"]')

    # 灯泡
    bulds = ('xpath', '//XCUIElementTypeStaticText[@name="Smart Bulbs"]')

    # 插座
    plug = ('xpath', '//XCUIElementTypeStaticText[@name="Smart Plugs"]')

    # 开关
    switch = ('xpath', '//XCUIElementTypeStaticText[@name="Smart Switches"]')

    # 音箱
    genie = ('xpath', '//XCUIElementTypeStaticText[@name="Eufy Genie"]')

    # *********************添加结果确认及设置名称************************ #

    # 添加成功页面标题
    connect_successed = ('name', 'Successfully Added Your Device')
    connect_failed = ('name', 'Failed to Connect')

    # 修改设备名称
    set_device_name = ('ios', 'type="XCUIElementTypeTextField"')

    # 提交按钮
    commit_name = ('xpath', '//XCUIElementTypeButton[@name="Save Name"][1]')

    # next
    Next_btn = ('name', 'Next')
