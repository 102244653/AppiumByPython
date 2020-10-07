class BulbsDefaultLightActivity(object):
    # 返回
    back_setting = ('id', 'com.eufylife.smarthome:id/common_header_start_icon')

    # 最后一次灯效
    last_title = ('id', 'com.eufylife.smarthome:id/last_state_tv')

    # 最后一次灯效选择标识
    last_status_icon = ('xpath', '//*[@resource-id="com.eufylife.smarthome:id/last_state_checked"]')

    # 自定义灯效
    custom_title = ('id', 'com.eufylife.smarthome:id/custom_state_tv')

    # 自定义灯效标识
    custom_status_icon = ('xpath', '//*[@resource-id="com.eufylife.smarthome:id/custom_state_checked"]')

    # 自定义灯效确认
    custom_done = ('id', 'com.eufylife.smarthome:id/dialog_end_done')

    # white
    white_btn = ('id', 'com.eufylife.smarthome:id/dialog_white_cb')

    # color
    color_btn = ('id', 'com.eufylife.smarthome:id/dialog_color_cb')

    # 灯泡亮度调节图片
    white_bulbs_pic = ('id', 'com.eufylife.smarthome:id/bulb_progress_bar')
