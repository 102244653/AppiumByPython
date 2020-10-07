class HomeActivity(object):

    # 左上角个人中心入口
    menu_icon = ('name', 'common icon menu')

    # app主页的欢迎词
    welcome = ("name", "Welcome Home")

    # 用户昵称
    username = ('xpath', '//XCUIElementTypeStaticText[@name="Welcome Home"]/../../XCUIElementTypeStaticText[1]')

    # help按钮
    home_help = ('name', 'common nav icon help')

    # 添加设备按钮（无设备时）
    null_add_device = ('name', 'Add Device')
    add_device = ('name', 'common nav icon add')

    # 设备模块
    item_device = ('xpath', '//XCUIElementTypeApplication[@name="EufyHome"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/'
                       'XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/'
                       'XCUIElementTypeCell/XCUIElementTypeImage')

    # 分组名称
    group_name = ('xpath', '//XCUIElementTypeStaticText[@name="Groups"]/../following-sibling::XCUIElementTypeCell/XCUIElementTypeCollectionView/XCUIElementTypeCell/XCUIElementTypeStaticText[1]')

    # 设备名
    device_name = ('xpath', '//XCUIElementTypeStaticText[@name="Devices"]/../following-sibling::XCUIElementTypeCell/XCUIElementTypeStaticText[1]')

    # 设备状态
    device_status = ('xpath', '//XCUIElementTypeStaticText[@name="Devices"]/../following-sibling::XCUIElementTypeCell/XCUIElementTypeStaticText[2]')

    # 设备开关
    device_btn = ('xpath', '//XCUIElementTypeStaticText[@name="Devices"]/../following-sibling::XCUIElementTypeCell/XCUIElementTypeButton[last()]')

    # 固件升级标识(使用整个设备模块截图比对)
    T2123_update = ('xpath', '//XCUIElementTypeStaticText[@name="T2123"]/../XCUIElementTypeButton[@name="home icon update"]')

    T2250_update = ('xpath', '//XCUIElementTypeStaticText[@name="T2250"]/../XCUIElementTypeButton[@name="home icon update"]')

    T2190_update = ('xpath', '//XCUIElementTypeStaticText[@name="T2190"]/../XCUIElementTypeButton[@name="home icon update"]')

    # 灯组开关
    bulbs_group_btn = ('xpath', '//*[@name="bgroup"]/../XCUIElementTypeButton')

    # 灯组状态
    bulbs_group_status = ('xpath', '//*[@name="bgroup"]/../XCUIElementTypeStaticText[2]')
