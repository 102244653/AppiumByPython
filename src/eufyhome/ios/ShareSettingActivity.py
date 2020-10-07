class ShareSettingActivity(object):
    # 分享列表返回
    back_setting = ('name', 'common icon back')

    # 添加用户(无分享人时添加按钮)
    share_null_add = ('name', 'Add Member')

    # 添加用户（已有分享者）
    share_add = ('name', 'common icon add')

    # 被分享人模块:被分享人昵称（list）
    share_member_item = ('xpath', '//XCUIElementTypeStaticText[starts-with(@name,"Send an invite to share")]/../following-sibling::XCUIElementTypeCell/XCUIElementTypeStaticText[1]')

    # 移除分享人
    share_remove = ('name', 'Remove')

    # 移除确认
    commit_remove = ('xpath', '(//XCUIElementTypeButton[@name="Remove"])[2]')

    # *********************************#

    # 分享页面的返回分享列表
    back_share = ('name', 'common icon back')

    # 被分享人账号
    share_member_input = ('name', 'Email')
    share_member_phone_input = ('ios', 'type="XCUIElementTypeTextField"')

    # 提交分享
    share_commit = ('name', 'Send Invitation')

    # # 邮箱格式错误提示
    # share_tip = ('', '')
    #
    # # 邮箱格式错误提示关闭按钮
    # close_share_tip = ()

    # 分享成功或者失败标题
    share_fail = ('name', 'Failed to share')
    share_success = ('name', 'Sent Successfully')

    # 分享确认按钮（OK）
    share_ok = ('id', 'com.eufylife.smarthome:id/dialog_btn')

    # 设备分享
    share_device = ('id', 'com.eufylife.smarthome:id/share_settings')


