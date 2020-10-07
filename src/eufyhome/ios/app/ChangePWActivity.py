class ChangePWActivity(object):
    # 修改密码返回按钮
    back_user = ('name', 'common icon back')

    # 确认当前密码
    old_pwd = ('name', 'Current Password')

    # 旧密码可见
    old_pwd_visible = ('xpath', '(//XCUIElementTypeButton[@name="signup icon closeeyes"])[1]')

    # 新密码
    new_pwd = ('name', 'New Password')

    # 新密码可见
    new_pwd_visible = ('xpath', '(//XCUIElementTypeButton[@name="signup icon closeeyes"])[2]')

    # 提交修改密码
    submit_change = ('name', 'Save Password')

    # 修改错误的提示
    old_pwd_error_text = ('name', 'The password you entered is incorrect.')
    new_pw_error_text = ('name', 'Your password must be 8-20 characters long.')

    # 修改密码错误提示关闭按钮
    close_change_fail = ('name', 'signup icon close')
