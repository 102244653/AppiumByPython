class RoboticMaintenanceActivity(object):
    # 返回界面
    back_setting = ('id', 'com.eufylife.smarthome:id/common_header_start_icon')

    # 清除
    clear_all = ('id', 'com.eufylife.smarthome:id/common_header_end_tv')

    # 滤网
    filter = ('xpath', '//*[@text="Filter"]')

    # 滤网使用率
    filter_percent = ('xpath', '//*[@text="Filter"]/../android.widget.TextView[2]')

    # 滚轮
    rolling = ('xpath', '//*[@text="Rolling Brush"]')

    # 滚轮使用率
    rolling_percent = ('xpath', '//*[@text="Rolling Brush"]/../android.widget.TextView[2]')

    # 刷子
    side = ('xpath', '//*[@text="Side Brush"]')

    # 刷子使用率
    side_percent = ('xpath', '//*[@text="Side Brush"]/../android.widget.TextView[2]')

    # 传感器
    sensors = ('xpath', '//*[@text="Sensors"]')

    # 传感器使用率
    sensors_percent = ('xpath', '//*[@text="Sensors"]/../android.widget.TextView[2]')

    # 重置滤网
    reset_filter = ('id', 'com.eufylife.smarthome:id/reset_btn')

