class RoboticVoiceActivity(object):
    # 返回
    back_setting = ('name', 'common icon back')

    # 音量条
    voice_btn = ('xpath', '//XCUIElementTypeStaticText[@name="Select Voice"]/../XCUIElementTypeOther')

    # 音量显示
    voice_value = ('xpath', '//XCUIElementTypeStaticText[@name="Select Voice"]/../XCUIElementTypeStaticText[1]')

