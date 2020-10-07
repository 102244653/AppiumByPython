class SwitchHomeActivity(object):
    # 返回
    back_home = ('id', 'com.eufylife.smarthome:id/common_header_start_icon')

    # 设置
    switch_setting = ('id', 'com.eufylife.smarthome:id/common_header_end_icon')

    # 设备名
    device_name = ('id', 'com.eufylife.smarthome:id/title_tv')

    # 开关按扭
    switch_btn = ('xpath', '//*[@resource-id="android:id/content"]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]')

    # 设备状态
    switch_status = ('id', 'com.eufylife.smarthome:id/switch_controller_text')

    # 定时任务
    schedules = ('id', 'com.eufylife.smarthome:id/schedules_tv')

    # 定时器
    timer = ('id', 'com.eufylife.smarthome:id/timer_tv')

    # ************************跳过引导************************** #
    # 跳过
    skip_guide = ('id', 'com.eufylife.smarthome:id/tv_skip')

    # 结束引导
    end_guide = ('id', 'com.eufylife.smarthome:id/done_btn')
