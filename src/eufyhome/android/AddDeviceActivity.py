class RoboticActivity(object):
    # *********************扫地机界面************************ #
    # 扫地机型号
    robotic_type = ('id', 'com.eufylife.smarthome:id/modelName')

    # *********************扫地机添加流程************************ #
    # wifi名输入框
    robovac_wifi_name = ('id', 'com.eufylife.smarthome:id/wifi_ssid_edit_text')

    # 显示Wi-Fi密码
    robovac_display_pw = ('id', 'com.eufylife.smarthome:id/pwd_checkbox')

    # Wi-Fi密码输入框
    robovac_wifi_password = ('id', 'com.eufylife.smarthome:id/wifi_pwd_edit_text')

    # 记住wifi密码
    robovac_save_network = ('id', 'com.eufylife.smarthome:id/savePasswordChkbox')

    # 下一步按钮
    robotic_wifi_next = ('id', 'com.eufylife.smarthome:id/configBt')

    # 状态确认
    robotic_status_confirm = ('id', 'com.eufylife.smarthome:id/cb_status')

    # 状态确认next
    robotic_status_next = ('id', 'com.eufylife.smarthome:id/next_button')

    # 设备名称
    device_udid = ('id', 'com.eufylife.smarthome:id/device_name')

    # 无设备刷新按钮
    robotic_refresh = ('id', 'com.eufylife.smarthome:id/bt_refresh')

    # 手动添加网络
    # manual_connect = ('id', 'com.eufylife.smarthome:id/device_sharing_tv')


class SwitchActivity(RoboticActivity):
    # 跳过
    switch_guide = ('xpath', '//*[@text="Skip"]')

    # 连接wifi
    connect_wifi = ('xpath', '//*[@text="Connect to Wi-Fi"]')

    # 列表刷新
    switch_refresh = ('id', 'com.eufylife.smarthome:id/common_header_end_icon')

    # 手动添加网络
    manual_connect = ('id', 'com.eufylife.smarthome:id/manualTv')

    # wifi名
    switch_wifi_name = ('id', 'com.eufylife.smarthome:id/hiddenSsid')

    # wifi密码
    switch_wifi_pw = ('id', 'com.eufylife.smarthome:id/passwordTv')

    # wifi密码显示
    switch_wifi_pw_display = ('id', 'com.eufylife.smarthome:id/ifShowPasswd')


class AddDeviceActivity(SwitchActivity):

    # 页面关闭按钮
    close = ('id', 'com.eufylife.smarthome:id/common_header_end_icon')

    # 设备类型
    device_type = ('id', 'com.eufylife.smarthome:id/productName')

    # 扫地机
    robotic = ('xpath', '//android.widget.TextView[@text="Robotic Vacuums"]/..')

    # 灯泡
    bulds = ('xpath', '//android.widget.TextView[@text="Smart Bulbs"]/..')

    # 插座
    plug = ('xpath', '//android.widget.TextView[@text="Smart Plugs"]/..')

    # 开关
    switch = ('xpath', '//android.widget.TextView[@text="Smart Switches"]/..')

    # 音箱
    genie = ('xpath', '//android.widget.TextView[@text="Eufy Genie"]/..')

    # *********************添加结果确认及设置名称************************ #

    # 添加成功页面标题
    connect_successed = ('xpath', '//*[@text="Successfully Added Your Device"]')
    connect_failed = ('xpath', '//*[@text="Failed to Connect"]')

    # 修改设备名称
    set_device_name = ('id', 'com.eufylife.smarthome:id/name_et')

    # 提交按钮
    commit_name = ('id', 'com.eufylife.smarthome:id/submit_btn')

    # next
    Next_btn = ('xpath', '//*[@text="Next"]')