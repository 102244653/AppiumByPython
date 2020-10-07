class BulbsScheduleActivity(object):
    # 返回按钮
    back_bulbs = ('name', 'common icon back')

    # 添加计划
    add_schedule = ('name', 'common icon add')
    null_add_schedule = ('name', 'Add Schedule')

    # 离家模式开关
    away_btn = ('xpath', '//XCUIElementTypeImage[contains(@name,"img_schedual_away")]/../XCUIElementTypeSwitch[1]')

    # 定时任务开关
    schedule_btn = ('xpath', '(//XCUIElementTypeOther[@name="Schedules"])[2]/following-sibling::XCUIElementTypeCell/XCUIElementTypeOther/XCUIElementTypeSwitch')

    # 定时任务模块
    schedule_item = ('xpath', '(//XCUIElementTypeOther[@name="Schedules"])[2]/following-sibling::XCUIElementTypeCell')

    # 删除按钮
    delete_schedule_btn = ('name', 'Delete')

    # 小黄条关闭
    close_yelloe_tip = ('name', 'common icon dialog close')

    # ***********************************新增定时任务****************************************#
    # 保存
    save_btn = ('name', 'Save')

    # 灯效编辑
    edit_effect = ('xpath', '//XCUIElementTypeStaticText[@name="Device Actions"]/following-sibling::XCUIElementTypeOther[1]/XCUIElementTypeButton[1]')

    # 打开灯泡
    on_btn = ('xpath', '//XCUIElementTypeStaticText[@name="ON"]/../XCUIElementTypeButton[1]')

    # 下一步
    next = ('name', 'Next')

    # 保存灯效
    done = ('name', 'Done')

    # 日期
    week = ('xpath', '//XCUIElementTypeStaticText[@name="Repeat"]/following-sibling::XCUIElementTypeOther/XCUIElementTypeButton')