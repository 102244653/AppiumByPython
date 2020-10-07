```
app_test
    |-src
        |-appium_log
            # 用于存放appium服务端日志 
        |-case
            __init__.py  # 不能删除
            conftest.py  # 共享的setUp/tearDown，自定义html报告
            pytest.ini  # pytest配置文件
            test_checklist.py  # 测试类，用于写测试用例
        |-config
            __init__.py
            config.py   # 定义全局变量
        |-html_report  # 用于存放失败截图和html报告
        |-page  # 遵循page object模式
            |-android  # 定义页面元素，文件名和ios一一对应
                __init__.py
                GDPRActivity.py
                SwitchLanguageActivity.py
                WelcomeActivity.py
            |-ios  # 定义页面元素，文件名和android一一对应
                __init__.py
                GDPRActivity.py
                SwitchLanguageActivity.py
                WelcomeActivity.py
            |-method  # 定义页面操作，文件名和页面元素的文件一一对应
                __init__.py
                GDPR_page.py
                SwitchLanguage_page.py
                Welcome_page.py
            __init__.py
        |-util  # 通用的方法
            __init__.py
            base_method.py  # 对appium API二次封装
            util.py  # 工具类，其他方法封装
        __init__.py
        README.md
        requirements.txt
```


安装requirements.txt依赖：pip install -r requirements.txt

执行命令：
由于conftest.py中有文件的相对路径，为了既能在IDE中执行和在命令行中执行，使用命令执行前需要先进到case路径下
pytest test_checklist.py -m menu --html=../html_report/report.html --cmd_sn=75e281cc


-m 筛选用例执行，-m menu表明筛选出带装饰器@pytest.mark.menu的用例执行, 不写-m参数表明执行所有用例
--html 指定生成html报告的路径
--cmd_sn 指定测试手机sn号（或UDID）