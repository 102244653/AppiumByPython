class SwitchHomeActivity(object):
    # 返回
    back_home = ('name', 'common icon back white')

    # 设置
    switch_setting = ('name', 'common icon more')

    # 设备名
    device_name = ('xpath', '//XCUIElementTypeButton[@name="switch icon off"]/../preceding-sibling::XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText')

    # 开关按扭
    switch_btn = ('xpath', '//XCUIElementTypeButton[starts-with(@name,"switch icon o")]')

    # 设备状态
    switch_status = ('xpath', '//XCUIElementTypeButton[starts-with(@name,"switch icon o")]/../XCUIElementTypeStaticText')

    # 定时任务
    schedules = ('name', 'bulb icon schedual')

    # 定时器
    timer = ('name', 'switch icon timer')

    # ************************跳过引导************************** #
    # 跳过
    skip_guide = ('name', 'Skip')

    # 结束引导
    end_guide = ('name', 'Done')
