class RoboticSuctionActivity(object):
    # ******************t2190******************** #
    # 吸力弹窗关闭按钮
    T2190_power_close = ('name', 'suction icon close')

    # 吸力-标准档
    T2190_power_standard = ('name', 'Standard')

    # 吸力-max
    T2190_power_max = ('name', 'Max')

    # 设备吸力档位
    T2190_power_quiet = ('name', 'Quiet')

    T2190_power_turbo = ('name', 'Turbo')

    T2190_power_quiet_icon = ('xpath', '//XCUIElementTypeStaticText[@name="Quiet"]'
                                       '/following-sibling::XCUIElementTypeButton')

    T2190_power_standard_icon = ('xpath', '//XCUIElementTypeStaticText[@name="Standard"]'
                                          '/following-sibling::XCUIElementTypeButton')

    # 选择后的小勾图标
    T2190_power_turbo_icon = ('xpath', '//XCUIElementTypeStaticText[@name="Turbo"]'
                                       '/following-sibling::XCUIElementTypeButton')

    T2190_power_max_icon = ('xpath', '//XCUIElementTypeStaticText[@name="Max"]/following-sibling::XCUIElementTypeButton')

    T2190_power_boostiq = ('name', 'common btn bg off')

    # ******************t2250******************** #
    # 吸力弹窗关闭按钮
    T2250_power_close = ('name', 'suction icon close')

    # 吸力-标准档
    T2250_power_standard = ('name', 'Standard')
    T2250_power_standard_icon = ('xpath', '//XCUIElementTypeStaticText[@name="Standard"]/following-sibling::XCUIElementTypeButton')

    # 吸力-turbo
    T2250_power_turbo = ('name', 'Turbo')
    T2250_power_turbo_icon = ('xpath', '//XCUIElementTypeStaticText[@name="Turbo"]/following-sibling::XCUIElementTypeButton')

    # 吸力-max
    T2250_power_max = ('name', 'Max')
    T2250_power_max_icon = ('xpath', '//XCUIElementTypeStaticText[@name="Max"]/following-sibling::XCUIElementTypeButton')

    # boostiq
    T2250_power_boostiq = ('name', 'BoostIQ™')
    T2250_power_boostiq_icon = ('xpath', '//XCUIElementTypeStaticText[@name="BoostIQ™"]/following-sibling::XCUIElementTypeButton')

    # ******************t2123******************** #
    # 吸力-标准
    T2123_power_standard = ('name', 'Standard')

    # 吸力-boostiq
    T2123_power_boostiq = ('xpath', '//XCUIElementTypeButton[starts-with(@name,"BoostIQ")]')

    # 吸力-max
    T2123_power_max = ('name', 'Max')

    # 关闭模式界面
    T2123_power_close = ('name', 'common icon close black')
