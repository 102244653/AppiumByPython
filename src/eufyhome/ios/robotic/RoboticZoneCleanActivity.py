class RoboticZoneCleanActivity(object):
    # 关闭提示弹窗
    close_tip = ('name', 'mop icon close')

    # 返回
    back_robovac = ('name', 'common icon back white')

    # 新增区域
    add_zone = ('name', 'zoned icon add')

    # clean按钮
    clean_btn = ('name', 'home icon clean')

    # 清扫次数
    clean_qty = ('xpath', '//XCUIElementTypeButton[contains(@name,"zoned icon")]')

