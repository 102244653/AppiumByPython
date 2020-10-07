class SystemActivity(object):
    # 账号昵称
    account = ('id', 'com.eufylife.smarthome:id/nick_name_tv')

    # 查看当前账号
    view_account = ('android', 'text("View Account")')

    # 返回按钮
    back_home = ('id', 'com.eufylife.smarthome:id/common_header_end_icon')

    # 消息
    news = ('android', 'text("Notifications")')

    # 消息通知小红点
    news_tip = ('xpath', '//*[@resource-id="com.eufylife.smarthome:id/navigation_recycler_view"]'
                         '/android.widget.LinearLayout[1]/android.view.View[2]')

    # 设备共享
    device_sharing = ('android', 'text("Device Sharing")')

    # 时区
    timezone = ('android', 'text("Timezone")')

    # 帮助
    help = ('android', 'text("Help & Feedback")')

    # 语言
    language = ('xpath', '//*[@resource-id="com.eufylife.smarthome:id/navigation_recycler_view"]/android.widget.LinearLayout[6]/android.widget.TextView')
