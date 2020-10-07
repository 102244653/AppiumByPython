class RoboticSchedulesActivity(object):
    # 返回按钮
    back_robotic = ('id', 'com.eufylife.smarthome:id/common_header_start_icon')

    # 小黄条文本
    yellow_tip = ('id', 'com.eufylife.smarthome:id/item_text')

    # 小黄条关闭
    close_yelloe_tip = ('id', 'com.eufylife.smarthome:id/item_close')

    # 日期
    week = ('xpath', '//*[@resource-id="com.eufylife.smarthome:id/edit_schedule_repeat_title"]/following-sibling::android.widget.FrameLayout/android.widget.LinearLayout/android.widget.CheckBox')

    # ******************************t2123************************************** #
    # t2123定时任务开关
    t2123_btns = ('id', 'com.eufylife.smarthome:id/schedules_sv')

    # 定时任务模块
    t2123_schedule_item = ('id', 'com.eufylife.smarthome:id/schedules_week')

    # t2123查看定时任务修改记录
    t2123_schedule_history = ('id', 'com.eufylife.smarthome:id/common_header_end_icon')

    # t2123定时任务历史记录模块
    t2123_schedule_record_item = ('xpath', '//*[@resource-id="com.eufylife.smarthome:id/logs_recycler_view"]/android.widget.LinearLayout[*]')

    # t2123修改记录全部删除
    t2123_delete_all_record = ('id', 'com.eufylife.smarthome:id/common_header_end_tv')

    # t2123 记录返回定时任务主页
    t2123_back_schedule = ('id', 'com.eufylife.smarthome:id/prompt_empty_back')

    # ******************************t2250************************************** #
    # t2250定时任务开关
    t2250_btns = ('id', 'com.eufylife.smarthome:id/schedules_sv')

    # ******************************t2190************************************** #
    # 新增定时任务按钮
    t2190_add_schedule = ('id', 'com.eufylife.smarthome:id/common_header_end_icon')
    t2190_null_add_schedule = ('id', 'com.eufylife.smarthome:id/schedule_add_btn')

    # 定时任务模块
    t2190_schedule_item = ('id', 'com.eufylife.smarthome:id/item_swipemenu_layout')

    # 删除定时任务
    t2190_delete_schedule = ('id', 'com.eufylife.smarthome:id/schedules_delete_tv')

    # 开关按钮
    t2190_schedule_btn = ('id', 'com.eufylife.smarthome:id/bulb_schedule_sv')

    # 保存定时任务
    save_schedule = ('id', 'com.eufylife.smarthome:id/common_header_end_tv')
