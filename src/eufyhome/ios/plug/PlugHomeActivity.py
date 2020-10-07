class PlugHomeActivity(object):
    # 返回
    back_home = ('name', 'common icon back white')

    # 设置
    plug_setting = ('name', 'common icon more')

    # 设备名
    plug_name = ('xpath', '//XCUIElementTypeButton[starts-with(@name,"plug icon o")]/../preceding-sibling::XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText')

    # 开关按钮
    plug_btn = ('xpath', '//XCUIElementTypeButton[starts-with(@name,"plug icon o")]')

    # 设备状态
    plug_status = ('xpath', '//XCUIElementTypeButton[starts-with(@name,"plug icon o")]/../XCUIElementTypeStaticText')

    # 定时任务
    schedules = ('name', 'bulb icon schedual')

    # 倒计时
    timer = ('name', 'switch icon timer')

    # 耗电量
    energy = ('xpath', '//XCUIElementTypeStaticText[contains(@name,"kWh")]')

    # 运行时间
    runtime = ('xpath', '//XCUIElementTypeStaticText[contains(@name,"hrs")]')

    # ************************跳过引导************************** #
    # 跳过
    skip_guide = ('name', 'Skip')

    # 结束引导
    end_guide = ('name', 'Done')