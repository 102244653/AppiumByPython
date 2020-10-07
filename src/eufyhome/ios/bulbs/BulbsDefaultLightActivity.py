class BulbsDefaultLightActivity(object):
    # 返回
    back_setting = ('name', 'common icon back')

    # 最后一次灯效
    last_title = ('name', 'Last On Status')

    # 最后一次灯效选择标识
    last_status_icon = ('xpath', '//XCUIElementTypeStaticText[@name="Last On Status"]/../XCUIElementTypeImage[@name="common_icon_select"]')

    # 自定义灯效
    custom_title = ('name', 'Custom Light Status')

    # 自定义灯效标识
    custom_status_icon = ('xpath', '//XCUIElementTypeStaticText[@name="Custom Light Status"]/../XCUIElementTypeImage[@name="common_icon_select"]')

    # 自定义灯效确认
    custom_done = ('name', 'Done')

    # white
    white_btn = ('name', 'bulb mode icon white')

    # color
    color_btn = ('name', 'bulb mode icon color')