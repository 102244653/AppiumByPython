class TimeZoneActivity(object):
    # 返回按钮
    back_system = ('name', 'common icon back')

    # 北京时区
    beijing = ('name', 'Beijing, Shanghai, Chongqing,Urumqi')

    # 北京时区的勾
    is_beijing = ('xpath', '//XCUIElementTypeStaticText[@name="Beijing, Shanghai, Chongqing,Urumqi"]'
                           '/../following-sibling::XCUIElementTypeImage')  # [@name="common_icon_select"]

    # 香港时区
    hongkong = ('name', 'Hong Kong')

    # 香港时区的勾
    is_hongkong = ('xpath', '//XCUIElementTypeStaticText[@name="Hong Kong"]/../following-sibling::XCUIElementTypeImage')

    # 第一个时区
    time_one = ('xpath', '//XCUIElementTypeStaticText[@name="Timezone"]/following-sibling::XCUIElementTypeCell[1]/XCUIElementTypeStaticText[1]/XCUIElementTypeStaticText[1]')

    # 时区模块
    timezone_item = ('xpath', '//XCUIElementTypeStaticText[@name="Timezone"]/../XCUIElementTypeCell')

