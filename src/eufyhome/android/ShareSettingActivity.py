class ShareSettingActivity(object):
    # 分享列表返回
    back_setting = ('id', 'com.eufylife.smarthome:id/common_header_start_icon')

    # 添加用户(无分享人时添加按钮)
    share_null_add = ('id', 'com.eufylife.smarthome:id/share_mine_device_add_member_btn')

    # 添加用户（已有分享者）
    share_add = ('id', 'com.eufylife.smarthome:id/common_header_end_icon')

    # 被分享人模块（list）
    share_member_item = ('xpath', '//*[@resource-id="com.eufylife.smarthome:id/share_mine_device_recycler_view"]/android.widget.'
                                  'LinearLayout[*]/android.widget.LinearLayout[1]/android.widget.TextView[1]')

    # 移除分享人
    share_remove = ('xpath', '//*[@text="Remove"]')

    # 移除分享人确认
    commit_remove = ('id', 'com.eufylife.smarthome:id/dialog_btn_right')

    # *********************************#

    # 分享页面的返回分享列表
    back_share = ('id', 'com.eufylife.smarthome:id/common_header_start_icon')

    # 被分享人账号
    share_member_input = ('id', 'com.eufylife.smarthome:id/email_et')

    # 提交分享
    share_commit = ('id', 'com.eufylife.smarthome:id/submit_btn')

    # 邮箱格式错误提示
    share_tip = ('id', 'com.eufylife.smarthome:id/error_email_describe_tv')

    # 邮箱格式错误提示关闭按钮
    close_share_tip = ('id', 'com.eufylife.smarthome:id/email_close_view')

    # 分享成功或者失败标题
    share_fail = ('xpath', '//*[@text="Failed to share"]')
    share_success = ('xpath', '//*[@text="Sent Successfully"]')

    # 分享确认按钮（OK）
    share_ok = ('id', 'com.eufylife.smarthome:id/dialog_btn')

    # 设备分享
    share_device = ('id', 'com.eufylife.smarthome:id/share_settings')

