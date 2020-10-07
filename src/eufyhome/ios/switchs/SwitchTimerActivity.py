class SwitchTimerActivity(object):
    # 返回
    back_switch = ('name', 'common icon back')

    # 开
    on = ('xpath', '//XCUIElementTypeStaticText[@name="ON"]/../XCUIElementTypeButton[1]')

    # 关
    off = ('xpath', '//XCUIElementTypeStaticText[@name="OFF"]/../XCUIElementTypeButton[1]')

    # 开始倒计时按钮
    start = ('name', 'Start')

    # 倒计时当前开关状态显示
    switch_status = ('xpath', '//XCUIElementTypeImage[@name="switch_icon_timer_on_big"]/following-sibling:: XCUIElementTypeStaticText')

    # 停止倒计时按钮
    stop = ('name', 'Stop')

