class RoboticHomeActivity(object):
    # 离线等弹窗
    offline_window = ('name', 'Device is offline')

    # 返回app主页按钮
    back_app = ('xpath', '//XCUIElementTypeButton[starts-with(@name,"common icon back")]')

    # 设备管理
    robotic_setting = ('xpath', '//XCUIElementTypeButton[starts-with(@name,"common icon more")]')

    T2250_robotic_setting = ('xpath', '//XCUIElementTypeButton[starts-with(@name,"eufy common")]')

    # 设别名称
    t2123_name = ('xpath', '//XCUIElementTypeButton[@name="common icon more"]/../following-sibling::XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeStaticText')
    t2250_name = ('xpath', '//XCUIElementTypeButton[@name="common icon back black"]/following-sibling::XCUIElementTypeStaticText/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText')
    t2190_name = ('xpath', '//XCUIElementTypeButton[@name="common icon back white"]/following-sibling::XCUIElementTypeStaticText/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText')

    # 设备状态
    t2123_status = ('xpath', '//XCUIElementTypeButton[@name="common icon more"]/../following-sibling::XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeButton')
    t2250_status = ('xpath', '(//XCUIElementTypeImage[@name="robovac_icon_battery"])[1]/../preceding-sibling::XCUIElementTypeStaticText')
    t2190_status = ('xpath', '//XCUIElementTypeStaticText[@name="Cleaning Area"]/../preceding-sibling::XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeStaticText')

    # 清扫记录
    clean_history = ('name', 'home icon history')

    # 清扫面积
    clean_area = (
    'xpath', '//XCUIElementTypeApplication[@name="EufyHome"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/'
             'XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
             '/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeStaticText')

    # 清扫时间
    clean_time = (
    'xpath', '//XCUIElementTypeApplication[@name="EufyHome"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther'
             '/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/'
             'XCUIElementTypeOther[3]/XCUIElementTypeStaticText[1]')

    # *******************T2123******************** #

    # 方向操作控件
    T2123_play = ('name', 'robovac icon play')

    # 上
    T2123_up = ('name', 'robovac icon arrow up')

    # 下
    T2123_down = ('name', 'robovac icon arrow down')

    # 左
    T2123_left = ('name', 'robovac icon arrow left')

    # 右
    T2123_right = ('name', 'robovac icon arrow right')

    # 模式
    T2123_mode = ('name', 'robovac icon model')

    # 定时计划
    T2123_schedules = ('name', 'robovac icon schedual')

    # 回充
    T2123_recharge = ('name', 'robovac icon home')

    # find me
    T2123_find_me = ('name', 'robovac icon find')

    # *******************T2250******************** #
    # 吸力设置
    T2250_power_set = ('name', 'home icon suction')

    # 开始暂停
    T2250_play = ('name', 'home icon clean')

    # 开始状态
    T2250_btn_status = ('xpath', '//XCUIElementTypeStaticText[@name="Suctions"]/following-sibling::XCUIElementTypeStaticText[1]')

    # 回充
    T2250_recharge = ('name', 'home icon recharge')

    # 定点清扫
    T2250_spot = ('name', 'homepage icon spot T2150')

    # 定时计划
    T2250_schedules = ('name', 'home icon schedule1')

    # *******************T2190******************** #


    # 吸力设置
    T2190_power_set = ('name', 'home icon suction')

    # 清扫
    T2190_play = ('name', 'home icon clean')

    # 回充
    T2190_recharge = ('name', 'home icon recharge')

    # 指定区域清扫
    T2190_zone_clean = ('name', 'home icon zone')

    # 定时计划
    T2190_schedule = ('name', 'home icon schedule1')

    # ************************跳过引导************************** #
    # 跳过
    skip_guide = ('name', 'Skip')

    # 结束引导
    end_guide = ('name', 'Done')

