"""
===================================
Author:商汤科技-刘孜煜
Time：2023/6/14
E-mail:liuziyu1@senseauto.com
Company:商汤科技
===================================
"""
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
class BasePage:
    def __init__(self):
        self.poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

    # 元素定位
    def get_element(self, locator):
        return self.poco(locator)

    def get_element_by_text(self, text):
        return self.poco(text)

    # 点击
    def click_button(self, locator):
        return self.poco(locator).click()

    # 等待元素出现
    def wait_element_appearance_by_id(self, locator):
        return self.poco(locator).wait_for_appearance()

    def wait_element_appearance_by_text(self, text):
        return self.poco(text=text).wait_for_appearance()

    # 输入
    def send_text(self, locator, text):
        return self.poco(locator).set_text(text)

    def get_text(self, locator):
        return self.poco(locator).get_text()

    # 清除输入数据
    def clear_text(self, locator):
        return self.poco(locator).set_text("")