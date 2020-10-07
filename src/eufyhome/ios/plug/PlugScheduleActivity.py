class PlugScheduleActivity(object):
    # 返回
    back_plug = ('name', 'common icon back')

    # 添加定时任务
    add_schedule = ('name', 'common icon add')
    null_add_schedule = ('name', 'Add Schedule')

    # 离家模式开关
    away_mode_btn = ('xpath', '//XCUIElementTypeImage[contains(@name,"img_schedual_away")]/../XCUIElementTypeSwitch')

    # 离家模式入口
    into_away_mode = ('xpath', '//XCUIElementTypeStaticText[@name="Away Mode"]/../following-sibling::XCUIElementTypeCell[1]')

    # 普通定时任务开关
    schedule_btn = ('xpath', '(//XCUIElementTypeOther[@name="Schedules"])[2]/following-sibling::XCUIElementTypeCell/XCUIElementTypeOther/XCUIElementTypeSwitch')

    # 定时任务模块
    schedule_item = ('xpath', '(//XCUIElementTypeOther[@name="Schedules"])[2]/following-sibling::XCUIElementTypeCell/XCUIElementTypeOther')

    # 定时任务左滑删除按钮
    schedule_delete = ('name', 'Delete')

    # 小黄条关闭
    close_yelloe_tip = ('name', 'common icon dialog close')

    # ************************添加定时任务界面*************************** #
    # 返回
    back_schedule = ('name', 'common icon back')

    # 保存
    save_schedule = ('name', 'Save')

    # 编辑开关状态
    edit_btn = ('xpath', '//XCUIElementTypeStaticText[@name="Device Actions"]/following-sibling::XCUIElementTypeOther[1]/XCUIElementTypeButton[1]')

    # 开关状态
    on_btn = ('xpath', '//XCUIElementTypeStaticText[@name="ON"]/../XCUIElementTypeButton[1]')

    # 完成编辑
    done = ('name', 'Done')

    # 日期
    week = ('xpath', '//XCUIElementTypeStaticText[@name="Repeat"]/following-sibling::XCUIElementTypeOther/XCUIElementTypeButton')

    # ************************离家模式编辑界面*************************** #
    # 开关
    away_btn = ('xpath', '//*[@name="Start"]/../XCUIElementTypeSwitch[1]')