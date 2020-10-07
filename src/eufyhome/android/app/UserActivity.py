class UserActivity(object):

    # 返回按钮
    back_btn = ('id', 'com.eufylife.smarthome:id/common_header_start_icon')

    # 用户昵称
    username = ('id', 'com.eufylife.smarthome:id/nick_name_tv')

    # 用户昵称输入框
    username_input = ('id', 'com.eufylife.smarthome:id/device_name_edt')

    # 昵称修改保存按钮
    save_btn = ('id', 'com.eufylife.smarthome:id/submit_btn')

    # 账号
    user_id = ('xpath', '//*[@resource-id="com.eufylife.smarthome:id/nick_name_tv"]/following-sibling::android.widget.TextView[1]')

    # 修改密码
    chang_password = ('android', 'text("Change Password")')

    # 退出账号
    sign_out = ('xpath', '//*[@text="Sign Out"]')

    # 退出确认弹窗
    logout_tip = ('id', 'com.eufylife.smarthome:id/dialog_describe_tv')

    # 注销账号
    delete_account = ('android', 'text("Delete Account")')

    # 删除账号
    delete = ('android', 'text("Delete")')

    # 删除账号确认弹窗
    delete_window = ('id', 'com.eufylife.smarthome:id/dialog_describe_tv')




