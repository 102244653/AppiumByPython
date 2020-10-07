class AllShareActivity(object):
    """
    系统分享列表
    """
    # 返回按钮
    back_system = ('id', 'com.eufylife.smarthome:id/common_header_start_icon')

    # 分享给我的设备模块
    shared_to_me_device = ('xpath', '//*[@resource-id="com.eufylife.smarthome:id/device_shared_with_me"]/android.widget.LinearLayout[*]/android.widget.LinearLayout[1]/android.widget.TextView[1]')
