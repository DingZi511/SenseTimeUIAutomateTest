"""
===================================

Time：2023/7/4

===================================
"""
import yaml

class ReadYAML:
    def __init__(self):
        with open(".config/devices.yaml",'r',encoding='utf-8')as f:
            self.config_data = yaml.safe_load(f.read())["Android"]
        f.close()