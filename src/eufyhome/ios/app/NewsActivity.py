class NewsActivity(object):
    # 消息列表返回
    back_system = ('name', 'common icon back')

    # 消息列表清除
    clear_news = ('name', 'Clear')

    # 消息模块
    item_new = ('xpath', '//XCUIElementTypeApplication[@name="EufyHome"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/'
                         'XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/'
                         'XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell')

    # 左滑删除按钮
    delete_news = ('name', 'notifications icon close')

    # 一件清除确认弹窗, yes
    clear_window = ('name', 'Are you sure you want to delete all notifications?')
