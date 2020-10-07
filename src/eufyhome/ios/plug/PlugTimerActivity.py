class PlugTimerActivity(object):
    # 返回
    back_plug = ('name', 'common icon back')

    # 开
    on = ('xpath', '//XCUIElementTypeStaticText[@name="ON"]/../XCUIElementTypeButton[1]')

    # 关
    off = ('xpath', '//XCUIElementTypeStaticText[@name="OFF"]/../XCUIElementTypeButton[1]')

    # 开始倒计时按钮
    start = ('name', 'Start')

    # 停止倒计时按钮
    stop = ('name', 'Stop')

