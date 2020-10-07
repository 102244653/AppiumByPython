class BulbsScheduleActivity(object):
    # 返回按钮
    back_bulbs = ('id', 'com.eufylife.smarthome:id/common_header_start_icon')

    # 添加计划
    add_schedule = ('id', 'com.eufylife.smarthome:id/common_header_end_icon')
    null_add_schedule = ('xpath', '//*[@text="Add Schedule"]')

    # 离家模式开关
    away_btn = ('id', 'com.eufylife.smarthome:id/away_mode_sv')

    # 定时任务开关
    schedule_btn = ('id', 'com.eufylife.smarthome:id/bulb_schedule_sv')

    # 定时任务模块
    schedule_item = ('id', 'com.eufylife.smarthome:id/schedules_recycler_view')

    # 删除按钮
    delete_schedule_btn = ('id', 'com.eufylife.smarthome:id/schedules_delete_tv')

    # 小黄条关闭
    close_yelloe_tip = ('id', 'com.eufylife.smarthome:id/item_close')

    # ***********************************新增定时任务****************************************#
    # 保存
    save_btn = ('id', 'com.eufylife.smarthome:id/common_header_end_tv')

    # 灯效编辑
    edit_effect = ('id', 'com.eufylife.smarthome:id/edit_schedules_edit')

    # 打开灯泡
    on_btn = ('id', 'com.eufylife.smarthome:id/dialog_layout_on')

    # 下一步
    next = ('id', 'com.eufylife.smarthome:id/dialog_end_next')

    # 保存灯效
    done = ('id', 'com.eufylife.smarthome:id/dialog_end_done')

    # 日期
    week = ('xpath', '//*[@text="Repeat"]/following-sibling::android.widget.FrameLayout/android.widget.LinearLayout/android.widget.CheckBox')