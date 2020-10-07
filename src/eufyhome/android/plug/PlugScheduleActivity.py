class PlugScheduleActivity(object):
    # 返回
    back_plug = ('id', 'com.eufylife.smarthome:id/common_header_start_icon')

    # 添加定时任务
    add_schedule = ('id', 'com.eufylife.smarthome:id/common_header_end_icon')
    null_add_schedule = ('xpath', '//*[@text="Add Schedule"]')

    # 离家模式开关
    away_mode_btn = ('id', 'com.eufylife.smarthome:id/away_mode_sv')

    # 普通定时任务开关
    schedule_btn = ('id', 'com.eufylife.smarthome:id/bulb_schedule_sv')

    # 离家模式入口
    into_away_mode = ('xpath', '//*[@resource-id="com.eufylife.smarthome:id/away_mode_icon"]')

    # 定时任务模块
    schedule_item = ('id', 'com.eufylife.smarthome:id/item_swipemenu_layout')

    # 定时任务左滑删除按钮
    schedule_delete = ('id', 'com.eufylife.smarthome:id/schedules_delete_tv')

    # 小黄条关闭
    close_yelloe_tip = ('id', 'com.eufylife.smarthome:id/item_close')

    # ************************添加定时任务界面*************************** #
    # 返回
    back_schedule = ('id', 'com.eufylife.smarthome:id/common_header_start_icon')

    # 保存
    save_schedule = ('id', 'com.eufylife.smarthome:id/common_header_end_tv')

    # 编辑开关状态
    edit_btn = ('id', 'com.eufylife.smarthome:id/item_layout')

    # 开关状态
    on_btn = ('id', 'com.eufylife.smarthome:id/dialog_layout_on')

    # 完成编辑
    done = ('id', 'com.eufylife.smarthome:id/dialog_end_next')

    # 日期
    week = ('xpath', '//*[@resource-id="com.eufylife.smarthome:id/edit_schedule_repeat_title"]/following-sibling::android.widget.FrameLayout/android.widget.LinearLayout/android.widget.CheckBox')

    # ************************离家模式编辑界面*************************** #
    # 开关
    away_btn = ('id', 'com.eufylife.smarthome:id/away_mode_sv')