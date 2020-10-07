class RoboticSettingActivity(object):
    # 设置界面返回
    back_device = ('name', 'common icon back')

    # 设备名称
    device_name = ('xpath', '//XCUIElementTypeStaticText[@name="Settings"]/../XCUIElementTypeButton')

    # 修改设备名
    device_name_input = ('xpath', '//XCUIElementTypeButton[@name="Save"]/../XCUIElementTypeTextField')

    # 修改设备名保存
    save = ('name', 'Save')

    # 分享设置
    setting_share = ('name', 'Sharing Settings')

    # 固件更新
    setting_update = ('name', 'Firmware Update')

    # 固件更新标示
    is_update = ()

    # 帮助
    setting_help = ('name', 'Help')

    # 移除设备
    setting_remove = ('name', 'Remove Device')

    # 确认移除按钮
    commit_remove = ('name', 'Yes')

    # *********************T2250********************* #
    # 声音设置
    setting_voice = ('name', 'Voice Settings')

    # 寻找扫地机
    setting_find = ('name', 'Find My Robot')

    # 手动控制
    setting_manual = ('name', 'Manual Controls')

    # distrub
    setting_distrub = ('name', 'Do Not Disturb')

    # 断点续扫
    auto_return = ('name', 'Auto-return cleaning')

    # 断点续扫页面返回
    t2250_back_setting = ('name', 'common icon back')

    # 断点续扫页面开关
    t2250_auto_clean_btn = ('name', 'common btn bg off')

    # 配材设置
    setting_maintenance = ('name', 'Maintenance')

    # *********************T2190********************* #
    # 面积单位
    setting_unit = ('name', 'Unit Settings')
