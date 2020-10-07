class RoboticManualActivity(object):
    # 返回
    back_setting = ('name', 'common icon back')

    # *************************t2190/t2250************************* #
    # 定点清扫
    spot = ('xpath', '//XCUIElementTypeButton[starts-with(@name,"control icon spot")]')

    # 清扫按钮
    clean = ('name', 'home icon clean')

    # 回充
    recharge = ('name', 'control icon recharge')

    # stop spot
    stop_spot = ('name', 'Stop Spot Cleaning')
