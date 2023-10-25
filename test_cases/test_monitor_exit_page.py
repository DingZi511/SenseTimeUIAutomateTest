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
    def setup(self):
        auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/HQM6R22B24000796?cap_method=MINICAP&touch_method=MAXTOUCH&", ])
        start_app('com.senseauto.healthdetect')
        sleep(3)

    @allure.feature('健康检测-检测中退出页面模块')
    @allure.story('健康检测之检测中点击左上角的返回按钮显示是否符合设计要求')
    def test_health_check_exit_page(self):
        if exists(Template(r"case_images/healthRisk_images/tpl1698199110469.png", record_pos=(-0.159, -0.126), resolution=(2560, 1600))):
            touch(Template(r"case_images/healthRisk_images/tpl1698199122282.png", record_pos=(-0.171, -0.159), resolution=(2560, 1600)))

        if assert_exists(Template(r"case_images/healthRisk_images/tpl1698199243891.png", record_pos=(-0.004, 0.005), resolution=(2560, 1600)),
                         "正常跳转到了健康检测识别选择界面"):
            assert_equal(poco("com.senseauto.healthdetect:id/tv_tips").get_text(), "请选择被检测人", "小糖智能的提示语正确")
            touch(Template(r"case_images/healthRisk_images/tpl1698199432166.png", record_pos=(-0.245, -0.002), resolution=(2560, 1600)))
            sleep(1)

        if assert_exists(Template(r"case_images/healthRisk_images/tpl1698199563430.png", record_pos=(-0.194, 0.272), resolution=(2560, 1600)),
                         "正确的跳转到了健康检测人脸扫描页面"):
            assert_equal(poco("com.senseauto.healthdetect:id/tv_tips").get_text(), "请保持正面面对摄像头，在采集框内请保持静止，避免晃动",
                         "人脸扫描页面小糖智能提示语正确")
            sleep(1)
            touch(Template(r"case_images/healthRisk_images/tpl1698199795731.png", record_pos=(-0.454, -0.283), resolution=(2560, 1600)))
            assert_exists(Template(r"case_images/healthRisk_images/tpl1698199825030.png", record_pos=(-0.018, -0.043), resolution=(2560, 1600)),
                          "点击返回按钮正常跳转到了首页")
        sleep(3)
        # if poco(text="请保持正面面对摄像头，在采集框内请保持静止，避免晃动").exists():


    @allure.feature('情绪与疲劳检测')
    @allure.story('情绪与疲劳检测之检测页面的显示是否符合设计要求')
    def test_emotion_fatigue_detection_page(self):
        if exists(Template(r"case_images/healthRisk_images/tpl1698201713968.png", record_pos=(-0.324, 0.122), resolution=(2560, 1600))):
            touch(Template(r"case_images/healthRisk_images/tpl1698201728774.png", record_pos=(-0.333, 0.083), resolution=(2560, 1600)))

        if assert_exists(Template(r"case_images/healthRisk_images/tpl1698201825694.png", record_pos=(0.011, -0.009), resolution=(2560, 1600)),"正常跳转到了情绪与疲劳检测页面了"):
            assert_equal(poco(text="持续监测您驾驶中的情绪与疲劳，如遇异常将自动触发以下提醒").get_text(), "持续监测您驾驶中的情绪与疲劳，如遇异常将自动触发以下提醒","自动触发提醒文案正确无误")
            touch(Template(r"case_images/healthRisk_images/tpl1698201982795.png", record_pos=(-0.122, -0.155), resolution=(2560, 1600)))
            sleep(1)
        if assert_exists(Template(r"case_images/healthRisk_images/tpl1698202041975.png", record_pos=(-0.003, 0.248), resolution=(2560, 1600)),"正常跳转到了脸部扫描检测页面"):
            if assert_exists(Template(r"case_images/healthRisk_images/tpl1698202165570.png", record_pos=(0.002, -0.012), resolution=(2560, 1600)),"异常图片检测"):
                assert_equal(poco("com.senseauto.healthdetect:id/tv_tired_grade").get_text(), "由于未捕捉到脸部，请将脸部对准摄像头","异常情况文案提示正确无误")
                touch(Template(r"case_images/healthRisk_images/tpl1698202292659.png", record_pos=(0.0, 0.248), resolution=(2560, 1600)))
                sleep(1)
                assert_exists(Template(r"case_images/healthRisk_images/tpl1698202659631.png", record_pos=(0.001, 0.273), resolution=(2560, 1600)),"异常结束检测toast提示正确")
                touch(Template(r"case_images/healthRisk_images/tpl1698202968872.png", record_pos=(-0.447, -0.281), resolution=(2560, 1600)))

                assert_exists(Template(r"case_images/healthRisk_images/tpl1698203021469.png", record_pos=(-0.011, -0.014), resolution=(2560, 1600)),"正常跳转到了首页")

    @allure.feature('情绪疲劳-预警温度设置')
    @allure.story('情绪疲劳之检测预警温度设置是否符合设计要求')
    def test_temperature_settability_page(self):
        if exists(Template(r"case_images/healthRisk_images/tpl1698201713968.png", record_pos=(-0.324, 0.122), resolution=(2560, 1600))):
            touch(Template(r"case_images/healthRisk_images/tpl1698201728774.png", record_pos=(-0.333, 0.083), resolution=(2560, 1600)))

        if assert_exists(Template(r"case_images/healthRisk_images/tpl1698203817402.png", record_pos=(0.21, -0.209), resolution=(2560, 1600)),"成功进入到了预警温度设置页面"):
            touch(Template(r"case_images/healthRisk_images/tpl1698203973874.png", record_pos=(0.23, -0.118), resolution=(2560, 1600)))
            assert_exists(Template(r"case_images/healthRisk_images/tpl1698204051867.png", record_pos=(0.221, 0.066), resolution=(2560, 1600)),"期望温度显示正常")
            touch(Template(r"case_images/healthRisk_images/tpl1698204013836.png", record_pos=(0.354, -0.116), resolution=(2560, 1600)))
            touch(Template(r"case_images/healthRisk_images/tpl1698204342464.png", record_pos=(0.326, 0.094), resolution=(2560, 1600)), times=3,duration=0.05)
            touch(Template(r"case_images/healthRisk_images/tpl1698204473629.png", record_pos=(0.103, -0.119), resolution=(2560, 1600)))
            touch(Template(r"case_images/healthRisk_images/tpl1698204484829.png", record_pos=(0.12, 0.091), resolution=(2560, 1600)), times=3,duration=0.05)
            touch(Template(r"case_images/healthRisk_images/tpl1698204560620.png", record_pos=(-0.452, -0.284), resolution=(2560, 1600)))
            assert_exists(Template(r"case_images/healthRisk_images/tpl1698204577975.png", record_pos=(-0.005, -0.016), resolution=(2560, 1600)),"正常跳转到了首页")


def teardown(self):
        stop_app('com.senseauto.healthdetect')