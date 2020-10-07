class SignPage(object):
    # 提交注册按钮
    signup_btn = ('xpath', '//XCUIElementTypeButton[@name="Sign Up"]')

    # 密码输入框
    sign_password_input = ('name', 'Password')

    # 密码可见
    pw_display = ('name', 'signup icon closeeyes')

    # 账号输入框
    sign_email_input = ('name', 'Email')

    # 选择的地区的按钮
    sign_country = ('name', 'Location')

    # 查找国家文本框
    sign_country_input = ('name', 'Search')

    # 国家确认弹窗
    country_window = ('xpath', '//*[starts-with(@name,"In order to comply with the corresponding")]')

    # 邮箱注册失败弹窗
    sign_email_error_tip = ('name', '//*[starts-with(@name,"This email address is already registered")]')

    # 密码错误失败提示
    sign_pw_error_tip = ('name', 'Your password must be 8-20 characters long.')

    # 关闭注册失败弹窗
    close_sign_tip = ('name', 'signup icon close')
    

class LoginPage(SignPage):
    # 退出登陆界面
    login_back = ('name', 'common icon back')

    # 当前选择的地区
    login_country = ('xpath', '//XCUIElementTypeNavigationBar[@name="AKSignInView"]/XCUIElementTypeButton[2]')

    login_country_input = ('name', 'Search')

    # 邮箱登陆账号
    login_email_input = ('xpath', '//XCUIElementTypeStaticText[@name="Log In"]/../../XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeTextField')

    # 手机账号
    login_phone_input = ('xpath', '//XCUIElementTypeStaticText[@name="Log In"]/../../XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeTextField')

    # 邮箱登录密码
    email_pw_input = ('name', 'Password')

    # 手机账号密码
    phone_pw_input = ('name', 'Password')

    # 密码明文显示
    pw_visible_btn = ('name', 'signup icon closeeyes')

    # 登陆提交按钮
    login_btn = ('xpath', '//XCUIElementTypeButton[@name="Log In"]')

    # 登陆失败的弹窗
    login_error_tip = ('name', 'Please enter a valid email address (Example: name@domain.com).')

    # 关闭弹窗
    close_login_tip = ('name', 'signup icon close')


class StartActivity(LoginPage):
    """
    注册登录界面
    """
    # 进入注册
    into_signup_btn = ('name', 'Sign Up')

    # 进入登陆
    into_login_btn = ('name', 'Log In')
