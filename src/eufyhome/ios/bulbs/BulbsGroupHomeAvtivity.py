class BulbsGroupHomeActivity(object):
    # 返回
    back_home = ('name', 'common icon back white')

    # 分组名
    home_group_name = ('xpath', '//XCUIElementTypeImage[@name="group_icon_kitchen_gray"]/following-sibling:: XCUIElementTypeStaticText[1]')

    # 模式
    group_effect = ('name', 'bulb icon mode')

    # 分组设置
    group_setting = ('name', 'bulb icon group')

    # 灯组是否开启
    group_is_on = ('xpath', '//XCUIElementTypeImage[@name="bulb_img_mask"]/following-sibling::XCUIElementTypeOther[2]/XCUIElementTypeStaticText')

    # 灯组界面灯泡按钮
    group_bulbs_bar = ('xpath', '//XCUIElementTypeImage[@name="bulb_img_mask"]/../XCUIElementTypeButton')

    # 灯组的状态
    group_home_status = ('xpath', '//XCUIElementTypeImage[@name="group_icon_kitchen_gray"]/following-sibling:: XCUIElementTypeStaticText[2]')

    # *******************************分组设置界面********************************** #

    #  返回
    back_group = ('name', 'common icon back')

    # 分组名
    setting_group_name = ('xpath', '//XCUIElementTypeOther[@name="Select Bulbs"]/XCUIElementTypeButton[2]')

    # 组名编辑
    edit_group_name = ('xpath', '//XCUIElementTypeButton[@name="Save"]/../XCUIElementTypeTextField')

    # 保存
    save_group_name = ('name', 'Save')

    # 删除分组
    delete_group = ('name', 'Delete this Group')

    # 设置保存
    save = ('name', 'Save')

    # *******************************分组模式界面********************************** #

    # white模式
    white_btn = ('name', 'bulb mode icon white')

    # flow模式
    flow_btn = ('name', 'bulb mode icon flow')

    # color模式
    color_btn = ('name', 'bulb mode icon color')

    # 关闭按钮
    close_effect = ('name', 'common icon close black')

    # 灯效
    effect_text = ('xpath', '//XCUIElementTypeImage[@name="bulb_img_bg"]/../preceding-sibling::XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeStaticText[2]')
