"""
===================================
Author:商汤科技-刘孜煜
Time：2023/7/17
E-mail:liuziyu1@senseauto.com
Company:商汤科技
===================================
"""
import os
import allure
import pytest
from airtest.core.api import *
from airtest.core.android import Android
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
@allure.feature("注册")
class TestRegister():
    @allure.story("注册成功")
    def test_register_success(self):
        print("测试用例：注册成功")
        pass
    @allure.story("注册失败")
    def test_register_failure(self):
        with allure.step("输入用户名"):
            print("输入用户名")
        with allure.step("输入密码"):
            print("输入密码")
        with allure.step("再次输入密码"):
            print("再次输入密码")
        print("点击注册")
        with allure.step("注册失败"):
            assert 1 + 1 == 2
            print("注册失败")



@allure.feature("健康关怀")
class TestHealth():
    def setup_method(self):
        auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/HQM6R22B24000796?cap_method=MINICAP&touch_method=MAXTOUCH&", ])
        start_app('com.senseauto.healthdetect')
        sleep(3)

    @allure.feature('健康关怀模块')
    @allure.story('健康关怀检测页面显示符合设计要求')
    def test_health_monitoring_home_contents(self):
        assert_equal(poco("com.senseauto.healthdetect:id/firstTips").get_text(), "请摘除口罩与墨镜等遮挡物哦","判断健康关怀左下角机器人的提示语是否正确")
        sleep(4)
        poco(name="com.senseauto.healthdetect:id/iv_close").click()
        sleep(5)

    @allure.feature('人脸识别')
    @allure.story('人脸识别开始页面符合设计要求')
    def test_face_identification_starts(self):
        assert_exists(Template(r"case_images/healthRisk_images/tpl1689233594470.png", record_pos=(-0.004, -0.285), resolution=(1920, 1200)),"成功跳转到健康关怀主页面")

        poco("com.senseauto.healthdetect:id/iv_health_detect").click()

        if exists(Template(r"case_images/healthRisk_images/tpl1689235963223.png", record_pos=(-0.366, 0.234),resolution=(1920, 1200))):
            assert_equal(poco("com.senseauto.healthdetect:id/tv_tips").get_text(), "请选择被检测人", "正常跳转到了健康检测开始识别页面")
            poco("com.senseauto.healthdetect:id/btn_reg_driver").click()

            if exists(Template(r"case_images/healthRisk_images/tpl1689236197627.png", record_pos=(-0.006, -0.268),resolution=(1920, 1200))):
                assert_equal(poco("com.senseauto.healthdetect:id/tv_tips").get_text(), "请保持正面面对摄像头，在采集框内请保持静止，避免晃动","识别主驾按钮可点击并且可以正常进入摄像头识别画面")
                poco("com.senseauto.healthdetect:id/iv_close").click()
                assert_exists(Template(r"case_images/healthRisk_images/tpl1689234844465.png", record_pos=(-0.007, -0.055),resolution=(1920, 1200)), "识别页面的返回键能正常返回到首页")
        # 到首页后再次点击健康检测按钮

        poco("com.senseauto.healthdetect:id/tv_iv_health_detect_text").click()
        if exists(Template(r"case_images/healthRisk_images/tpl1689235963223.png", record_pos=(-0.366, 0.234), resolution=(1920, 1200))):
            assert_equal(poco("com.senseauto.healthdetect:id/tv_tips").get_text(), "请选择被检测人", "正常跳转到了健康检测开始识别页面")
            poco("com.senseauto.healthdetect:id/btn_reg_copilot").click()
            if exists(Template(r"case_images/healthRisk_images/tpl1689237521614.png", record_pos=(-0.002, -0.266), resolution=(1920, 1200))):
                assert_equal(poco("com.senseauto.healthdetect:id/tv_tips").get_text(), "请保持正面面对摄像头，在采集框内请保持静止，避免晃动","识别副驾按钮可点击并且可以正常进入摄像头识别画面")
                poco("com.senseauto.healthdetect:id/iv_close").click()
                assert_exists(Template(r"case_images/healthRisk_images/tpl1689234844465.png", record_pos=(-0.007, -0.055), resolution=(1920, 1200)),"识别页面的返回键能正常返回到首页")


    @allure.story('人脸识别-老用户-未填写自评')
    def test_face_identification_oldUser_notfilled(self):
        touch(Template(r"case_images/oldUser_notfiled/tpl1689239355012.png", record_pos=(-0.461, 0.238), resolution=(1920, 1200)), duration=2.0)
        assert_equal(poco("com.senseauto.healthdetect:id/tv_test_environment").get_text(), "测试模式", "顺利跳转到debug健康检测弹框页面")
        poco("com.senseauto.healthdetect:id/bt_health_detect").click()
        sleep(3.0)
        while True:
            if assert_equal(poco("com.senseauto.healthdetect:id/tv_tips_result").get_text().__contains__('请先根据您的最近健康情况回答问题'),True, "未填写自评的老用户头像下方提示正确"):
                break
            print("未填写自评的老用户正常登录")

        poco("com.senseauto.healthdetect:id/iv_close").click()

    @allure.story('人脸识别-老用户-已填写自评')
    def test_face_identification_oldUser_filled(self):
        touch(Template(r"case_images/oldUser_notfiled/tpl1689239355012.png", record_pos=(-0.461, 0.238),resolution=(1920, 1200)), duration=2.0)
        assert_equal(poco("com.senseauto.healthdetect:id/tv_test_environment").get_text(), "测试模式", "顺利跳转到debug健康检测弹框页面")
        poco("com.senseauto.healthdetect:id/bt_health_detect").click()
        sleep(3.0)
        while True:
            if assert_equal(poco("com.senseauto.healthdetect:id/tv_tips_result").get_text().__contains__('欢迎您使用健康检测请您保持静止，即将开始检测'), True, "头像下方提示正确"):
                break
            print("老用户正常登录")

#这是全局的停止代码
    def teardown_method(self):
        stop_app('com.senseauto.healthdetect')
        
