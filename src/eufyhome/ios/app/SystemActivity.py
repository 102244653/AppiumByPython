class SystemActivity(object):

    # 账号昵称
    account = ('xpath', '//XCUIElementTypeStaticText[@name="View Account"]/../XCUIElementTypeStaticText[1]')

    # 查看当前账号
    view_account = ('name', 'View Account')

    # 返回按钮
    back_home = ('name', 'common icon menu back')

    # 消息
    news = ('name', 'Notifications')

    # 消息通知小红点
    news_tip = ('xpath', '//XCUIElementTypeApplication[@name="EufyHome"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                         '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]')

    # 设备共享
    device_sharing = ('name', 'Device Sharing')

    # 时区
    timezone = ('name', 'Timezone')

    # 帮助
    help = ('name', 'Help & Feedback')

    # 语言
    language = ('xpath', '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]'
                         '/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]'
                         '/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[6]/XCUIElementTypeStaticText[1]')
