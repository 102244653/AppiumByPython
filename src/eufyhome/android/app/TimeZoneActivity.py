class TimeZoneActivity(object):
    # 返回按钮
    back_system = ('id', 'com.eufylife.smarthome:id/common_header_start_icon')

    # 北京时区
    beijing = ('xpath', '//*[@text="Beijing, Shanghai, Chongqing, Urumqi"]')

    # 北京时区的勾
    is_beijing = ('xpath', '//*[@text="Beijing, Shanghai, Chongqing, Urumqi"]/../../android.widget.ImageView[1]')

    # 香港时区
    hongkong = ('xpath', '//*[@text="Hong Kong"]')

    # 香港时区的勾
    is_hongkong = ('xpath', '//*[@text="Hong Kong"]/../following-sibling::android.widget.ImageView[1]')

    # 第一个时区
    time_one = ('xpath', '//*[@text="Midway Island, Samoa"]')

    # 时区模块名称
    timezone_item = ('id', 'com.eufylife.smarthome:id/timezone_lst')
