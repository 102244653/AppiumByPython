class PlugSettingActivity(object):
    # 返回
    back_home = ('name', 'common icon back')

    # 设备名
    device_name = ('xpath', '//XCUIElementTypeStaticText[@name="Settings"]/../XCUIElementTypeButton')

    # 设备名编辑
    edit_device_name = ('xpath', '//XCUIElementTypeButton[@name="Save"]/../XCUIElementTypeTextField')

    # 设备名编辑保存
    save_name = ('name', 'Save')

    # 分享
    into_share = ('name', 'Sharing Settings')

    # 升级
    into_update = ('name', 'Firmware Update')

    # help
    into_help = ('name', 'Help')

    # 移除
    remove_btn = ('name', 'Remove Device')

    # 确认移除
    commit_remove = ('name', 'Yes')
