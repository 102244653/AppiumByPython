class HomeActivity(object):
    # 左上角个人中心入口
    menu_icon = ('id', 'com.eufylife.smarthome:id/menu_icon')

    # APP主页欢迎词
    welcome = ('xpath', '//*[@text="Welcome Home"]')

    # 用户昵称
    username = ('id', 'com.eufylife.smarthome:id/subUser')

    # help按钮
    home_help = ('id', 'com.eufylife.smarthome:id/tv_help')

    # 添加设备（+）
    add_device = ('id', 'com.eufylife.smarthome:id/add_device')

    # 添加设备按钮（无设备时）
    null_add_device = ('id', 'com.eufylife.smarthome:id/add_layout')

    # 设备模块
    item_device = ('id', 'com.eufylife.smarthome:id/item_device')

    # 设备名
    device_name = ('id', 'com.eufylife.smarthome:id/device_name')

    # 设备状态
    device_status = ('id', 'com.eufylife.smarthome:id/device_status')

    # 设备开关
    device_btn = ('id', 'com.eufylife.smarthome:id/bt_layout')

    # 分组名称
    group_name = ('id', 'com.eufylife.smarthome:id/group_name')



    # 设备的状态等元素，根据设备名的相对位置来确定，需单一已处理 #
    # 设备名称
    T2123_name = ('xpath', '//android.widget.TextView[starts-with(@text,"T2123")]')
    T2250_name = ('xpath', '//android.widget.TextView[starts-with(@text,"T2250")]')
    T2190_name = ('xpath', '//android.widget.TextView[starts-with(@text,"T2190")]')

    # 设备状态
    T2123_status = ('xpath', '//android.widget.TextView[starts-with(@text,"T2123")]/../*[@resource-id="com.eufylife.smarthome:id/device_status"]')
    T2250_status = ('xpath', '//android.widget.TextView[starts-with(@text,"T2250")]/../*[@resource-id="com.eufylife.smarthome:id/device_status"]')
    T2190_status = ('xpath', '//android.widget.TextView[starts-with(@text,"T2190")]/../*[@resource-id="com.eufylife.smarthome:id/device_status"]')

    # 设备开关
    T2123_switch = ('xpath', '//android.widget.TextView[starts-with(@text,"T2123")]/../*[@resource-id="com.eufylife.smarthome:id/bt_layout"]')
    T2250_switch = ('xpath', '//android.widget.TextView[starts-with(@text,"T2250")]/../*[@resource-id="com.eufylife.smarthome:id/bt_layout"]')
    T2190_switch = ('xpath', '//android.widget.TextView[starts-with(@text,"T2190")]/../*[@resource-id="com.eufylife.smarthome:id/bt_layout"]')

    # 固件升级标识(使用整个设备模块截图比对)
    T2123_update = ('xpath', '//android.widget.TextView[starts-with(@text,"T2123")]/../android.widget.ImageView[@resource-id="com.eufylife.smarthome:id/firmware_dot"]')
    T2250_update = ('xpath', '//android.widget.TextView[starts-with(@text,"T2250")]/../android.widget.ImageView[@resource-id="com.eufylife.smarthome:id/firmware_dot"]')
    T2190_update = ('xpath', '//android.widget.TextView[starts-with(@text,"T2190")]/../android.widget.ImageView[@resource-id="com.eufylife.smarthome:id/firmware_dot"]')
    # 灯泡
    T1013_update = ('xpath', '//android.widget.TextView[starts-with(@text,"T1013")]/../android.widget.ImageView[@resource-id="com.eufylife.smarthome:id/firmware_dot"]')
    # 插座
    T1100_update = ('xpath', '//android.widget.TextView[starts-with(@text,"T1100")]/../android.widget.ImageView[@resource-id="com.eufylife.smarthome:id/firmware_dot"]')
    # 开关
    T1211_update = ('xpath', '//android.widget.TextView[starts-with(@text,"T1211")]/../android.widget.ImageView[@resource-id="com.eufylife.smarthome:id/firmware_dot"]')

    # 定时任务标识
    T2123_schedule = ('xpath', '//android.widget.TextView[starts-with(@text,"T2123")]/../*[@resource-id="com.eufylife.smarthome:id/schedule_icon"]')
    T2250_schedule = ('xpath', '//android.widget.TextView[starts-with(@text,"T2250")]/../*[@resource-id="com.eufylife.smarthome:id/schedule_icon"]')
    T2190_schedule = ('xpath', '//android.widget.TextView[starts-with(@text,"T2190")]/../*[@resource-id="com.eufylife.smarthome:id/schedule_icon"]')
    T1013_schedule = ('xpath', '//android.widget.TextView[starts-with(@text,"T1013")]/../*[@resource-id="com.eufylife.smarthome:id/schedule_icon"]')
    T1100_schedule = ('xpath', '//android.widget.TextView[starts-with(@text,"T1100")]/../*[@resource-id="com.eufylife.smarthome:id/schedule_icon"]')
    T1211_schedule = ('xpath', '//android.widget.TextView[starts-with(@text,"T1211")]/../*[@resource-id="com.eufylife.smarthome:id/schedule_icon"]')

    # 灯组开关
    bulbs_group_btn = ('xpath', '//*[@text="bgroup"]/../*[@resource-id="com.eufylife.smarthome:id/sv"]')

    # 灯组状态
    bulbs_group_status = ('xpath', '//*[@text="bgroup"]/../*[@resource-id="com.eufylife.smarthome:id/group_status"]')
