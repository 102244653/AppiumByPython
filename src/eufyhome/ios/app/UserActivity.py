class UserActivity(object):

    # 返回按钮
    back_btn = ('name', 'common icon back')

    # 用户昵称
    username = ('xpath', '//XCUIElementTypeButton[@name="common icon back"]/../following-sibling::XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeButton[2]')

    # 用户昵称输入框
    username_input = ('xpath', '//XCUIElementTypeButton[@name="Save"]/../XCUIElementTypeTextField')

    # 昵称修改保存按钮
    save_btn = ('name', 'Save')

    # 账号
    user_id = ('xpath', '//XCUIElementTypeButton[@name="common icon back"]/../following-sibling::XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText')

    # 修改密码
    chang_password = ('name', 'Change Password')

    # 退出账号
    sign_out = ('name', 'Sign Out')

    # 退出确认弹窗
    logout_tip = ('name', 'Are you sure you want to sign out?')

    # 进入注销账号
    delete_account = ('name', 'Delete Account')

    # 删除账号
    delete = ('name', 'Delete')

    # 删除账号确认弹窗
    delete_window = ('name', 'Are you sure you want to delete this account?')
