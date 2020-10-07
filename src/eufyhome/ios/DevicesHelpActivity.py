class DevicesHelpActivity:
    # 返回设置界面
    back_setting = ('name', 'common icon back')

    # 查看所有
    see_all = ('name', 'See All')

    # 反馈
    feed_back = ('name', 'Feedback')

    # 交流
    chat = ('name', 'Chat')

    # 通讯录
    call_us = ('name', 'Call Us')

    # 列表标题
    title_list = ('xpath', '(//XCUIElementTypeImage[@name="common_icon_lists_arrow"])/../XCUIElementTypeStaticText')

    # us电话
    us_phone = ('xpath', '//XCUIElementTypeStaticText[@name="(US)"]/preceding-sibling:: XCUIElementTypeStaticText[1]')

    # uk电话
    uk_phone = ('xpath', '//XCUIElementTypeStaticText[@name="(UK)"]/preceding-sibling:: XCUIElementTypeStaticText[1]')

    # de电话
    de_phone = ('xpath', '//XCUIElementTypeStaticText[@name="(DE)"]/preceding-sibling:: XCUIElementTypeStaticText[1]')

    # jp电话
    jp_phone = ('xpath', '//XCUIElementTypeStaticText[@name="(JP)"]/preceding-sibling:: XCUIElementTypeStaticText[1]')

    # *******************问题反馈*************************** #
    # 反馈内容
    feed_back_text = ('xpath', '//XCUIElementTypeStaticText[ends-with(@name, "/200")]/../XCUIElementTypeTextView')

    # 提交
    submit = ('name', 'Submit')

    # 搜索
    search_input = ('name', 'Search devices')

    # 搜索结果list
    result_list = ('xpath', '(//XCUIElementTypeImage[@name="common_icon_lists_arrow"])/../XCUIElementTypeStaticText')

    # 问题类型
    issue_type = ('name', 'Other issue')

