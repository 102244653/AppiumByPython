class RoboticSchedulesActivity(object):
    # 返回按钮
    back_robotic = ('name', 'common icon back')

    # 小黄条文本
    yellow_tip = ('xpath', '//XCUIElementTypeOther[@name="Schedules"]/XCUIElementTypeStaticText[2]')

    # 小黄条关闭
    close_yelloe_tip = ('name', 'common icon dialog close')

    # 日期
    week = ('xpath', '//XCUIElementTypeStaticText[@name="Repeat"]/following-sibling::XCUIElementTypeOther/XCUIElementTypeButton')

    # ******************************t2123************************************** #
    # t2123定时任务开关
    t2123_btns = ('xpath', '//XCUIElementTypeCell/XCUIElementTypeSwitch')

    # t2123定时任务修改记录
    t2123_schedule_history = ('name', 'common icon update history')

    # t2123定时任务历史记录模块
    t2123_schedule_record_item = ('xpath', '//XCUIElementTypeStaticText[@name="Modified Schedules"]/../XCUIElementTypeCell[*]')

    # t2123修改记录全部删除
    t2123_delete_all_record = ('name', 'Delete All')

    # t2123 返回定时任务主页
    t2123_back_schedule = ('name', 'common icon back')

    # ******************************t2250************************************** #
    # t2250定时任务开关
    t2250_btns = ('xpath', '//XCUIElementTypeCell/XCUIElementTypeSwitch')

    # ******************************t2190************************************** #
    # 新增定时任务按钮
    t2190_add_schedule = ('xpath', '//XCUIElementTypeButton[@name="common icon add"]')
    t2190_null_add_schedule = ('name', 'Add Schedule')

    # 定时任务模块
    t2190_schedule_item = ('xpath', '//XCUIElementTypeOther[@name="Schedules"]/following-sibling::XCUIElementTypeCell/XCUIElementTypeOther[1]')

    # 删除定时任务
    t2190_delete_schedule = ('name', 'Delete')

    # 开关按钮
    t2190_schedule_btn = ('xpath', '//XCUIElementTypeOther[@name="Schedules"]/following-sibling::XCUIElementTypeCell/XCUIElementTypeOther/XCUIElementTypeSwitch')

    # 保存定时任务
    save_schedule = ('name', 'Save')
