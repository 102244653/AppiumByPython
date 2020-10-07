class BaseActivity(object):
    # 加载动画
    progress = ('name', 'In progress')

    # ios弹窗接受按钮
    ok = ('name', 'OK')
    yes = ('name', 'Yes')
    no = ('name', 'No')
    ignore = ('name', 'Ignore')

    # ios弹窗拒绝按钮
    common_cancel = ('name', 'Cancel')

    # 离线弹窗
    offline_window = ('name', 'Device is offline')

    # 重试按钮
    try_again = ('name', 'Try Again')

    # 升级弹窗
    update_window = ('name', 'Firmware Update')

    # 时间滚轮
    # 图片识别
    t2123_ocr_img = ('xpath', '//*[@name="At"]/following-sibling::XCUIElementTypeDatePicker')
    t2250_ocr_img = ('xpath', '//*[@name="At"]/following-sibling::XCUIElementTypeDatePicker')
    t2190_ocr_img = ('xpath', '//*[@name="At"]/following-sibling::XCUIElementTypeDatePicker')
    t1013_ocr_img = ('xpath', '//*[@name="At"]/following-sibling::XCUIElementTypeDatePicker')
    t1100_ocr_img = ('xpath', '//*[@name="At"]/following-sibling::XCUIElementTypeDatePicker')
    t1211_ocr_img = ('xpath', '//*[@name="At"]/following-sibling::XCUIElementTypeDatePicker')

    # 小时
    hour = ('xpath', '//*[@name="At"]/following-sibling::XCUIElementTypeDatePicker[1]/XCUIElementTypeOther[1]/XCUIElementTypePickerWheel[1]')

    # 分钟
    min = ('xpath', '//*[@name="At"]/following-sibling::XCUIElementTypeDatePicker[1]/XCUIElementTypeOther[1]/XCUIElementTypePickerWheel[2]')

    # Timer
    # 时
    timer_hour = ('xpath', '//*[@name="Timer"]/../following-sibling::XCUIElementTypeDatePicker[1]/XCUIElementTypeOther[1]/XCUIElementTypePickerWheel[1]')

    # 分
    timer_min = ('xpath', '//*[@name="Timer"]/../following-sibling::XCUIElementTypeDatePicker[1]/XCUIElementTypeOther[1]/XCUIElementTypePickerWheel[2]')

    # timer图片识别
    timer_ocr_img = ('xpath', '//*[@name="Timer"]/../following-sibling::XCUIElementTypeDatePicker')

    # -----------------------------离家模式-------------------------------- #

    # start_hour
    # 时
    start_hour = ('xpath', '//*[@name="Start"]/following-sibling::XCUIElementTypeDatePicker[1]/XCUIElementTypeOther[1]/XCUIElementTypePickerWheel[1]')

    # 分
    start_min = ('xpath', '//*[@name="Start"]/following-sibling::XCUIElementTypeDatePicker[1]/XCUIElementTypeOther[1]/XCUIElementTypePickerWheel[2]')

    # start图片识别
    start_ocr_img = ('xpath', '//*[@name="Start"]/following-sibling::XCUIElementTypeDatePicker')

    # end_hour
    # 时
    end_hour = ('xpath', '//*[@name="End"]/following-sibling::XCUIElementTypeDatePicker[1]/XCUIElementTypeOther[1]/XCUIElementTypePickerWheel[1]')

    # 分
    end_min = ('xpath', '//*[@name="End"]/following-sibling::XCUIElementTypeDatePicker[1]/XCUIElementTypeOther[1]/XCUIElementTypePickerWheel[2]')

    # start图片识别
    end_ocr_img = ('xpath', '//*[@name="End"]/following-sibling::XCUIElementTypeDatePicker')
