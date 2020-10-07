class BulbsHomeActivity(object):
    # 返回
    back_home = ('id', 'com.eufylife.smarthome:id/common_header_start_icon')

    # 离线等弹窗
    offline_window = ('id', 'com.eufylife.smarthome:id/dialog_describe_tv')

    # 灯泡设置
    bulb_setting = ('id', 'com.eufylife.smarthome:id/common_header_end_icon')

    # 设备名称
    device_name = ('id', 'com.eufylife.smarthome:id/title_tv')

    # 分组名称
    group_name = ('id', 'com.eufylife.smarthome:id/group_name')

    # 灯泡背景
    bulb_mask_view = ('id', 'com.eufylife.smarthome:id/bulb_mask_view')

    # 灯泡亮度调节
    bulb_progress_bar = ('id', 'com.eufylife.smarthome:id/bulb_progress_bar')

    # 灯泡亮度值
    bulb_light_num = ('xpath', '//*[@resource-id="com.eufylife.smarthome:id/bulb_light_progress"]/android.widget.TextView')

    # 模式
    effect = ('id', 'com.eufylife.smarthome:id/mode_effect_btn')

    # 定时任务
    color_schedules = ('id', 'com.eufylife.smarthome:id/mode_schedule_btn')
    white_schedules = ('id', 'com.eufylife.smarthome:id/schedules_tv')

    # 收藏
    favorites_page = ('id', 'com.eufylife.smarthome:id/mode_favorites_btn')
    white_favorites_page = ('id', 'com.eufylife.smarthome:id/home_tv')

    add_white_favorites = ('id', 'com.eufylife.smarthome:id/bulb_add_favorite')

    # 白色灯效
    bulb_color = ('xpath', '//*[@resource-id="com.eufylife.smarthome:id/bulb_mode_icon"]/android.widget.TextView[1]')

    # ************************跳过引导************************** #
    # 跳过
    skip_guide = ('id', 'com.eufylife.smarthome:id/tv_skip')

    # 结束引导
    end_guide = ('id', 'com.eufylife.smarthome:id/done_btn')

