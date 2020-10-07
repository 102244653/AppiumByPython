class BaseActivity(object):
    # 加载动画
    progress = ('id', 'com.eufylife.smarthome:id/loadProgress')

    # 安卓弹窗接受按钮
    right_btn = ('id', 'com.eufylife.smarthome:id/dialog_btn_right')
    ok = ('xpath', '//*[@text="OK"]')
    yes = ('xpath', '//*[@text="Yes"]')
    no = ('xpath', '//*[@text="No"]')
    ignore = ('xpath', '//*[@text="Ignore"]')

    # 安卓弹窗拒绝按钮
    common_cancel = ('id', 'com.eufylife.smarthome:id/dialog_btn_left')

    # 离线弹窗
    offline_window = ('xpath', '//*[@text="Device is offline"]')

    # 重试按钮
    try_again = ('xpath', '//android.widget.Button[@text="Try Again"]')

    # 固件升级弹窗
    update_window = ('xpath', '//*[@text="Firmware Update"]')

    # 时间滚轮
    # 图片识别
    t2123_ocr_img = ('xpath', '//android.widget.ScrollView/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]')
    t2250_ocr_img = ('xpath', '//*[@resource-id="com.eufylife.smarthome:id/edit_schedule_date_wheel_view"]')
    t2190_ocr_img = ('xpath', '//*[@resource-id="com.eufylife.smarthome:id/edit_schedule_date_wheel_view"]')
    t1013_ocr_img = ('xpath', '//*[@resource-id="com.eufylife.smarthome:id/edit_schedule_date_wheel_view"]')
    t1100_ocr_img = ('xpath', '//*[@resource-id="com.eufylife.smarthome:id/edit_schedule_date_wheel_view"]')
    t1211_ocr_img = ('xpath', '//*[@resource-id="com.eufylife.smarthome:id/edit_schedule_date_wheel_view"]')

    # 小时
    hour = ('id', 'com.eufylife.smarthome:id/hour_lv')

    # 分钟
    min = ('id', 'com.eufylife.smarthome:id/min_lv')

    # Timer
    # 时
    timer_hour = ('id', 'com.eufylife.smarthome:id/hours_loop_view')

    # 分
    timer_min = ('id', 'com.eufylife.smarthome:id/min_loop_view')

    # timer图片识别
    timer_ocr_img = ('id', 'com.eufylife.smarthome:id/loop_view_bg')

    # -----------------------------离家模式-------------------------------- #

    # start_hour
    # 时
    start_hour = ('xpath', '//*[@resource-id="com.eufylife.smarthome:id/away_mode_start"]/android.widget.RelativeLayout[1]/android.view.View[1]')

    # 分
    start_min = ('xpath', '//*[@resource-id="com.eufylife.smarthome:id/away_mode_start"]/android.widget.RelativeLayout[1]/android.view.View[2]')

    # start图片识别
    start_ocr_img = ('id', 'com.eufylife.smarthome:id/away_mode_start')

    # end_hour
    # 时
    end_hour = ('xpath', '//*[@resource-id="com.eufylife.smarthome:id/away_mode_end"]/android.widget.RelativeLayout[1]/android.view.View[1]')

    # 分
    end_min = ('xpath', '//*[@resource-id="com.eufylife.smarthome:id/away_mode_end"]/android.widget.RelativeLayout[1]/android.view.View[2]')

    # start图片识别
    end_ocr_img = ('id', 'com.eufylife.smarthome:id/away_mode_end')
