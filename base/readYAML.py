"""
===================================
Author:商汤科技-刘孜煜
Time：2023/7/4
E-mail:liuziyu1@senseauto.com
Company:商汤科技
===================================
"""
import yaml

class ReadYAML:
    def __init__(self):
        with open(".config/devices.yaml",'r',encoding='utf-8')as f:
            self.config_data = yaml.safe_load(f.read())["Android"]
        f.close()