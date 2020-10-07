class BulbsEffectActivity(object):
    # 灯效（页面标题）
    bulb_title = ('id', 'com.eufylife.smarthome:id/title_tv')

    # 灯泡
    bulbs_btn = ('id', 'com.eufylife.smarthome:id/bulb_progress_bar')

    # white模式
    bulbs_white = ('xpath', '//*[@resource-id="com.eufylife.smarthome:id/select_layout"]/android.widget.RelativeLayout[1]/android.widget.CheckBox')

    bulbs_color = ('xpath', '//*[@resource-id="com.eufylife.smarthome:id/select_layout"]/android.widget.RelativeLayout[2]/android.widget.CheckBox')

    # recommended
    bulbs_recommended = ('xpath', '//*[@resource-id="com.eufylife.smarthome:id/select_layout"]/android.widget.RelativeLayout[3]/android.widget.CheckBox')
    bulbs_flow = ('xpath', '//*[@resource-id="com.eufylife.smarthome:id/select_layout"]/android.widget.RelativeLayout[4]/android.widget.CheckBox')

    bulbs_music = ('xpath', '//*[@resource-id="com.eufylife.smarthome:id/select_layout"]/android.widget.RelativeLayout[5]/android.widget.CheckBox')

    # # Relax
    # Relax = ('xpath', '//android.widget.TextView[@text="Relax"]')
    #
    # # Read
    # Read = ('xpath', '//android.widget.TextView[@text="Read"]')
    #
    # # Focus
    # Focus = ('xpath', '//android.widget.TextView[@text="Focus"]')
    #
    # # Night Light
    # Night_Light = ('xpath', '//android.widget.TextView[@text="Night Light"]')

    # 关闭界面
    close_effect = ('id', 'com.eufylife.smarthome:id/bulb_close_view')

    # 灯效区域
    color_area = ('id', 'com.eufylife.smarthome:id/bulb_bottom_layout')

    # 添加收藏
    add_favorite = ('id', 'com.eufylife.smarthome:id/bulb_add_favorite')

    # 收藏名称
    favorite_name = ('id', 'com.eufylife.smarthome:id/favorite_name_et')

    # 收藏亮度值
    favorite_lightness = ('id', 'com.eufylife.smarthome:id/lum_tv')

    # 保存按钮
    save_favorite = ('id', 'com.eufylife.smarthome:id/save_btn')
