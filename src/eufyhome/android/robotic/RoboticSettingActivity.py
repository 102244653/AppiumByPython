class RoboticSettingActivity(object):

    # 设置界面返回
    back_device = ('id', 'com.eufylife.smarthome:id/common_header_start_icon')

    # 设备名称
    device_name = ('id', 'com.eufylife.smarthome:id/device_name_edt')

    # 修改设备名
    device_name_input = ('id', 'com.eufylife.smarthome:id/device_name_edt')

    # 修改设备名保存
    save = ('id', 'com.eufylife.smarthome:id/submit_btn')

    # 分享设置
    setting_share = ('xpath', '//*[@text="Sharing Settings"]')

    # 固件更新
    setting_update = ('xpath', '//*[@text="Firmware Update"]')

    # 固件更新标示
    is_update = ()

    # 帮助
    setting_help = ('id', 'com.eufylife.smarthome:id/help')

    # 移除设备
    setting_remove = ('id', 'com.eufylife.smarthome:id/remove_device')

    # 确认移除按钮
    commit_remove = ('xpath', '//*[@text="Delete"]')

    # *********************T2250********************* #
    # 声音设置
    setting_voice = ('android', 'text("Voice Settings")')

    # 寻找扫地机
    setting_find = ('android', 'text("Find My Robot")')

    # 手动控制
    setting_manual = ('android', 'text("Manual Controls")')

    # 断点续扫
    auto_return = ('android', 'text("Auto-return cleaning")')

    # 配材设置
    setting_maintenance = ()

    # *********************T2190/T2250********************* #
    # 面积单位
    setting_unit = ('id', 'com.eufylife.smarthome:id/robovac_units_setting')
