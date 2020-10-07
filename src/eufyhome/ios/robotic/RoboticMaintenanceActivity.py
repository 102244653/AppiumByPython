class RoboticMaintenanceActivity(object):
    # 返回界面
    back_setting = ('name', 'common icon back')

    # 清除
    clear_all = ('name', 'Clear')

    # 滤网
    filter = ('name', 'Filter')

    # 滤网使用率
    filter_percent = ('xpath', '//XCUIElementTypeStaticText[@name="Filter"]/../XCUIElementTypeStaticText[2]')

    # 滚轮
    rolling = ('name', 'Rolling Brush')

    # 滚轮使用率
    rolling_percent = ('xpath', '//XCUIElementTypeStaticText[@name="Rolling Brush"]/../XCUIElementTypeStaticText[2]')

    # 刷子
    side = ('name', 'Side Brush')

    # 刷子使用率
    side_percent = ('xpath', '//XCUIElementTypeStaticText[@name="Side Brush"]/../XCUIElementTypeStaticText[2]')

    # 传感器
    sensors = ('name', 'Sensors')

    # 传感器使用率
    sensors_percent = ('xpath', '//XCUIElementTypeStaticText[@name="Sensors"]/../XCUIElementTypeStaticText[2]')

    # 重置滤网
    reset_filter = ('name', 'Reset Filter')

