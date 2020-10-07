class SwitchSettingActivity(object):
    # 返回
    back_switch = ('name', 'common icon back')

    # 设备名
    device_name = ('xpath', '//XCUIElementTypeStaticText[@name="Settings"]/../XCUIElementTypeButton')

    # 编辑设备名
    edit_device_name = ('xpath', '//XCUIElementTypeButton[@name="Save"]/../XCUIElementTypeTextField')

    # 修改设备名保存
    save_name = ('name', 'Save')

    # 分享
    into_share = ('name', 'Sharing Settings')

    # 升级
    into_update = ('name', 'Firmware Update')
    update_tip = ('xpath', '//XCUIElementTypeStaticText[@name="Firmware Update"]/following-sibling::XCUIElementTypeOther')

    # help
    into_help = ('name', 'Help')

    # 移除设备
    remove_device = ('name', 'Remove Device')

    # 确认移除
    commit_remove = ('name', 'Yes')
