
import os
import allure
import pytest
from airtest.core.api import *
from airtest.core.android import Android
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

@allure.feature("健康视诊")
class TestHealthOnline():
    def setup_method(self):
        auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/HQM6R22B24000796?cap_method=MINICAP&touch_method=MAXTOUCH&", ])
        start_app('com.senseauto.healthdetect')
        sleep(3)

    @allure.feature('进入到在线问诊模块')
    @allure.story('访客点击进入在线问诊')
    def test_health_online_lnQuiry(self):
        if exists(Template(r"case_images/healthRisk_images/tpl1698150685155.png", record_pos=(0.304, 0.117), resolution=(2560, 1600))):
            touch(Template(r"case_images/healthRisk_images/tpl1698150702446.png", record_pos=(0.305, 0.095), resolution=(2560, 1600)))

        if assert_exists(Template(r"case_images/healthRisk_images/tpl1698150826189.png", record_pos=(-0.372, -0.074), resolution=(2560, 1600)),
                         "问题列表存在的话"):
            touch(Template(r"case_images/healthRisk_images/tpl1698150868025.png", record_pos=(-0.377, -0.076), resolution=(2560, 1600)))

        if assert_exists(Template(r"case_images/healthRisk_images/tpl1698151004422.png", record_pos=(-0.007, 0.115), resolution=(2560, 1600)),
                         "正在等待中。。。。"):
            poco("com.senseauto.healthdetect:id/tips_tv").wait_for_disappearance()

        assert_equal(poco(text="首先，我需要了解一些更具体的信息以便更准确地判断你的症状。我的第一个问题是：你的胃部不适是持续性的还是间歇性的？").get_text(),
                     "首先，我需要了解一些更具体的信息以便更准确地判断你的症状。我的第一个问题是：你的胃部不适是持续性的还是间歇性的？", "小糖智能回答正确")

        if exists(Template(r"case_images/healthRisk_images/tpl1698151402061.png", record_pos=(-0.016, 0.271), resolution=(2560, 1600))):
            poco("com.senseauto.healthdetect:id/text_input").set_text(38.6)
            touch(Template(r"case_images/healthRisk_images/tpl1698151887711.png", record_pos=(0.381, 0.272), resolution=(2560, 1600)))
            assert_exists(Template(r"case_images/healthRisk_images/tpl1698152703707.png", record_pos=(0.142, -0.041), resolution=(2560, 1600)),
                          "小糖回答的很漂亮")

        sleep(1)
        touch(Template(r"case_images/healthRisk_images/tpl1698151524727.png", record_pos=(-0.457, -0.284), resolution=(2560, 1600)))
        sleep(2)
        wait(Template(r"case_images/healthRisk_images/tpl1698151576219.png", record_pos=(-0.001, 0.014), resolution=(2560, 1600)))
        touch(Template(r"case_images/healthRisk_images/tpl1698151593762.png", record_pos=(0.069, 0.066), resolution=(2560, 1600)))
        assert_exists(Template(r"case_images/healthRisk_images/tpl1698151625471.png", record_pos=(-0.004, -0.032), resolution=(2560, 1600)),
                      "正常返回了主页")

        # # if poco("com.senseauto.healthdetect:id/iv_robot").exists():
        # poco("com.senseauto.healthdetect:id/iv_robot").click()  # 进入到健康关怀主页面点击小机器人图标
        # # else:
        # #     poco("com.senseauto.healthdetect:id/iv_online_consultation").click()  # 进入到健康关怀主页面点击在线问诊图标
        # # 开始点击示例问题列表
        # if poco("com.senseauto.healthdetect:id/rv_question").exists():
        #     assert_equal(poco("com.senseauto.healthdetect:id/answer_content_tv").get_text(), "你好，我是小糖，您的智能医生",
        #                  "小糖智能问候语言正确")
        #     poco(text="胃有点不舒服，怎么办？").click()
        #     poco("com.senseauto.healthdetect:id/tips_tv").wait_for_disappearance()
        #     sleep(2)
        #     assert_equal(poco(text="首先，我需要了解一些更具体的信息以便更准确地判断你的症状。我的第一个问题是：你的胃部不适是持续性的还是间歇性的？").get_text(),
        #                  "首先，我需要了解一些更具体的信息以便更准确地判断你的症状。我的第一个问题是：你的胃部不适是持续性的还是间歇性的？", "小糖智能回答正确")
        #     sleep(2)
        #     poco("com.senseauto.healthdetect:id/text_input").set_text(38.6)
        #     poco("com.senseauto.healthdetect:id/iv_send").click()
        #     sleep(2)
        #     poco("com.senseauto.healthdetect:id/iv_back").click()
        #     sleep(2)
        #     if poco("android.view.ViewGroup").wait_for_appearance():
        #         poco("com.senseauto.healthdetect:id/bt_confirm").click()
        #
        # elif assert_equal(poco(text="网络无法连接，请稍后再试").get_text(), "网络无法连接，请稍后再试", "网络异常判断正确"):
        #     poco("com.senseauto.healthdetect:id/iv_back").click()
        #     if poco("android.view.ViewGroup").wait_for_appearance():
        #         poco("com.senseauto.healthdetect:id/bt_confirm").click()

    def teardown_method(self):
        stop_app('com.senseauto.healthdetect')