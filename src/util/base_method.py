import time
import os
import cv2
import duration as Duration
from PIL import Image
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import base_path
from src.config.config import GlobalVar
from src.util import util

'''
对appium的接口进行二次封装
'''


class BaseMethod:
    def __init__(self, driver):
        self.driver = driver
        self.platform = GlobalVar.get_platform()

    def open_app(self):
        """
        启动初始化app
        :return:
        """
        self.driver.launch_app()

    def kill_app(self):
        """
        关闭初始化中的app
        :return:
        """
        self.driver.close_app()

    def background_app(self, timeout=5):
        """
        置于后台
        :return:
        """
        self.driver.background_app(timeout)

    def activate_app(self, pkg_name):
        '''
        打开指定应用
        :param pkg_name:
        :return:
        '''
        self.driver.activate_app(pkg_name)

    def terminate_app(self, pkg_name):
        """
        关闭指定应用
        :param pkg_name:
        :return:
        """
        self.driver.terminate_app(pkg_name)

    def hide_keyboard(self):
        '''
        隐藏键盘
        :return:
        '''
        try:
            self.driver.hide_keyboard()
        except Exception as e:
            print(e)
            pass

    def restart_app(self):
        """
        清除数据，重启app
        :return:
        """
        self.driver.reset()

    def press_back(self):
        '''
        返回
        :return:
        '''
        if self.platform == GlobalVar.IOS:
            self.driver.background_app(Duration.to_seconds(-1))
        else:
            self.driver.press_keycode(4)

    def tap_element(self, locator):
        '''
        点击控件
        :param locator:
        :return:
        '''
        if isinstance(locator, tuple):
            el = self.get_element(locator)
        else:
            el = locator
        attr = self.get_element_attributes(el)
        self.tap(attr['center_x'], attr['center_y'])

    def click_element(self, locator):
        if isinstance(locator, tuple):
            el = self.get_element(locator)
        else:
            el = locator
        el.click()

    def click_child_element(self, par_loc, child_loc, index):
        '''
        点击指定子控件
        :param par_loc:
        :param child_loc:
        :param index:
        :return:
        '''
        btn = self.get_child_element(par_loc, child_loc, index)
        btn.click()

    def get_text_locator(self, text, class_name=None):
        """
        返回locator
        :param text:
        :param class_name:
        :return:
        """
        if self.platform == 'ios':
            if class_name is None:
                loc = ('name', text)
            else:
                loc = ('xpath', '//{}[@name="{}"]'.format(class_name, text))
        else:
            if class_name is None:
                loc = ('android', 'text("{}")'.format(text))
            else:
                loc = ('android', 'className("{}").text("{}")'.format(class_name, text))
        return loc

    def get_element(self, locator, index=0):
        """
        获取控件
        :param locator:
        :param index:
        :return:
        """
        method = locator[0]
        values = locator[1]
        if index == 0:
            ele = self.get_element_by_type(method, values)
        else:
            ele = self.get_elements_by_type(method, values)[index]
        return ele

    def get_elements(self, locator):
        """
        获取满足条件的所有控件
        :param locator:
        :return:
        """
        method = locator[0]
        values = locator[1]
        if type(values) is str:
            return self.get_elements_by_type(method, values)
        elif type(values) is list:
            for value in values:
                try:
                    return self.get_elements_by_type(method, value)
                except NoSuchElementException as e:
                    print(e)
                    pass
            raise NoSuchElementException

    def get_text(self, locator):
        '''
        获取字符串
        :param locator:
        :return:
        '''
        if isinstance(locator, tuple):
            el = self.get_element(locator)
        else:
            el = locator
        if self.platform == GlobalVar.IOS:
            return el.get_attribute('name')
        else:
            return el.text

    def is_exist(self, locator):
        '''
        控件是否存在
        :param locator:
        :return:
        '''

        try:
           _ele = self.get_element(locator)
        except Exception as e:
            print(e)
            return False
        else:
            return True

    def wait(self, ec, timeout=10):
        '''
        等待条件满足
        :param ec:
        :param timeout:
        :return:
        '''
        try:
            if WebDriverWait(self.driver, timeout).until(ec):
                flag = True
        except Exception as e:
            print(e)
            flag = False
        return flag

    def wait_exist(self, locator, timeout=8):
        '''
        等待控件出现
        :param locator:
        :param timeout:
        :return:
        '''
        try:
            ele = WebDriverWait(self.driver, timeout, 1).until(EC.visibility_of_element_located(locator))
        except Exception as e:
            print(e)
            return False
        if ele:
            return True
        else:
            return False

    def wait_not_exist(self, locator, timeout=10):
        '''
        等待存在的控件消失
        :param locator:
        :param timeout:
        :return:
        '''
        try:
            if WebDriverWait(self.driver, timeout, 0.5).until(EC.invisibility_of_element_located(locator)):
                flag = True
        except Exception as e:
            print(e)
            flag = False
        return flag

    def wait_elements(self, timeout=10, *locator):
        '''
        等待多个控件之中的一个出现
        :param timeout:
        :param locator:
        :return:
        '''
        end = time.time() + timeout
        while time.time() < end:
            for loc in locator:
                if self.is_exist(loc):
                    return True
            time.sleep(1)
        return False

    def wait_clickable(self, locator, timeout=10):
        '''
        等待控件可点击
        :param locator:
        :param timeout:
        :return:
        '''
        if isinstance(locator, tuple):
            el = self.get_element(locator)
        else:
            el = locator

        end = time.time() + timeout
        if self.platform == 'ios':
            while time.time() < end:
                if el.get_attribute('enabled') == 'true':
                    return True
                time.sleep(1)
        else:
            while time.time() < end:
                if el.get_attribute('clickable') == 'true':
                    return True
                time.sleep(1)
        return False

    def clear_text(self, locator):
        if isinstance(locator, tuple):
            el = self.get_element(locator)
        else:
            el = locator

        el.click()
        if self.platform == 'ios':
            text = self.get_ele_attr(el, 'value')
            if text is None or text.startswith('P'):
                return
            btn = self.get_element(('xpath', '//XCUIElementTypeKey[@name="delete" or @name="Delete"]'))
            for i in range(len(text.strip())):
                self.click_element(btn)

        if self.platform == 'android':
            # 123代表光标移动到末尾
            self.driver.press_keycode(123)
            for i in range(len(el.text.strip())):
                # 67退格键
                self.driver.press_keycode(67)

    def send_keys(self, locator, text, times=1):
        '''
        带检查的文本输入，保证输入的字符串无误
        :param locator:
        :param text:
        :param times:
        :return:
        '''
        if isinstance(locator, tuple):
            el = self.get_element(locator)
        else:
            el = locator
        el_text = el.text.strip()
        for i in range(times):
            if el_text == text:
                return True
            el.clear()
            # self.clear_text(el)
            el.send_keys(text)

    def swipe_by_element(self, direction, start, end, percent, locator=None, duration=None):
        '''
        滑动
        :param direction: 方向
        :param start: 起点相对（控件/屏幕）位置
        :param end: 终点相对（控件/屏幕）位置
        :param percent: 整体滑动在屏幕的位置
        :param locator: 控件，如不指定则是整个屏幕
        :param duration: 时长
        :return:
        '''
        if locator is None:
            window_size = self.driver.get_window_size()
            x = 0
            y = 0
            width = window_size['width']
            height = window_size['height']
        else:
            att = self.get_element_attributes(locator)
            x = att['left']
            y = att['top']
            width = att['width']
            height = att['height']
        if direction == 'up' or direction == 'down':
            start_x = x + int(percent * width)
            if self.platform == 'android' and locator is not None:
                end_y = y + int(start * height)
                start_y = y + int(end * height)
            else:
                start_y = y + int(start * height)
                end_y = y + int(end * height)
            self.driver.swipe(start_x, start_y, start_x, end_y, duration)
        elif direction == 'left' or direction == 'right':
            start_x = x + int(start * width)
            end_x = x + int(end * width)
            start_y = y + int(percent * height)
            self.driver.swipe(start_x, start_y, end_x, start_y, duration)

    def swipe_to_find_element(self, scrollable_element_locator, target_element_locator, direction, duration=None,
                              limit=10):
        '''
        swipe the scrollable_element to find target_element
        :param scrollable_element_locator:
        :param target_element_locator:
        :param direction:
        :param duration:
        :param limit:
        :return:
        '''
        self.wait_exist(scrollable_element_locator)
        scrollable_element_attributes = self.get_element_attributes(scrollable_element_locator)
        attempts = 0
        while True:
            if self.is_exist(target_element_locator):
                return self.get_element(target_element_locator)
            if attempts == limit:
                return None
            else:
                if direction == 'up':
                    self.driver.swipe(
                        scrollable_element_attributes['center_x'],
                        (scrollable_element_attributes['top'] + scrollable_element_attributes['center_y']) / 2,
                        scrollable_element_attributes['center_x'],
                        (scrollable_element_attributes['bottom'] + scrollable_element_attributes['center_y']) / 2,
                        duration
                    )
                elif direction == 'down':
                    self.driver.swipe(
                        scrollable_element_attributes['center_x'],
                        (scrollable_element_attributes['bottom'] + scrollable_element_attributes['center_y']) / 2,
                        scrollable_element_attributes['center_x'],
                        (scrollable_element_attributes['top'] + scrollable_element_attributes['center_y']) / 2,
                        duration
                    )
                elif direction == 'left':
                    self.driver.swipe(
                        (scrollable_element_attributes['left'] + scrollable_element_attributes['center_x']) / 2,
                        scrollable_element_attributes['center_y'],
                        (scrollable_element_attributes['right'] + scrollable_element_attributes['center_x']) / 2,
                        scrollable_element_attributes['center_y'],
                        duration
                    )
                elif direction == 'right':
                    self.driver.swipe(
                        (scrollable_element_attributes['right'] + scrollable_element_attributes['center_x']) / 2,
                        scrollable_element_attributes['center_y'],
                        (scrollable_element_attributes['left'] + scrollable_element_attributes['center_x']) / 2,
                        scrollable_element_attributes['center_y'],
                        duration
                    )
                else:
                    return None
            attempts += 1

    def get_element_by_type(self, method, value):
        msg = 'selenium.common.exceptions.FindElementTimeoutException:' \
              ' ("{}", "{}") could not be located on the page using the given search parameters.'.format(method, value)

        if method == 'accessibility_id':
            locator = (MobileBy.ACCESSIBILITY_ID, value)
        elif method == 'android':
            locator = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().{}'.format(value))
        elif method == 'ios':
            # 这里把IOS_UIAUTOMATION换掉了，新版好像不支持了，改成了元素属性，例如：'type="XCUIElementTypeSwitch"'
            locator = (MobileBy.IOS_PREDICATE, value)
        elif method == 'class_name':
            locator = (By.CLASS_NAME, value)
        elif method == 'id':
            locator = (By.ID, value)
        elif method == 'xpath':
            locator = (By.XPATH, value)
        elif method == 'name':
            locator = (By.NAME, value)
        else:
            raise Exception('Invalid locator method.')
        # 每次查找元素最多等待10s，每隔0.5s查找一次
        return WebDriverWait(self.driver, 20, 0.5).until(EC.visibility_of_element_located(locator), msg.format(value))

    def get_elements_by_type(self, method, value):
        if method == 'accessibility id':
            return self.driver.find_elements_by_accessibility_id(value)
        elif method == 'android':
            return self.driver.find_elements_by_android_uiautomator(value)
        elif method == 'ios':
            return self.driver.find_elements_by_ios_predicate(value)
        elif method == 'class name':
            return self.driver.find_elements_by_class_name(value)
        elif method == 'id':
            return self.driver.find_elements_by_id(value)
        elif method == 'xpath':
            return self.driver.find_elements_by_xpath(value)
        elif method == 'name':
            return self.driver.find_elements_by_name(value)
        else:
            raise Exception('Invalid locator method.')

    def get_element_attributes(self, locator):
        '''
        获取控件位置和大小信息
        :param locator:
        :return:
        '''
        if isinstance(locator, tuple):
            element = self.get_element(locator)
        else:
            element = locator
        return {
            'top': element.location['y'],
            'bottom': element.location['y'] + element.size['height'],
            'left': element.location['x'],
            'right': element.location['x'] + element.size['width'],
            'width': element.size['width'],
            'height': element.size['height'],
            'center_x': (element.size['width'] // 2) + element.location['x'],
            'center_y': (element.size['height'] // 2) + element.location['y']
        }

    def get_ele_attr(self, locator, attr_name):
        '''
        获取元素指定属性
        :param locator: 元素定位方式
        :param attr_name:属性名
        :return:
        '''
        if isinstance(locator, tuple):
            ele = self.get_element(locator)
        else:
            ele = locator
        return ele.get_attribute(attr_name)

    def get_size(self):
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        return width, height

    def tap(self, x, y):
        '''
        点击坐标
        :param x:
        :param y:
        :return:
        '''
        self.driver.tap([(x, y)], 300)

    def long_press(self, ele, duration=3):
        """
        长按操作
        :param ele:传参为一个元素
        :param duration:
        :return:
        """
        if ele.get_attribute('clickable') == 'false':
            attr = self.get_element_attributes(ele)
            TouchAction(self.driver).long_press(attr['center_x'], attr['center_y'], duration * 1000).release().perform()
        else:
            TouchAction(self.driver).long_press(ele, duration*1000).release().perform()

    def press_and_move(self, desc, ele_btn):
        """
        按压一个元素并读取文本信息
        :return:
        """
        touch = TouchAction(self.driver)
        btn = self.get_element(ele_btn)
        attr = self.get_element_attributes(btn)
        if desc == 'down':
            touch.press(btn, attr['center_x'], attr['top']).wait(3).move_to(btn, attr['center_x'], attr['bottom']).release().perform()
        elif desc == 'up':
            touch.press(btn, attr['center_x'], attr['bottom']).wait(3).move_to(btn, attr['center_x'], attr['top']).release().perform()

    def page_source(self):
        '''
        获取当前页面所有控件信息
        :return:
        '''
        return self.driver.page_source

    def image_color(self, path):
        '''
        计算图片的色调
        :param path:
        :return:
        '''
        image = Image.open(path)
        # 颜色模式转换，以便输出rgb颜色值
        image = image.convert('RGB')
        image_size = image.size[0] * image.size[1]
        R = G = B = i = 0
        for count, (r, g, b) in image.getcolors(image_size):
            if r == 255 and g == 255 and b == 255:
                continue
            elif r == 0 and g == 0 and b == 0:
                continue
            else:
                R += r
                G += g
                B += b
                i += 1
        R = int(R / i)
        G = int(G / i)
        B = int(B / i)
        return (R, G, B)

    def screen_ele_shot(self, locator):
        """
        截取元素图片
        :return:
        """
        if isinstance(locator, tuple):
            ele = self.get_element(locator)
        else:
            ele = locator

        path = '{}/src/images/ele.png'.format(base_path.get_path())
        ele.screenshot(path)
        return path

    def compare_img(self, locator, expect_img, res=5):
        """
        比较两张图片相识度
        :param locator:
        :param expect_img:
        :return:
        """
        if isinstance(locator, tuple):
            ac_img = self.screen_ele_shot(locator)
        else:
            ac_img = locator
        ac_hash = util.pHash(ac_img)
        if self.platform == 'ios':
            expect_img = '{}/src/images/ios_eleimg/{}.png'.format(base_path.get_path(), expect_img)
        elif self.platform == 'android':
            expect_img = '{}/src/images/android_eleimg/{}.png'.format(base_path.get_path(), expect_img)
        expect_hash = util.pHash(expect_img)
        _res = util.cmpHash(ac_hash, expect_hash)
        os.remove(ac_img)
        if _res <= res:
            return True
        else:
            return False

    def is_colorful(self, locator):
        '''
        控件颜色是不是彩色的，可以用于判断开关是否打开，设备是否在线等
        :param locator:
        :return:
        '''
        if isinstance(locator, tuple):
            el = self.get_element(locator)
        else:
            el = locator

        path = '{}/src/images/click_image.png'.format(base_path.get_path())
        el.screenshot(path)
        (r, g, b) = self.image_color(path)
        if abs(r - g) <= 3 and abs(g - b) <= 3 and abs(r - b) <= 3:  # 灰r=g=b，白r=g=b=255，黑r=g=b=0
            return False
        else:
            return True

    def wait_colorful(self, locator, timeout=10):
        '''
        控件颜色是不是彩色的，可以用于判断开关是否打开，设备是否在线等
        :param locator:
        :param timeout:
        :param expect_img:
        :return:
        '''
        end = time.time() + timeout
        while time.time() < end:
            if self.is_colorful(locator):
                return True
            else:
                time.sleep(1)
        return False

    def get_image_point(self, path):
        '''
        查找图片元素坐标
        :param path:目标图片
        :return:
        '''
        # 目标控件的截图
        find_img = cv2.imread(path)  # 目标截图
        # 对当前屏幕进行截图
        img_path = '{}/src/images/click_image.png'.format(base_path.get_path())
        self.driver.get_screenshot_as_file(img_path)  # 当前屏幕截图
        target_img = cv2.imread(path)
        # 在当前屏幕的截图上进行横向和纵向比对，查找目标控件
        result = cv2.matchTemplate(target_img, find_img, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        # 如果相似度最高的位置，相似度达到99.9%，说明已经找到了目标控件
        if max_val > 0.999:
            find_height, find_width, find_channel = find_img.shape[::]
            width = self.driver.get_window_size()['width']
            multiple = find_width / width  # 算出倍数
            x = max_loc[0] + int(find_width * 0.5)  # 像素点
            x = int(x / multiple)  # 坐标点
            y = max_loc[1] + int(find_height * 0.5)  # 像素点
            y = int(y / multiple)  # 坐标点
            return x, y
        else:
            raise Exception('Not Found Image Element')

    def image_is_exists(self, path, timeout=60):
        '''
        图片所对应的控件是否存在
        :param path:目标图片
        :param timeout:
        :return:
        '''
        # 目标控件的截图
        find_img = cv2.imread(path)  # 目标截图
        img_path = '{}/src/images/click_image.png'.format(base_path.get_path())
        for i in range(timeout):
            # 对当前屏幕进行截图
            self.driver.get_screenshot_as_file(img_path)  # 当前屏幕截图
            target_img = cv2.imread(path)
            # 在当前屏幕的截图上进行横向和纵向比对，查找目标控件
            result = cv2.matchTemplate(target_img, find_img, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            # 如果相似度最高的位置，相似度达到99.9%，说明已经找到了目标控件
            if max_val > 0.999:
                return True
            else:
                time.sleep(5)
        return False

    def execute_command(self, command, desc):
        self.driver.execute_script(command, desc)

    def screen_shot(self, path):
        """
        截取屏幕
        :return:
        """
        self.driver.get_screenshot_as_file(path)

    def find_toast(self, message, android_in_current_page=True, ios_in_current_page=True):
        """
        查找toast
        :param message:
        :param android_in_current_page: toast是否在当前页面显示
        :param ios_in_current_page: toast是否在当前页面显示
        :return:
        """
        if self.platform == 'android':
            toast_element = (By.XPATH, '//*[starts-with(@text,"{}")]'.format(message))  # @class="android.widget.Toast"
            flag = android_in_current_page
        else:
            toast_element = (By.XPATH, '//*[starts-with(@name,"{}")]'.format(message))
            flag = ios_in_current_page
        try:
            if flag:
                toast = WebDriverWait(self.driver, 15, 0.1).until(EC.presence_of_element_located(toast_element))
            else:
                toast = WebDriverWait(self.driver, 15, 0.1).until(lambda driver: driver.find_element(toast_element))
        except Exception as e:
            print(e)
            toast = None
        return toast

    def find_ele(self, locator):
        """
        直接查找元素
        :param locator:
        :return:
        """
        return self.driver.find_element(locator)

    def adb_input(self, locator, text):
        """
        使用adb命令输入
        :param locator:
        :param text:
        :return:
        """
        if isinstance(locator, tuple):
            el = self.get_element(locator)
        else:
            el = locator
        self.tap_element(el)
        os.system('adb shell input text "{}"'.format(text))
