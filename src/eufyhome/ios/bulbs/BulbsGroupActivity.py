class BulbsGroupActivity(object):
    # 返回
    back_setting = ('name', 'common icon back')

    # 添加
    null_add_group = ('name', 'Add Group')
    add_group = ('name', 'common icon add')

    # ******************场景选择*********************** #

    # 取消添加
    cancel_add = ('name', 'Cancel')

    # 下一步
    next_add = ('name', 'Next')

    # 场景图标
    icons = ('xpath', '//XCUIElementTypeStaticText[@name="Select an icon for group"]/../XCUIElementTypeOther[1]/XCUIElementTypeScrollView/XCUIElementTypeButton')

    # *****************添加界面************************ #
    # 返回选择界面
    back_select_icon = ('name', 'common icon back')

    # 保存按钮
    save_group = ('name', 'Save')

    # 分组名称
    group_name = ('xpath', '//XCUIElementTypeOther[@name="Select Bulbs"]/XCUIElementTypeButton[2]')

    # 设备名称
    device_name = ('xpath', '//XCUIElementTypeOther[@name="Select Bulbs"]/../XCUIElementTypeCell/XCUIElementTypeStaticText')

    # **********************编辑设备名********************** #

    # 分组名编辑框
    group_name_edit = ('xpath', '//XCUIElementTypeButton[@name="signup icon close"]/../XCUIElementTypeTextField')

    # 保存
    save_name = ('name', 'Save')

    # **********************编辑设备名********************** #

    list_name = ('xpath', '//XCUIElementTypeOther[@name="Groups"]/following-sibling::XCUIElementTypeCell/XCUIElementTypeStaticText')

    # 删除分组
    delete_group_btn = ('xpath', '//*[@text="Delete this Group"]')

