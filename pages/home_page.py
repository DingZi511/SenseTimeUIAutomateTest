"""
===================================
Time：2023/7/4
===================================
"""
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from pages import BasePage
from base import readYAML

class HomePage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        # ele元素事例

        # img图片事例
        self.e_invite_day_img = self("邀请页面图片",'Template(r"tpl1576805695978.png", record_pos=(-0.246, -0.551), resolution=(720, 1280))')

        self._end = self()
        self.RY = readYAML.ReadYAML()
        BasePage.__init__(self)

