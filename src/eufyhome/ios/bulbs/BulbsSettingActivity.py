class BulbsSettingActivity(object):
    # 返回
    back_bulb = ('name', 'common icon back')

    # 设备名
    bulb_name = ('xpath', '//XCUIElementTypeStaticText[@name="Settings"]/../XCUIElementTypeButton')
    # 设备名编辑狂
    bulbs_name_edit = ('xpath', '//XCUIElementTypeButton[@name="Save"]/../XCUIElementTypeTextField')

    # 保存修改名称
    save_name = ('name', 'Save')

    # 分享
    share = ('name', 'Sharing Settings')

    # 分组
    group = ('name', 'Group')

    # 默认设置
    default_light = ('name', 'Default Light State')

    # 固件升级
    update = ('name', 'Firmware Update')

    update_tip = ()

    # 帮助
    help = ('name', 'Help')

    # 移除
    remove = ('name', 'Remove Device')

    # 确认移除
    commit_remove = ('name', 'Yes')



