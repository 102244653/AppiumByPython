class BulbsGroupHomeActivity(object):
    # 返回
    back_home = ('id', 'com.eufylife.smarthome:id/common_header_start_icon')

    # 分组名
    home_group_name = ('id', 'com.eufylife.smarthome:id/group_title_tv')

    # 模式
    group_effect = ('id', 'com.eufylife.smarthome:id/group_mode_effect_btn')

    # 分组设置
    group_setting = ('id', 'com.eufylife.smarthome:id/group_mode_setting_btn')

    # 灯组是否开启
    group_is_on = ('xpath', '//*[@resource-id="com.eufylife.smarthome:id/bulb_mode_icon"]/android.widget.TextView')

    # 扽组界面灯泡按钮
    group_bulbs_bar = ('id', 'com.eufylife.smarthome:id/bulb_progress_bar')

    # 灯组的状态
    group_home_status = ('id', 'com.eufylife.smarthome:id/group_status_tv')

    # *******************************分组设置界面********************************** #

    #  返回
    back_group = ('id', 'com.eufylife.smarthome:id/common_header_start_icon')

    # 分组名
    setting_group_name = ('id', 'com.eufylife.smarthome:id/group_name')

    # 组名编辑
    edit_group_name = ('id', 'com.eufylife.smarthome:id/device_name_edt')

    # 保存
    save_group_name = ('id', 'com.eufylife.smarthome:id/submit_btn')

    # 删除分组
    delete_group = ('xpath', '//*[@text="Delete this Group"]')

    # 设置保存
    save = ('id', 'com.eufylife.smarthome:id/common_header_end_tv')

    # *******************************分组模式界面********************************** #
    # white模式
    white_btn = ('xpath', '//*[@resource-id="com.eufylife.smarthome:id/select_layout"]/android.widget.RelativeLayout[1]/android.widget.CheckBox[1]')

    # flow模式
    flow_btn = ('xpath', '//*[@resource-id="com.eufylife.smarthome:id/select_layout"]/android.widget.RelativeLayout[3]/android.widget.CheckBox[1]')

    # color模式
    color_btn = ('xpath', '//*[@resource-id="com.eufylife.smarthome:id/select_layout"]/android.widget.RelativeLayout[2]/android.widget.CheckBox[1]')

    # 关闭按钮
    close_effect = ('id', 'com.eufylife.smarthome:id/bulb_close_view')

    # 灯效
    effect_text = ('id', 'com.eufylife.smarthome:id/group_mode_title_tv')