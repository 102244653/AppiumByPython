class ChangePWActivity(object):
    # 修改密码返回按钮
    back_user = ('id', 'com.eufylife.smarthome:id/common_header_start_icon')

    # 确认当前密码
    old_pwd = ('id', 'com.eufylife.smarthome:id/old_pwd_et')

    # 旧密码可见
    old_pwd_visible = ('id', 'com.eufylife.smarthome:id/old_visible_view')

    # 新密码
    new_pwd = ('id', 'com.eufylife.smarthome:id/new_pwd_et')

    # 新密码可见
    new_pwd_visible = ('id', 'com.eufylife.smarthome:id/new_visible_view')

    # 提交修改密码
    submit_change = ('id', 'com.eufylife.smarthome:id/submit_btn')

    # 修改错误的提示
    old_pwd_error_text = ('id', 'com.eufylife.smarthome:id/old_describe_tv')
    new_pw_error_text = ('id', 'com.eufylife.smarthome:id/describe_tv')

    # 修改密码错误提示关闭按钮
    close_change_fail = ('id', 'signup icon close')
