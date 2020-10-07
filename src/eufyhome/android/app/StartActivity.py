class SignPage(object):
    # 提交注册按钮
    signup_btn = ('id', 'com.eufylife.smarthome:id/submit_btn')

    # 密码输入框
    sign_password_input = ('id', 'com.eufylife.smarthome:id/pwd_et')

    # 账号输入框
    sign_email_input = ('id', 'com.eufylife.smarthome:id/email_et')

    # 选择的地区
    sign_country = ('id', 'com.eufylife.smarthome:id/account_region')

    # 查找国家文本框
    sign_country_input = ('id', 'android:id/search_src_text')

    # 国家确认弹窗
    country_window = ('id', 'com.eufylife.smarthome:id/dialog_describe_tv')

    # 邮箱错误失败提示
    sign_email_error_tip = ('id', 'com.eufylife.smarthome:id/error_email_describe_tv')

    # 密码错误失败提示
    sign_pw_error_tip = ('id', 'com.eufylife.smarthome:id/describe_tv')

    # 关闭注册失败弹窗
    close_sign_tip = ('id', 'com.eufylife.smarthome:id/email_close_view')


class LoginPage(SignPage):
    # 退出登陆界面
    login_back = ('id', 'com.eufylife.smarthome:id/common_header_start_icon')

    # 当前选择的地区
    login_country = ('id', 'com.eufylife.smarthome:id/common_header_end_tv')

    # 国家输入框
    login_country_input = ('id', 'android:id/search_src_text')

    # 邮箱登陆账号
    login_email_input = ('id', 'com.eufylife.smarthome:id/email_et')

    # 手机账号
    login_phone_input = ('id', 'com.eufylife.smarthome:id/phone_et')

    # 邮箱登录密码
    email_pw_input = ('id', 'com.eufylife.smarthome:id/pwd_et')

    # 手机账号密码
    phone_pw_input = ('id', 'com.eufylife.smarthome:id/pwd_et')

    # 密码明文显示
    pw_visible_btn = ('id', 'com.eufylife.smarthome:id/visible_view')

    # 登陆提交按钮
    login_btn = ('id', 'com.eufylife.smarthome:id/submit_btn')

    # 登陆失败的提示
    login_error_tip = ('id', 'com.eufylife.smarthome:id/error_email_describe_tv')

    # 关闭弹窗
    close_login_tip = ('id', 'com.eufylife.smarthome:id/email_close_view')


class StartActivity(LoginPage):
    """
    注册登录界面
    """
    # 进入注册
    into_signup_btn = ('id', 'com.eufylife.smarthome:id/welcome_sign_up_btn')

    # 进入登陆
    into_login_btn = ('id', 'com.eufylife.smarthome:id/welcome_log_in_btn')

