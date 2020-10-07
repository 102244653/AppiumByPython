class BulbsHomeActivity(object):
    # 返回
    back_home = ('name', 'common icon back white')

    # 离线等弹窗
    offline_window = ('name', 'Device is offline')

    # 灯泡设置
    bulb_setting = ('name', 'common icon more')

    # 设备名称
    device_name = ('xpath', '//XCUIElementTypeButton[@name="common icon more"]/../following-sibling::XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeStaticText')

    # 灯泡背景
    bulb_mask_view = ('xpath', '//XCUIElementTypeImage[@name="bulb_img_mask"]')

    # 灯泡亮度调节
    bulb_progress_bar = ('xpath', '//XCUIElementTypeImage[@name="bulb_img_mask"]/../XCUIElementTypeButton')

    # 模式
    effect = ('name', 'bulb icon mode')

    # 定时任务
    color_schedules = ('name', 'bulb icon schedual')
    white_schedules = ('name', 'bulb icon schedual')

    # 收藏
    favorites_page = ('name', 'bulb icon favorites')
    white_favorites_page = ('name', 'bulb icon favorites')

    add_white_favorites = ('name', 'bulb icon add favorite')

    # 白色灯效
    bulb_color = ('xpath', '//XCUIElementTypeImage[@name="bulb_img_mask"]/following-sibling::XCUIElementTypeOther[2]/XCUIElementTypeStaticText')

    # ************************跳过引导************************** #
    # 跳过
    skip_guide = ('name', 'Skip')

    # 结束引导
    end_guide = ('name', 'Done')
