class BulbsFavoriteActivity(object):

    # 收藏名
    favorite_name = ('xpath', '//XCUIElementTypeStaticText[@name="Favorites"]/../XCUIElementTypeCell/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[2]')

    # 添加人信息
    favorite_adder = ('xpath', '//XCUIElementTypeStaticText[@name="Favorites"]/../XCUIElementTypeCell/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[3]')

    # 亮度值
    favorite_lum = ('xpath', '//XCUIElementTypeStaticText[@name="Favorites"]/../XCUIElementTypeCell/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[1]')

    # 选择按钮
    select_favorite_btn = ('xpath', '//XCUIElementTypeStaticText[@name="Favorites"]/../XCUIElementTypeCell/XCUIElementTypeOther[1]/XCUIElementTypeButton')

    # 操作说明
    detail = ('name', 'bulb icon information')

    # 关闭
    back_bulbs = ('name', 'common icon back')

    # 删除专用滑动区域
    delete_swipe_btn = ('xpath', '//*[@name="Favorites"]/../XCUIElementTypeCell')

    # 删除按钮
    delete_btn = ('name', 'Delete')
