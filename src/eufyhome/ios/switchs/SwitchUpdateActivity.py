class SwitchUpdateActivity(object):
    # 返回
    back_setting = ('name', 'common icon back')

    # 升级按钮
    update_btn = ('xpath', '//XCUIElementTypeButton[@name="Update"]')

    # 升级中
    wait_update = ('', '')

    # 版本号
    ota_version = ('xpath', '//XCUIElementTypeStaticText[starts-with(@name,"Latest Version")]')

