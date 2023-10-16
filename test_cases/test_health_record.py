"""
===================================
Author:商汤科技-刘孜煜
Time：2023/8/17
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

@allure.feature("健康档案")
class TestHealthRecord():
    def setup_method(self):
        auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/HQM6R22B24000796?cap_method=MINICAP&touch_method=MAXTOUCH&", ])
        start_app('com.senseauto.healthdetect')
        sleep(3)

    @allure.feature('健康检测访客扫描进入创建档案模块')
    @allure.story('访客扫描进入创建档案')
    def test_health_visitor_enter_create_record(self):
        poco("com.senseauto.healthdetect:id/iv_account_manage").click()
        # 点击后断言是否正常跳转到健康检测主副驾驶识别页面
        if poco("com.senseauto.healthdetect:id/iv_robot").exists():
            assert_equal(poco("com.senseauto.healthdetect:id/tv_tips").get_text(), "请选择被检测人", "正常跳转到健康检测主副驾驶识别页面")
        else:
            clear_app("com.senseauto.healthdetect")

        # 已经正常的进入到主副驾识别页面了，此时需要进行点击识别主驾操作了
        poco(text="识别主驾").click()
        # 对人脸图片扫描页面进行断言
        if poco("com.senseauto.healthdetect:id/iv_robot").exists():
            assert_equal(poco("com.senseauto.healthdetect:id/tv_tips").get_text(), "请保持正面面对摄像头，在采集框内请保持静止，避免晃动",
                         "正常跳转到健康检测人脸图片扫描页面")
        else:
            snapshot(msg="点击识别主驾操作没响应")
            clear_app("com.senseauto.healthdetect")
        # 此时需要拿起照片进行人脸扫描操作了
        if poco(text="创建档案").wait_for_appearance():
            assert_equal(
                poco("com.senseauto.healthdetect:id/tv_tips_result").get_text().__contains__("Hi 访客，欢迎您使用健康检测"), True,
                "人脸图片扫描成功")
        else:
            poco(text="请保持正面面对摄像头，在采集框内请保持静止，避免晃动").wait_for_disappearance()

    @allure.feature('创建档案')
    @allure.story('访客创建档案')
    def test_health_visitor_create_record(self):
        poco("com.senseauto.healthdetect:id/btn_create_record").click()
        # 断言是否正常跳转到了个人资料填写页面
        if poco("com.senseauto.healthdetect:id/iv_robot").exists():
            assert_equal(poco(text="填写信息用于精准获取建议").get_text(), "填写信息用于精准获取建议", "正常跳转到了个人资料填写页面")
        else:
            snapshot(msg="访客没有正常跳转到个人资料填写页面")
            poco("com.senseauto.healthdetect:id/iv_close").click()

        # 开始进行访客个人资料填写操作
        poco("com.senseauto.healthdetect:id/et_nickname").set_text('西伯利亚狼001')  # 因为是set进去的，所以没有键盘的弹出
        # 点击键盘褪去按钮
        # touch(2246,885)
        # sleep(2.0)
        # 点击性别男选项
        poco("com.senseauto.healthdetect:id/radioButtonMale").click()
        sleep(2.0)
        # 对年龄进行设置
        poco("com.senseauto.healthdetect:id/et_age").click()
        # 在年龄弹框中下拉选中某个年龄进行确定操作(如果该弹框存在，那么我就在里头进行下滑选中操作)
        if poco("com.senseauto.healthdetect:id/pickerView").exists():
            swipe((1461, 990), (1461, 30), duration=1)
            poco("com.senseauto.healthdetect:id/tv_agree").click()  # 点击确定按钮
        #     touch(2246,885) #褪去键盘
        #     sleep(2.0)
        else:
            snapshot(msg="年龄选择弹框没有正常的弹跳出来")
            clear_app("com.senseauto.healthdetect")

        # 对身高进行设置
        poco("com.senseauto.healthdetect:id/et_height").click()  # 点击身高选择按钮
        if poco("com.senseauto.healthdetect:id/pickerView").exists():
            swipe((1461, 990), (1461, 30), duration=1)
            poco("com.senseauto.healthdetect:id/tv_agree").click()
        else:
            snapshot(msg="身高选择弹框没有正常的弹跳出来")
            clear_app("com.senseauto.healthdetect")

            # 对体重进行设置
        poco("com.senseauto.healthdetect:id/et_weight").click()
        if poco("android.widget.FrameLayout").offspring("android:id/content").child("android.widget.LinearLayout").child("android.widget.LinearLayout")[0].exists():
            swipe((1066, 1008), (1066, 30), duration=1)
            swipe((1664, 1046), (1664, 385), duration=1)
            poco("com.senseauto.healthdetect:id/tv_agree").click()
        #     touch(2246,885) #褪去键盘
        #     sleep(2.0)
        else:
            snapshot(msg="体重选择弹框没有正常的弹跳出来")
            clear_app("com.senseauto.healthdetect")
        # 填好了个人信息后点击确定按钮进行信息的提交
        poco("com.senseauto.healthdetect:id/btn_commit").click()
        if poco("android.view.ViewGroup").exists():
            assert_equal(poco(text="请确保填写信息真实准确，否则将影响计算精度").get_text(), "请确保填写信息真实准确，否则将影响计算精度", "正常弹出了信息填写确认提示弹框")
            poco("com.senseauto.healthdetect:id/bt_confirm").click()  # 点击【我知道了】的按钮
        else:
            snapshot(msg="访客没有正常弹出信息填写确认提示弹框")
            poco("com.senseauto.healthdetect:id/bt_cancel").click()  # 没有弹出信息填写确认提示弹框那么就点击【取消】按钮退回到健康关怀首页



    @allure.story('访客答题环节')
    def test_face_health_visitor_answer(self):
        # 开始进行健康自评答题  第一题的答题
        if poco("com.senseauto.healthdetect:id/radioGroup").exists():
            assert_equal(poco(text="(单选) 你平时从事体力劳动的强度？").get_text(), "(单选) 你平时从事体力劳动的强度？", "第一题问题题目文案正确")
            poco(text="坐位工作，几乎无走动，如办公室职员").click()
            sleep(1.0)
            poco("com.senseauto.healthdetect:id/tv_next").click()
        else:
            poco("com.senseauto.healthdetect:id/tv_title").wait_for_appearance()

        # 开始进入下一题的答题
        if poco("com.senseauto.healthdetect:id/radioGroup").exists():
            assert_equal(poco(text="(单选) 你目前是否患有以下代谢性疾病?").get_text(), "(单选) 你目前是否患有以下代谢性疾病?", "第二题问题题目文案正确")
            poco(text="无").click()
            sleep(1.0)
            poco("com.senseauto.healthdetect:id/tv_next").click()
        else:
            poco("com.senseauto.healthdetect:id/tv_last").click()

        # 开始进入多选题的答题
        if poco("com.senseauto.healthdetect:id/vg_checkbox").exists():
            assert_equal(poco(text="(多选) 你目前是否患有以下心脑血管疾病？").get_text(), "(多选) 你目前是否患有以下心脑血管疾病？", "第三题多选问题题目文案正确")
            poco(text="高血压").click()
            poco(text="冠心病").click()
            poco(text="脑卒中").click()
            sleep(1.0)
            poco("com.senseauto.healthdetect:id/tv_next").click()
        else:
            poco("com.senseauto.healthdetect:id/tv_last").click()

        # 开始进入下一题的答题
        if poco("com.senseauto.healthdetect:id/radioGroup").exists():
            assert_equal(poco(text="(单选) 你是否饮酒？").get_text(), "(单选) 你是否饮酒？", "第四题问题题目文案正确")
            poco(text="平均每天0.5-1两酒精25g（0.5两）酒精=750ml啤酒=250ml葡萄酒=75ml 38度白酒=50ml高度白酒。").click()
            sleep(1.0)
            poco("com.senseauto.healthdetect:id/tv_next").click()
        else:
            poco("com.senseauto.healthdetect:id/tv_last").click()

        # 开始进入多选题的答题
        if poco("com.senseauto.healthdetect:id/vg_checkbox").exists():
            assert_equal(poco(text="(多选) 你是否有以下健康问题？").get_text(), "(多选) 你是否有以下健康问题？", "第五题多选问题题目文案正确")
            poco(text="心房纤颤").click()
            poco(text="左心室肥厚").click()
            sleep(1.0)
            poco("com.senseauto.healthdetect:id/tv_next").click()
        else:
            poco("com.senseauto.healthdetect:id/tv_last").click()

        # 开始进入下一题的答题
        if poco("com.senseauto.healthdetect:id/radioGroup").exists():
            assert_equal(poco(text="(单选) 你是否连续服用以下药物超过3个月？").get_text(), "(单选) 你是否连续服用以下药物超过3个月？", "第六题问题题目文案正确")
            poco(text="降压药").click()
            sleep(1.0)
            poco("com.senseauto.healthdetect:id/tv_next").click()
        else:
            poco("com.senseauto.healthdetect:id/tv_last").click()

        # 开始进入多选题的答题
        if poco("com.senseauto.healthdetect:id/vg_checkbox").exists():
            assert_equal(poco(text="(多选) 你是否有以下食物摄入超量问题？").get_text(), "(多选) 你是否有以下食物摄入超量问题？", "第七题多选问题题目文案正确")
            poco(text="喜好咸菜、火腿、各类炒货和腌制品").click()
            poco(text="饭菜放酱油、味精较多").click()
            sleep(1.0)
            poco("com.senseauto.healthdetect:id/tv_next").click()
        else:
            poco("com.senseauto.healthdetect:id/tv_last").click()

        # 开始进入多选题的答题
        if poco("com.senseauto.healthdetect:id/vg_checkbox").exists():
            assert_equal(poco(text="(多选) 你是否有以下食物摄入不足问题？").get_text(), "(多选) 你是否有以下食物摄入不足问题？", "第八题多选问题题目文案正确")
            poco(text="蔬菜摄入少，平均每日低于300g300g混合蔬菜约相当于11cm口径的碗1.5碗的量。").click()
            poco(text="水果摄入少，平均每日低于200g200g水果约相当于1个中等苹果的量。").click()
            sleep(1.0)
            poco("com.senseauto.healthdetect:id/tv_next").click()
        else:
            poco("com.senseauto.healthdetect:id/tv_last").click()

            # 开始进入下一题的答题
        if poco("com.senseauto.healthdetect:id/radioGroup").exists():
            assert_equal(poco(text="(单选) 你的吸烟情况？").get_text(), "(单选) 你的吸烟情况？", "第九题问题题目文案正确")
            poco(text="不抽烟但会接触二手烟，接触史≥20年").click()
            sleep(1.0)
            poco("com.senseauto.healthdetect:id/tv_next").click()
        else:
            poco("com.senseauto.healthdetect:id/tv_last").click()

        # 开始进入多选题的答题
        if poco("com.senseauto.healthdetect:id/vg_checkbox").exists():
            assert_equal(poco(text="(多选) 你是否经常存在以下精神状态？").get_text(), "(多选) 你是否经常存在以下精神状态？", "第十题多选问题题目文案正确")
            poco(text="心理压力大紧张").click()
            poco(text="焦虑、担忧").click()
            poco(text="恐慌").click()
            sleep(1.0)
            poco("com.senseauto.healthdetect:id/tv_next").click()
        else:
            poco("com.senseauto.healthdetect:id/tv_last").click()


    def teardown_method(self):
        stop_app('com.senseauto.healthdetect')