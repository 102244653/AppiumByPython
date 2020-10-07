class BulbsEffectActivity(object):
    # 灯效（页面标题）
    bulb_title = ('xpath', '//XCUIElementTypeImage[@name="bulb_img_bg"]/../preceding-sibling::XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeStaticText[2]')

    # 灯泡
    bulbs_btn = ('xpath', '//XCUIElementTypeImage[@name="bulb_img_mask"]/../XCUIElementTypeButton')

    # white模式
    bulbs_white = ('name', 'bulb mode icon white')

    # recommended
    bulbs_recommended = ('name', 'bulb mode icon recommend')

    bulbs_music = ('name', 'bulb mode icon music')

    bulbs_color = ('name', 'bulb mode icon color')

    bulbs_flow = ('name', 'bulb mode icon flow')

    # # Relax
    # Relax = ()
    #
    # # Read
    # Read = ()
    #
    # # Focus
    # Focus = ()
    #
    # # Night Light
    # Night_Light = ()

    # 关闭界面
    close_effect = ('name', 'common icon close black')

    # 灯效区域
    color_area = ()

    # 添加收藏
    add_favorite = ('name', 'bulb icon add favorite')

    # ********************* favorite ******************** #

    # 收藏名称
    favorite_name = ('xpath', '//XCUIElementTypeStaticText[@name="Add To Favorites"]/../XCUIElementTypeOther[1]/XCUIElementTypeTextField')

    # 收藏亮度值
    favorite_lightness = ('xpath', '//XCUIElementTypeStaticText[@name="Add To Favorites"]/../XCUIElementTypeStaticText[2]')

    # 保存按钮
    save_favorite = ('name', 'Save')
