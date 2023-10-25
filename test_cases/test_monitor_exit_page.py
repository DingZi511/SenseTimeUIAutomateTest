"""
===================================
Time：2023/7/21
===================================
"""
import os
import allure
import pytest
from airtest.core.api import *
from airtest.core.android import Android
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

@allure.feature("健康检测")
class TestCheck():
    def setup_method(self):
        auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/HQM6R22B24000796?cap_method=MINICAP&touch_method=MAXTOUCH&", ])
        start_app('com.senseauto.healthdetect')
        sleep(3)

    @allure.feature('健康检测-检测中退出页面模块')
    @allure.story('健康检测之检测中点击左上角的返回按钮显示是否符合设计要求')
    def test_health_check_exit_page(self):
        if exists(Template(r"tpl1698199110469.png", record_pos=(-0.159, -0.126), resolution=(2560, 1600))):
            touch(Template(r"tpl1698199122282.png", record_pos=(-0.171, -0.159), resolution=(2560, 1600)))

        if assert_exists(Template(r"tpl1698199243891.png", record_pos=(-0.004, 0.005), resolution=(2560, 1600)),
                         "正常跳转到了健康检测识别选择界面"):
            assert_equal(poco("com.senseauto.healthdetect:id/tv_tips").get_text(), "请选择被检测人", "小糖智能的提示语正确")
            touch(Template(r"tpl1698199432166.png", record_pos=(-0.245, -0.002), resolution=(2560, 1600)))
            sleep(1)

        if assert_exists(Template(r"tpl1698199563430.png", record_pos=(-0.194, 0.272), resolution=(2560, 1600)),
                         "正确的跳转到了健康检测人脸扫描页面"):
            assert_equal(poco("com.senseauto.healthdetect:id/tv_tips").get_text(), "请保持正面面对摄像头，在采集框内请保持静止，避免晃动",
                         "人脸扫描页面小糖智能提示语正确")
            sleep(1)
            touch(Template(r"tpl1698199795731.png", record_pos=(-0.454, -0.283), resolution=(2560, 1600)))
            assert_exists(Template(r"tpl1698199825030.png", record_pos=(-0.018, -0.043), resolution=(2560, 1600)),
                          "点击返回按钮正常跳转到了首页")
        sleep(3)
        # if poco(text="请保持正面面对摄像头，在采集框内请保持静止，避免晃动").exists():
      

    @allure.feature('健康检测-检测出报告页面')
    @allure.story('健康检测之检测出报告中成功提示页面的显示是否符合设计要求')
    def test_health_make_report_page(self):
        touch(Template(r"case_images/healthRisk_images/tpl1689667365289.png", record_pos=(-0.463, 0.234),resolution=(1920, 1200)), duration=2.0)
        poco("com.senseauto.healthdetect:id/bt_health_detect").click()
        # 等待该页面消失
        if poco(text="请选择被检测人 ").wait_for_disappearance():
            assert_equal(poco("com.senseauto.healthdetect:id/tv_tips_result").get_text().__contains__("欢迎您使用健康检测请您保持静止，即将开始检测"),True, "成功绕过人脸登录转跳到了人脸图片识别中")
        sleep(3)
        poco(text="您好，检测已经开始了，为了检测的准确度，请您面向 摄像头，保持静止，很快就能看到结果了！").wait_for_appearance(20)

        assert_exists(Template(r"case_images/healthRisk_images/tpl1689930868878.png", record_pos=(-0.005, -0.007), resolution=(1920, 1200)),"出报告中，成功提示页面")

    @allure.feature('健康检测-检测结果页面')
    @allure.story('健康检测之检测结果页面中页面提示语以及UI的显示是否符合设计要求')
    def test_health_result_page(self):
        touch(Template(r"case_images/healthRisk_images/tpl1689667365289.png", record_pos=(-0.463, 0.234),resolution=(1920, 1200)), duration=2.0)
        poco("com.senseauto.healthdetect:id/bt_health_detect").click()
        # 等待该页面消失
        if poco(text="请选择被检测人 ").wait_for_disappearance():
            assert_equal(poco("com.senseauto.healthdetect:id/tv_tips_result").get_text().__contains__("欢迎您使用健康检测请您保持静止，即将开始检测"),True, "成功绕过人脸登录转跳到了人脸图片识别中")
        sleep(3)
        poco(text="您好，检测已经开始了，为了检测的准确度，请您面向 摄像头，保持静止，很快就能看到结果了！").wait_for_appearance(20)

        assert_exists(Template(r"case_images/healthRisk_images/tpl1689930868878.png", record_pos=(-0.005, -0.007),resolution=(1920, 1200)), "出报告中，成功提示页面")
        assert_equal(poco("com.senseauto.healthdetect:id/tv_health_record_remark").get_text().__contains__("仅作为参考，不可作为医疗专业诊断"),True, "正常跳转到了健康检测结果页面")
        if poco(text="检测结果").exists():
            poco("com.senseauto.healthdetect:id/tvDetectResult").click()
            if poco(text="偏低").exists():
                assert_equal(poco("com.senseauto.healthdetect:id/tv_robot_text").get_text(), "本次健康检测存在不达标项，请关注身体健康~","在不达标时小机器人的提示语是否正确")
            else:
                assert_equal(poco("com.senseauto.healthdetect:id/tv_robot_text").get_text(), "恭喜您，本次检测各项指标一切正常，继续保持~","在达标时小机器人的提示语是否正确")
        else:
            print("没有正常跳转到检测结果页面来")

    @allure.feature('健康检测-健康风险页面')
    @allure.story('健康检测之健康风险页面中页面提示语以及UI的显示是否符合设计要求')
    def test_health_risk_page(self):
        touch(Template(r"case_images/healthRisk_images/tpl1689667365289.png", record_pos=(-0.463, 0.234),resolution=(1920, 1200)), duration=2.0)
        poco("com.senseauto.healthdetect:id/bt_health_detect").click()
        # 等待该页面消失
        if poco(text="请选择被检测人 ").wait_for_disappearance():
            assert_equal(poco("com.senseauto.healthdetect:id/tv_tips_result").get_text().__contains__("欢迎您使用健康检测请您保持静止，即将开始检测"),True, "成功绕过人脸登录转跳到了人脸图片识别中")
        sleep(3)
        poco(text="您好，检测已经开始了，为了检测的准确度，请您面向 摄像头，保持静止，很快就能看到结果了！").wait_for_appearance(20)

        assert_exists(Template(r"case_images/healthRisk_images/tpl1689930868878.png", record_pos=(-0.005, -0.007),resolution=(1920, 1200)), "出报告中，成功提示页面")
        assert_equal(poco("com.senseauto.healthdetect:id/tv_health_record_remark").get_text().__contains__("仅作为参考，不可作为医疗专业诊断"),True, "正常跳转到了健康检测结果页面")
        if poco(text="健康风险").exists():
            poco("com.senseauto.healthdetect:id/tvHealthRisk").click()
            if poco(text="心率").exists():
                swipe((1779, 903), (1779, 290), duration=1)
                assert_equal(poco("com.senseauto.healthdetect:id/tv_health_record_recommend_service").get_text(),"为您推荐的相关健康服务", "健康有风险页面内容显示正常")
            else:
                assert_equal(poco(text="恭喜您，本次检测各项指标一切正常，继续保持~"), "恭喜您，本次检测各项指标一切正常，继续保持~", "健康无风险页面内容显示正常")


def teardown_method(self):
        stop_app('com.senseauto.healthdetect')